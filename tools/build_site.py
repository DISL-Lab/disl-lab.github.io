#!/usr/bin/env python3
"""
Build the DISLab homepage (index.html at the repo root).

Reads (repo root):
    _pages/publications.md   publication list (year sections + project-block entries)
    _news/*.md               news items
Template:
    tools/templates/nextgen.html  -> index.html

Usage:
    python3 tools/build_site.py

Korean news translations live in KO_NEWS below: add a line when you add a news item
(match on a distinctive English substring). Untranslated items fall back to English.
"""
import glob
import html
import json
import os
import re
import sys

TOOLS = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(TOOLS)                # repo root
OUT = REPO
TPL = os.path.join(TOOLS, "templates")

ACTIVE_PROJECTS = 10
MEMBERS = 24  # postdoc + Ph.D. + M.S. + co-advised + interns (PI and staff excluded)

KO_NEWS = [
    ("Three papers were accepted at NeurIPS 2026", "NeurIPS 2026에 논문 3편이 채택되었습니다."),
    ("Six papers were accepted at EMNLP 2026", "EMNLP 2026에 논문 6편, CIKM 2026에 논문 2편이 채택되었습니다."),
    ("Three MS students", "석사과정 3명(Seunghwan, Jibin, Yeeun)과 인턴 3명(Hwan, Byeongjun, Chanjoong)이 DISLab에 합류했습니다."),
    ("Four papers on RAG", "RAG, 시뮬레이션, 요약에 관한 논문 4편이 COLM 2026에 채택되었습니다."),
    ("efficient VLM", "효율적인 VLM에 관한 논문이 ECCV 2026에 채택되었습니다."),
    ("APEC ASPIRE", "송환준 교수가 APEC 회원국별로 대표 연구자 1인을 선정하는 APEC ASPIRE 상의 한국 대표로 선정되었습니다."),
    ("Conversational Search", "대화형 검색과 그래프 신경망에 관한 논문 2편이 ICML 2026에 채택되었습니다."),
    ("Six papers on Alignment", "정렬 튜닝, 추론, 분석에 관한 논문 6편이 ACL 2026에 채택되었습니다."),
    ("Ewon Assistant Professor", "송환준 교수가 KAIST의 우수 신임교원 직위인 Ewon 조교수로 임용되었습니다 (2026.03–2029.02)."),
    ("(Yujin and Taewon)", "Yujin, Taewon 학생이 올여름 NVIDIA(미국 산타클라라)와 AWS AI(미국 뉴욕)에서 인턴십을 진행합니다."),
    ("Information Retrieval was accepted at ICLR 2026", "정보 검색에 관한 논문이 ICLR 2026에 채택되었습니다."),
    ("Technology Innovation Award", "송환준 교수가 2025년 우수 기술 성과를 인정받아 KAIST 기술혁신상을 수상했습니다."),
    ("WSDM 2026", "강건한 검색 증강 생성(RAG)에 관한 논문이 WSDM 2026에 채택되었습니다."),
    ("Long Document Comprehension", "LLM 기반 장문 문서 이해와 추천 시스템에 관한 논문 2편이 EMNLP 2025에 채택되었습니다."),
    ("Keynote Speaker", "송환준 교수가 CIKM과 함께 열린 International Workshop on Retrieval-Driven Generative AI & ScienceON AI Challenge에 기조연설자로 초청되었습니다."),
    ("AAAI 2026", "송환준 교수가 AAAI 2026 Area Chair로 위촉되어 투고 논문 100편을 담당합니다."),
    ("Reflective Reasoning", "텍스트 요약을 위한 반성적 추론(Reflective Reasoning)에 관한 논문이 COLM 2025에 채택되었습니다."),
    ("Data Condensation", "노이즈 레이블 환경의 데이터 압축(Data Condensation)에 관한 논문이 ICCV 2025에 채택되었습니다."),
    ("dissertation defense", "석사과정 Yuho Lee, Taewon Yun 학생이 석사 학위논문 심사를 통과했습니다."),
    ("Area Chair at ICLR 2026", "송환준 교수가 NeurIPS 2025, ICLR 2025에 이어 ICLR 2026 Area Chair로 위촉되었습니다."),
    ("SIGIR 2025", "LLM 기반 추천 시스템에 관한 논문이 SIGIR 2025 (GENNEXT Workshop)에 채택되었습니다."),
    ("ACL 2025", "LLM 벤치마킹과 RAG 검색에 관한 논문 2편이 ACL 2025에 채택되었습니다."),
    ("KDD 2025", "시계열 바이모달 학습에 관한 논문이 KDD 2025 Research Track에 채택되었습니다."),
    ("ICWSM 2025", "시계열 벤치마크 데이터셋에 관한 논문이 ICWSM 2025에 채택되었습니다."),
    ("Minjeong Ban and Kibum Kim", "신입 석사과정 Minjeong Ban, Kibum Kim 학생이 DISLab에 합류했습니다."),
    ("AWS Bedrock team", "석사과정 Yuho Lee 학생이 올여름 Amazon Web Services(AWS Bedrock 팀) Applied Scientist 인턴으로 합류합니다."),
    ("Hallucination and Preference", "환각(Hallucination)과 선호 최적화에 관한 논문 2편이 NAACL 본 학회에 채택되었으며, 두 편 모두 구두 발표(Oral)로 선정되었습니다."),
    ("Test Time Adaptation", "RAG 기반 테스트 시점 적응(Test-Time Adaptation)에 관한 논문이 ICLR 2025에 채택되었습니다."),
    ("Fact Verification", "사실 검증(Fact Verification)에 관한 논문이 COLING 2025에 채택되었으며, 구두 발표(Oral)로 선정되었습니다."),
]
TYPO_FIXES = [("acceptd", "accepted"), ("A papers", "A paper"), ("Two paper ", "Two papers "), ("retreival", "retrieval"),
              ("Summariation", "Summarization"), ("nomiated", "nominated"), ("CKIM", "CIKM"), ("has joined in", "have joined"), ("  ", " ")]


