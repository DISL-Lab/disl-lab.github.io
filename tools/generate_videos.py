#!/usr/bin/env python3
"""
Generate background videos for the DISLab homepage with the Gemini API.

Veo models were shut down on the Gemini API (Oct 2026); this script uses the
successor video model (default: gemini-omni-1.2-flash) via the Interactions API.

Usage (from the repo root or anywhere):
    python3 tools/generate_videos.py --dry-run        # show requests, no API call
    python3 tools/generate_videos.py                  # generate all missing clips
    python3 tools/generate_videos.py hero --force     # regenerate one clip

Reads the API key from .env.local (repo root) (git-ignored).
Outputs:
    media/raw/<name>.mp4   original model output (git-ignored)
    media/<name>.mp4       web-ready: muted, seamless loop, compressed
    media/<name>.jpg       poster frame
Post-processing needs ffmpeg; without it the raw clip is copied as-is.
"""
import argparse
import base64
import json
import os
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent          # repo root
MEDIA = ROOT / "media"
RAW = MEDIA / "raw"
API = "https://generativelanguage.googleapis.com/v1beta"

STYLE = (
    " Visual style: premium research-lab aesthetic, deep navy (#0a1424) and cool blue (#1d6fe0) palette "
    "with soft white highlights, shallow depth of field, gentle film grain, calm and elegant. "
    "Camera: one continuous, slow, steady movement with no cuts, so the clip can loop. "
    "Avoid: any text, letters, numbers, captions, watermarks, logos, visible faces, flicker, fast motion, scene cuts."
)

LIGHT_STYLE = (
    " Visual style: premium research-lab aesthetic on a bright background — clean white (#ffffff) to very light "
    "cool gray-blue (#eef3fb) backdrop, with nodes and lines in deep navy (#0b1f44), cool blue (#2563eb) and a "
    "touch of teal (#0f9488); soft diffused daylight, gentle shadows, shallow depth of field, airy and elegant, "
    "high-key exposure. Camera: one continuous, slow, steady movement with no cuts, so the clip can loop. "
    "Avoid: dark backgrounds, neon glow, any text, letters, numbers, captions, watermarks, logos, visible faces, "
    "flicker, fast motion, scene cuts."
)

CLIPS = {
    # Full-bleed hero background. Abstract so the headline stays readable on top.
    "hero": (
        "A slow forward dolly through an abstract dark space where thousands of fine luminous particles "
        "flow like streams of data from the edges of the frame and gradually self-organize into a delicate, "
        "glowing three-dimensional network of nodes and thin connecting lines, like an AI agent's memory "
        "taking shape. Most of the frame stays dark and uncluttered, especially the left half." + STYLE
    ),
    # Same scene for the light theme: bright backdrop, dark nodes. Left half stays empty for the headline.
    "hero-light": (
        "A slow forward dolly through an abstract bright white space where thousands of fine navy and blue "
        "particles flow like streams of data from the edges of the frame and gradually self-organize into a "
        "delicate three-dimensional network of small spherical nodes and thin connecting lines, like an AI "
        "agent's memory taking shape. The network sits on the right side of the frame; most of the frame, "
        "especially the left half, stays clean, bright and uncluttered." + LIGHT_STYLE
    ),
    # Research area — Enterprise Agent AI
    "enterprise": (
        "A slow, smooth glide through a dark, minimal digital archive: translucent panels of documents, tables, "
        "charts, and dashboards float in orderly rows like a vast library. Thin luminous threads route between "
        "the panels as an AI agent retrieves, cross-references, and passes information between tools; small "
        "pulses of light travel along the routes and converge into one organized structure. Clean, precise, "
        "corporate." + STYLE
    ),
    # Research area — AI Scientist
    "ai-scientist": (
        "A slow orbit around translucent sheets of scientific papers, charts, and equations floating in a dark "
        "navy void. Thin glowing threads link passages between the sheets, forming an evolving citation and "
        "knowledge graph; small points of light travel along the threads as if an AI agent is reading, "
        "cross-checking evidence, and writing. Macro lens, soft volumetric light." + STYLE
    ),
    # Research area — Video Foundation Models → Factory AI
    "factory-ai": (
        "A slow cinematic tracking shot along a clean, modern, fully automated factory production line at "
        "night. Precise industrial robot arms assemble components; subtle translucent blue bounding boxes, "
        "motion trails, and timeline markers appear over objects and arms, as if a video foundation model is "
        "perceiving and reasoning over the scene in real time. Reflective floor, cool lighting, no workers' "
        "faces visible." + STYLE
    ),
    # Light-theme versions of the three application clips: same scenes, bright palette.
    "enterprise-light": (
        "A slow, smooth glide through a bright, minimal white digital archive: translucent frosted-glass panels "
        "of documents, tables, charts, and dashboards float in orderly rows like a vast, airy library. Thin navy "
        "and blue threads route between the panels as an AI agent retrieves, cross-references, and passes "
        "information between tools; small blue pulses travel along the routes and converge into one organized "
        "structure. Clean, precise, corporate." + LIGHT_STYLE
    ),
    "ai-scientist-light": (
        "A slow orbit around translucent white sheets of scientific papers, charts, and equations floating in a "
        "bright, softly lit white space. Thin navy and blue threads link passages between the sheets, forming an "
        "evolving citation and knowledge graph; small blue points travel along the threads as if an AI agent is "
        "reading, cross-checking evidence, and writing. Macro lens, soft diffused daylight." + LIGHT_STYLE
    ),
    "factory-ai-light": (
        "A slow cinematic tracking shot along a clean, modern, fully automated factory production line in bright "
        "daylight, with white walls, white robot arms and a light polished floor. Precise industrial robot arms "
        "assemble components; subtle translucent blue bounding boxes, motion trails, and timeline markers appear "
        "over objects and arms, as if a video foundation model is perceiving and reasoning over the scene in real "
        "time. No workers' faces visible." + LIGHT_STYLE
    ),
}


