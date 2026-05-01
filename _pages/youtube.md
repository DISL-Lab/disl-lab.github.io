---
layout: page
permalink: /youtube/
title: YouTube
description: ""
nav: true
nav_order: 6
---

{% capture yt_stats %}
<span class="ph-stat s4"><i class="fab fa-youtube" style="color:#ff0000;"></i> @DISL-LAB</span>
<span class="ph-stat s1">Research Talks</span>
<span class="ph-stat s2">Paper Presentations</span>
<span class="ph-stat s3">Lab Highlights</span>
{% endcapture %}
{% include page_hero.html
   eyebrow="Video Channel"
   title="DISLab on YouTube"
   subtitle="Research talks, paper presentations, and lab highlights — catch up on our latest work in video form. Sorted from newest to oldest."
   stats=yt_stats
   orb_a="#ff0000"
   orb_b="#4285f4"
   eyebrow_color="#ff0000" %}

<style>
.yt-featured {
  position: relative;
  margin: 0 0 2rem 0;
  background: #000;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 8px 28px rgba(0,0,0,0.12);
  aspect-ratio: 16 / 9;
}

.yt-featured iframe {
  width: 100%;
  height: 100%;
  border: 0;
  display: block;
}

.yt-section-label {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 1.5rem 0 1rem 0;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.yt-section-label h2 {
  font-size: 1.05rem;
  font-weight: 700;
  margin: 0;
  color: #222;
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
}

.yt-section-label h2::before {
  content: "";
  display: inline-block;
  width: 4px;
  height: 18px;
  border-radius: 2px;
  background: linear-gradient(180deg, #ff0000, #b91c1c);
}

.yt-section-label .yt-channel-link {
  font-size: 0.8rem;
  font-weight: 600;
  color: #ff0000;
  text-decoration: none;
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  transition: transform 0.2s ease;
}

.yt-section-label .yt-channel-link:hover {
  transform: translateX(3px);
  color: #b91c1c;
}

.yt-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.yt-card {
  display: flex;
  flex-direction: column;
  text-decoration: none;
  color: inherit;
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s ease, border-color 0.3s ease;
}

.yt-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 26px rgba(0,0,0,0.08);
  border-color: #ffd6d6;
  text-decoration: none;
  color: inherit;
}

.yt-thumb-wrap {
  position: relative;
  aspect-ratio: 16 / 9;
  overflow: hidden;
  background: #f0f0f0;
}

.yt-thumb-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.yt-card:hover .yt-thumb-wrap img {
  transform: scale(1.05);
}

.yt-thumb-wrap::after {
  content: "";
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%) scale(0.9);
  width: 48px;
  height: 48px;
  background: rgba(0, 0, 0, 0.7);
  border-radius: 50%;
  background-image: url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='white'><path d='M8 5v14l11-7z'/></svg>");
  background-repeat: no-repeat;
  background-position: center;
  background-size: 22px 22px;
  opacity: 0.85;
  transition: transform 0.3s ease, background 0.3s ease;
}

.yt-card:hover .yt-thumb-wrap::after {
  transform: translate(-50%, -50%) scale(1.05);
  background-color: #ff0000;
  opacity: 1;
}

.yt-card-body {
  padding: 0.85rem 0.95rem 1rem;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.yt-card-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: #222;
  line-height: 1.4;
  margin: 0 0 0.4rem 0;
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}

.yt-card-meta {
  font-size: 0.72rem;
  color: #888;
  margin-top: auto;
  display: flex;
  align-items: center;
  gap: 0.4rem;
}

.yt-card-meta .yt-dot {
  width: 3px;
  height: 3px;
  border-radius: 50%;
  background: #ccc;
}

/* States */
.yt-loading,
.yt-error {
  text-align: center;
  padding: 3rem 1.5rem;
  color: #888;
  background: #fafafa;
  border: 1px dashed #e5e7eb;
  border-radius: 12px;
}

.yt-loading .yt-spinner {
  display: inline-block;
  width: 24px;
  height: 24px;
  border: 3px solid #e5e7eb;
  border-top-color: #ff0000;
  border-radius: 50%;
  animation: yt-spin 0.8s linear infinite;
  margin-bottom: 0.6rem;
}

@keyframes yt-spin {
  to { transform: rotate(360deg); }
}

.yt-error a {
  color: #ff0000;
  font-weight: 600;
}