def clean(t):
    return html.unescape(re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", t)).strip())


def parse_publications():
    s = open(os.path.join(REPO, "_pages/publications.md")).read()
    s = re.sub(r"<!--.*?-->", "", s, flags=re.S)
    marks = [(m.start(), "Preprint") for m in re.finditer(r"<h2[^>]*>\s*Preprint\s*</h2>", s)]
    marks += [(m.start(), m.group(1).replace("–", "-"))
              for m in re.finditer(r'letter-spacing:\s*0\.1em;">\s*([0-9]{4}(?:\s*[-–]\s*[0-9]{4})?)\s*</div>', s)]
    marks.sort()
    starts = [m.start() for m in re.finditer(r'<div class="project-block">', s)]
    pubs = []
    for k, st in enumerate(starts):
        end = starts[k + 1] if k + 1 < len(starts) else len(s)
        later = [p for p, _ in marks if p > st]
        if later:
            end = min(end, later[0])
        chunk = s[st:end]
        year = ([y for p, y in marks if p < st] or ["Preprint"])[-1].replace(" ", "")
        h3 = re.search(r"<h3[^>]*>(.*?)</h3>", chunk, re.S)
        if not h3:
            print("!! no title in block at char", st, file=sys.stderr)
            continue
        badges = [clean(x) for x in re.findall(r'<span style="[^"]*">\s*(.*?)\s*</span>', h3.group(1), re.S)]
        title = clean(re.sub(r"<span.*?</span>", "", h3.group(1), flags=re.S))
        ps = re.findall(r"<p[^>]*>(.*?)</p>", chunk, re.S)
        auth = ps[0] if ps else ""
        collab = re.search(r"\((with [^)]*)\)", clean(auth))
        authors = clean(re.sub(r"<span.*?</span>", "", auth, flags=re.S))
        venue = clean(ps[1]) if len(ps) > 1 else ""
        img = re.search(r'<img src="([^"]+)"', chunk)
        links = [[u, clean(l)] for u, l in re.findall(r'href="(http[^"]+)"[^>]*>(.*?)</a>', chunk, re.S)][:3]
        tag = badges[0] if badges else ""
        conf = re.sub(r"-(main|Main|Findings|findings)$", "", re.sub(r"\s*\(.*?\)", "", tag)).strip()
        if conf.lower() in ("acl", "emnlp", "naacl"):
            conf = conf.upper()
        # ACL / EMNLP / NAACL: Main vs Findings, read from the venue line, e.g. "... (Findings), 2026"
        tm = re.search(r"\((Main|Findings)\)", venue)
        track = tm.group(1) if tm and conf in ("ACL", "EMNLP", "NAACL") else ""
        oral = "oral" in tag.lower()
        yrm = re.search(r"(\d{4})\s*$", venue)
        yr = year if re.fullmatch(r"\d{4}", year) else (yrm.group(1) if yrm else "")
        label = conf + (f" {track}" if track else "") + (" · Oral" if oral else "")
        short = f"{conf}'{yr[2:]}" + (f" {track}" if track else "") + (" Oral" if oral else "")
        pubs.append(dict(year=year, img=img.group(1).replace("/assets/img/", "assets/img/") if img else "",
                         venue_tag=tag, venue_short=conf, label=label, short=short,  # venue_short: stats group Main+Findings
                         track=track, topic=badges[1] if len(badges) > 1 else "",
                         title=title, authors=authors, collab=collab.group(1) if collab else "",
                         venue=venue, links=links))
    if len(pubs) != len(starts):
        print(f"!! parsed {len(pubs)} of {len(starts)} publication blocks", file=sys.stderr)
    return pubs


def parse_news():
    news = []
    for f in glob.glob(os.path.join(REPO, "_news/*.md")):
        s = open(f).read()
        d = re.search(r"date:\s*(\d{4})-(\d{1,2})-(\d{1,2})", s)
        body = re.sub(r"<[^>]+>", "", s.split("---", 2)[2].strip())
        for a, b in TYPO_FIXES:
            body = body.replace(a, b)
        t = body.lower()
        tag = ("paper" if "accept" in t else
               "award" if any(k in t for k in ["award", "appointed", "selected as the korean"]) else
               "service" if any(k in t for k in ["area chair", "keynote", "speaker"]) else "people")
        ko = next((k for sub, k in KO_NEWS if sub in body), "")
        if not ko:
            print("!! no Korean translation for news:", body[:80], file=sys.stderr)
        news.append(dict(date="%s-%02d-%02d" % (d.group(1), int(d.group(2)), int(d.group(3))), text=body, ko=ko, tag=tag))
    news.sort(key=lambda n: n["date"], reverse=True)
    return news


def main():
    pubs, news = parse_publications(), parse_news()
    years = {}
    for p in pubs:
        years[p["year"]] = years.get(p["year"], 0) + 1
    print("publications:", len(pubs), years)
    print("news:", len(news))

    def fill(h, variant=""):
        return (h.replace("__VARIANT__", variant)
                 .replace("__PUBS__", json.dumps(pubs, ensure_ascii=False))
                 .replace("__NEWS__", json.dumps(news, ensure_ascii=False))
                 .replace("__PUBS_TOTAL__", str(len(pubs)))
                 .replace("__PUBS_2026__", str(years.get("2026", 0)))
                 .replace("__MEMBERS__", str(MEMBERS))
                 .replace("__ACTIVE_PROJ__", str(ACTIVE_PROJECTS)))

    nextgen = open(os.path.join(TPL, "nextgen.html")).read()
    outputs = {"index.html": fill(nextgen)}
    for name, body in outputs.items():
        left = set(re.findall(r"__[A-Z_]{3,}__", body))
        open(os.path.join(OUT, name), "w").write(body)
        print(f"  wrote {name}" + (f"  (unfilled: {left})" if left else ""))


if __name__ == "__main__":
    main()