def load_env():
    env = {}
    f = ROOT / ".env.local"
    if f.exists():
        for line in f.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                env[k.strip()] = v.strip().strip('"').strip("'")
    for k in ("GEMINI_API_KEY", "VIDEO_MODEL", "VIDEO_RESOLUTION", "VIDEO_DURATION"):
        if os.environ.get(k):
            env[k] = os.environ[k]
    return env


def http(method, url, key, body=None, timeout=900):
    req = urllib.request.Request(url, method=method)
    req.add_header("x-goog-api-key", key)
    data = None
    if body is not None:
        data = json.dumps(body).encode()
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, data=data, timeout=timeout) as r:
            return r.read(), r.headers.get("Content-Type", "")
    except urllib.error.HTTPError as e:
        msg = e.read().decode(errors="replace")
        raise SystemExit(f"HTTP {e.code} from {url.split('?')[0]}\n{msg[:2000]}")


def find_video(obj):
    """Search the response for inline base64 video data or a file reference."""
    if isinstance(obj, dict):
        mime = str(obj.get("mime_type") or obj.get("mimeType") or "")
        if obj.get("data") and (mime.startswith("video") or obj.get("type") == "video"):
            return ("inline", obj["data"])
        for k in ("uri", "file_uri", "fileUri"):
            if isinstance(obj.get(k), str) and (mime.startswith("video") or obj.get("type") == "video" or "files/" in obj[k]):
                return ("uri", obj[k])
        for v in obj.values():
            hit = find_video(v)
            if hit:
                return hit
    elif isinstance(obj, list):
        for v in obj:
            hit = find_video(v)
            if hit:
                return hit
    return None


def strip_data(obj):
    if isinstance(obj, dict):
        return {k: ("<base64 omitted>" if k == "data" and isinstance(v, str) and len(v) > 200 else strip_data(v)) for k, v in obj.items()}
    if isinstance(obj, list):
        return [strip_data(v) for v in obj]
    return obj


def download_file(ref, key, dest):
    name = ref
    if "files/" in ref and not ref.startswith("files/"):
        name = "files/" + ref.split("files/", 1)[1].split(":")[0].split("?")[0]
    if not name.startswith("files/"):
        raw, _ = http("GET", ref, key)               # already a direct URL
        dest.write_bytes(raw)
        return
    for _ in range(120):                               # wait until the file is ACTIVE
        meta = json.loads(http("GET", f"{API}/{name}", key)[0])
        state = meta.get("state", "ACTIVE")
        if state == "ACTIVE":
            break
        if state == "FAILED":
            raise SystemExit(f"File {name} failed: {meta}")
        time.sleep(5)
    raw, _ = http("GET", f"{API}/{name}:download?alt=media", key)
    dest.write_bytes(raw)