/* Channel CTA at bottom */
.yt-cta {
  margin-top: 2rem;
  padding: 1.4rem 1.5rem;
  text-align: center;
  background: linear-gradient(135deg, #fff5f5 0%, #fee2e2 100%);
  border: 1px solid #fecaca;
  border-radius: 14px;
}

.yt-cta p {
  margin: 0 0 0.8rem 0;
  font-size: 0.9rem;
  color: #7f1d1d;
}

.yt-cta a.yt-cta-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.55rem 1.1rem;
  background: #ff0000;
  color: #fff;
  font-weight: 600;
  font-size: 0.85rem;
  text-decoration: none;
  border-radius: 8px;
  transition: transform 0.2s ease, background 0.2s ease;
}

.yt-cta a.yt-cta-btn:hover {
  background: #b91c1c;
  transform: translateY(-2px);
  text-decoration: none;
  color: #fff;
}

@media (max-width: 480px) {
  .yt-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<div class="yt-featured">
  <iframe
    src="https://www.youtube.com/embed/videoseries?list=UUrEpnN7_2BmrHsPWns_Vx3Q&autoplay=0"
    title="DISLab YouTube — Latest Videos Playlist"
    allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    allowfullscreen
    loading="lazy"></iframe>
</div>

<div class="yt-section-label">
  <h2>All Videos · Newest first</h2>
  <a href="https://www.youtube.com/@DISL-LAB" target="_blank" rel="noopener" class="yt-channel-link">
    Visit channel <i class="fas fa-arrow-right"></i>
  </a>
</div>

<div id="ytGrid" class="yt-grid">
  <div class="yt-loading" style="grid-column: 1 / -1;">
    <div class="yt-spinner"></div>
    <div>Loading videos from YouTube…</div>
  </div>
</div>

<div class="yt-cta">
  <p>For the full archive — including older talks and lectures —ㅆ visit our channel directly.</p>
  <a href="https://www.youtube.com/@DISL-LAB" target="_blank" rel="noopener" class="yt-cta-btn">
    <i class="fab fa-youtube"></i> Browse Full Archive on YouTube
  </a>
</div>

<script>
(function() {
  const CHANNEL_ID = 'UCrEpnN7_2BmrHsPWns_Vx3Q';
  const RSS_URL    = 'https://www.youtube.com/feeds/videos.xml?channel_id=' + CHANNEL_ID;
  const API_URL    = 'https://api.rss2json.com/v1/api.json?rss_url=' + encodeURIComponent(RSS_URL);
  const grid       = document.getElementById('ytGrid');

  const fmtDate = (iso) => {
    const d = new Date(iso);
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  };

  const escapeHtml = (s) => s.replace(/[&<>"']/g, c => ({
    '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;'
  }[c]));

  const videoIdFromLink = (link) => {
    const m = link.match(/[?&]v=([^&]+)/) || link.match(/youtu\.be\/([^?&]+)/);
    return m ? m[1] : null;
  };

  const renderError = () => {
    grid.innerHTML = '<div class="yt-error" style="grid-column: 1 / -1;">' +
      '<p>Could not load videos right now.</p>' +
      '<p><a href="https://www.youtube.com/@DISL-LAB" target="_blank" rel="noopener">Browse on YouTube →</a></p>' +
    '</div>';
  };

  fetch(API_URL)
    .then(r => r.ok ? r.json() : Promise.reject())
    .then(data => {
      if (!data || !data.items || !data.items.length) {
        renderError();
        return;
      }
      const items = data.items;
      const html = items.map(item => {
        const vid = videoIdFromLink(item.link);
        if (!vid) return '';
        const thumb = 'https://i.ytimg.com/vi/' + vid + '/mqdefault.jpg';
        const title = escapeHtml(item.title || 'Untitled');
        const date  = item.pubDate ? fmtDate(item.pubDate) : '';
        return '<a class="yt-card" href="' + item.link + '" target="_blank" rel="noopener" aria-label="' + title + '">' +
          '<div class="yt-thumb-wrap"><img src="' + thumb + '" alt="" loading="lazy" onerror="this.style.opacity=0.3"></div>' +
          '<div class="yt-card-body">' +
            '<p class="yt-card-title">' + title + '</p>' +
            '<div class="yt-card-meta"><i class="fab fa-youtube" style="color:#ff0000;"></i><span class="yt-dot"></span><span>' + date + '</span></div>' +
          '</div>' +
        '</a>';
      }).join('');
      grid.innerHTML = html;
    })
    .catch(renderError);
})();
</script>