def postprocess(name, raw_path):
    out, poster = MEDIA / f"{name}.mp4", MEDIA / f"{name}.jpg"
    if not shutil.which("ffmpeg"):
        shutil.copy(raw_path, out)
        print("  ffmpeg not found — copied raw clip (audio kept; page mutes it).")
        return
    dur = float(subprocess.check_output([
        "ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(raw_path)]).decode().strip())
    fade = 1.0
    # Seamless loop: start at t=fade and cross-fade the tail back into the first `fade` seconds.
    vf = (f"[0:v]split[a][b];[b]trim=0:{fade},setpts=PTS-STARTPTS[head];"
          f"[a]trim={fade},setpts=PTS-STARTPTS[body];"
          f"[body][head]xfade=transition=fade:duration={fade}:offset={dur - 2 * fade:.3f},"
          f"scale='min(1920,iw)':-2,format=yuv420p[v]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(raw_path), "-filter_complex", vf,
                    "-map", "[v]", "-an", "-c:v", "libx264", "-preset", "slow", "-crf", "26",
                    "-movflags", "+faststart", str(out)], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(out), "-vframes", "1",
                    "-q:v", "3", str(poster)], check=True)
    print(f"  web-ready: {out.relative_to(ROOT)} ({out.stat().st_size / 1e6:.1f} MB), poster: {poster.name}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("clips", nargs="*", help=f"subset of: {', '.join(CLIPS)}")
    ap.add_argument("--force", action="store_true", help="regenerate even if the clip exists")
    ap.add_argument("--dry-run", action="store_true", help="print the requests without calling the API")
    ap.add_argument("--postprocess-only", action="store_true", help="re-run ffmpeg on existing raw clips")
    a = ap.parse_args()

    env = load_env()
    model = env.get("VIDEO_MODEL") or "gemini-omni-1.2-flash"
    names = a.clips or list(CLIPS)
    for n in names:
        if n not in CLIPS:
            raise SystemExit(f"Unknown clip '{n}'. Choose from: {', '.join(CLIPS)}")
    RAW.mkdir(parents=True, exist_ok=True)

    for name in names:
        raw_path = RAW / f"{name}.mp4"
        if a.postprocess_only:
            if raw_path.exists():
                print(f"[{name}] post-processing"); postprocess(name, raw_path)
            continue
        if (MEDIA / f"{name}.mp4").exists() and not a.force:
            print(f"[{name}] exists — skip (use --force to regenerate)")
            continue
        body = {
            "model": model,
            "input": CLIPS[name],
            "response_format": {
                "type": "video",
                "aspect_ratio": "16:9",
                "resolution": env.get("VIDEO_RESOLUTION") or "1080p",
                "duration": env.get("VIDEO_DURATION") or "8s",
            },
        }
        if a.dry_run:
            print(f"[{name}] POST {API}/interactions\n{json.dumps(body, indent=2)}\n")
            continue
        key = env.get("GEMINI_API_KEY")
        if not key:
            raise SystemExit(f"GEMINI_API_KEY is empty. Put your key in {ROOT / '.env.local'}")

        print(f"[{name}] generating with {model} … (this can take a few minutes)")
        t0 = time.time()
        raw, _ = http("POST", f"{API}/interactions", key, body)
        resp = json.loads(raw)
        (RAW / f"{name}.response.json").write_text(json.dumps(strip_data(resp), indent=2))
        hit = find_video(resp)
        if not hit:
            raise SystemExit(f"No video found in response — see {RAW / (name + '.response.json')}")
        if hit[0] == "inline":
            raw_path.write_bytes(base64.b64decode(hit[1]))
        else:
            download_file(hit[1], key, raw_path)
        print(f"  saved raw clip ({raw_path.stat().st_size / 1e6:.1f} MB) in {time.time() - t0:.0f}s")
        postprocess(name, raw_path)

    if not a.dry_run:
        print("\nDone. Rebuild with tools/build_site.py — the page picks up media/*.mp4 automatically.")


if __name__ == "__main__":
    sys.exit(main())
