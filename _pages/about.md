---
layout: about
title: About
permalink: /
full_title: Data Intelligence System Lab (DISLab)
subtitle: Department of Industrial and Systems Engineering & Graduate School of Data Science, KAIST, South Korea

news: false
latest_posts: false
selected_papers: false
social: false
---

<style>
/* Scroll reveal */
.reveal {
  opacity: 0;
  transform: translateY(18px);
  transition: opacity 0.7s ease, transform 0.7s cubic-bezier(0.25, 0.8, 0.25, 1);
}
.reveal.is-visible {
  opacity: 1;
  transform: none;
}

/* Title styling */
.post-header .post-title {
  font-size: 2.1rem;
  font-weight: 800;
  background: linear-gradient(120deg, #4285f4 0%, #34a853 25%, #fbbc04 50%, #ea4335 75%, #4285f4 100%);
  background-size: 300% 100%;
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.3rem;
  animation: title-shimmer 8s ease-in-out infinite;
  letter-spacing: -0.01em;
}

@keyframes title-shimmer {
  0%, 100% { background-position: 0% 50%; }
  50%      { background-position: 100% 50%; }
}

.post-header .desc {
  display: none;
}

.dept-highlight {
  display: block;
  font-size: 0.9rem;
  color: #777;
  font-weight: 400;
  letter-spacing: 0.02em;
  margin-top: -0.3rem;
}

.dept-highlight .affiliated {
  display: block;
  font-size: 0.8rem;
  color: #999;
  margin-top: 0.2rem;
}

.dept-ise { color: #4285f4; font-weight: 600; }
.dept-ds { color: #34a853; font-weight: 600; }
.dept-ai { color: #e8a817; font-weight: 600; }

.hero-section {
  position: relative;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.8rem;
  margin-bottom: 2rem;
  padding: 1.5rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%);
  border-radius: 16px;
  border: 1px solid #e0e7ef;
  overflow: hidden;
  isolation: isolate;
}

.hero-section::before,
.hero-section::after {
  content: "";
  position: absolute;
  z-index: -1;
  border-radius: 50%;
  filter: blur(50px);
  opacity: 0.55;
  pointer-events: none;
}

.hero-section::before {
  width: 280px;
  height: 280px;
  background: radial-gradient(circle, #4285f4 0%, transparent 70%);
  top: -80px;
  right: -60px;
  animation: orb-float-a 14s ease-in-out infinite;
}

.hero-section::after {
  width: 240px;
  height: 240px;
  background: radial-gradient(circle, #34a853 0%, transparent 70%);
  bottom: -90px;
  left: -50px;
  animation: orb-float-b 18s ease-in-out infinite;
}

@keyframes orb-float-a {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50%      { transform: translate(-30px, 30px) scale(1.1); }
}

@keyframes orb-float-b {
  0%, 100% { transform: translate(0, 0) scale(1); }
  50%      { transform: translate(40px, -25px) scale(1.15); }
}

.hero-section > .img-col,
.hero-section > .text-col {
  position: relative;
  z-index: 1;
}

.hero-section .img-col {
  flex: 1 1 100%;
  max-width: 100%;
  text-align: center;
}

.hero-section .text-col {
  flex: 1 1 100%;
}

.hero-section img {
  width: 100%;
  height: auto;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
}

/* Slideshow */
.slideshow {
  position: relative;
  width: 100%;
  padding-top: 56.25%; /* 16:9 aspect ratio */
  overflow: hidden;
  border-radius: 12px;
  box-shadow: 0 6px 20px rgba(0,0,0,0.1);
  background: #f0f0f0;
}

.slideshow .slide {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  opacity: 0;
  transition: opacity 1s ease-in-out;
}

.slideshow .slide.active {
  opacity: 1;
}

.slideshow .slide img {
  width: 100%;
  height: 100%;
  display: block;
  border-radius: 12px;
  object-fit: cover;
  box-shadow: none;
}

.slide-caption {
  font-size: 0.75rem;
  color: #999;
  text-align: center;
  margin: 0.3rem 0 0 0;
  font-style: italic;
  min-height: 1.2em;
  transition: opacity 0.5s ease;
}

.slide-dots {
  display: flex;
  justify-content: center;
  gap: 0.4rem;
  margin-top: 0.5rem;
}

.slide-dots .dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: #ccc;
  border: none;
  padding: 0;
  cursor: pointer;
  transition: background 0.3s ease;
}

.slide-dots .dot.active {
  background: #4285f4;
}

.hero-section .text-col p {
  font-size: 0.95rem;
  line-height: 1.8;
  color: #444;
  margin: 0;
}

@media (max-width: 768px) {
  .hero-section {
    flex-direction: column;
    padding: 1.2rem;
  }
  .hero-section .img-col,
  .hero-section .text-col {
    flex: 1 1 100%;
    max-width: 100%;
  }
}

/* Research Pillars */
.pillars-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1rem;
  margin-bottom: 2rem;
}

@media (max-width: 600px) {
  .pillars-grid {
    grid-template-columns: 1fr;
  }
}

.pillar-card {
  position: relative;
  padding: 1.2rem 1.2rem 1.2rem 1.2rem;
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  border-top: 3px solid transparent;
  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
  overflow: hidden;
  isolation: isolate;
}

.pillar-card::before {
  content: "";
  position: absolute;
  inset: 0;
  z-index: -1;
  opacity: 0;
  transition: opacity 0.35s ease;
  background: linear-gradient(135deg, var(--pillar-accent, #4285f4) 0%, transparent 60%);
}

.pillar-card:hover {
  box-shadow: 0 12px 30px rgba(0,0,0,0.08);
  transform: translateY(-5px);
  border-color: transparent;
}

.pillar-card:hover::before {
  opacity: 0.06;
}

.pillar-card:nth-child(1) { --pillar-accent: #4285f4; border-top-color: #4285f4; }
.pillar-card:nth-child(2) { --pillar-accent: #34a853; border-top-color: #34a853; }
.pillar-card:nth-child(3) { --pillar-accent: #fbbc04; border-top-color: #fbbc04; }
.pillar-card:nth-child(4) { --pillar-accent: #ea4335; border-top-color: #ea4335; }

.pillar-icon {
  width: 36px;
  height: 36px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 9px;
  font-size: 1rem;
  margin-bottom: 0.6rem;
  background: color-mix(in srgb, var(--pillar-accent) 12%, transparent);
  color: var(--pillar-accent);
  transition: transform 0.35s cubic-bezier(0.25, 0.8, 0.25, 1), background 0.35s ease;
}

.pillar-card:hover .pillar-icon {
  transform: scale(1.08) rotate(-4deg);
  background: color-mix(in srgb, var(--pillar-accent) 18%, transparent);
}

.pillar-card .pillar-title {
  font-size: 0.95rem;
  font-weight: 700;
  margin: 0 0 0.4rem 0;
  color: #222;
}

.pillar-card:nth-child(1) .pillar-title { color: #4285f4; }
.pillar-card:nth-child(2) .pillar-title { color: #34a853; }
.pillar-card:nth-child(3) .pillar-title { color: #b8960c; }
.pillar-card:nth-child(4) .pillar-title { color: #ea4335; }

.pillar-card .pillar-desc {
  font-size: 0.82rem;
  color: #555;
  line-height: 1.65;
  margin: 0;
}

/* CTA Boxes */
.cta-box {
  position: relative;
  padding: 1.2rem 1.5rem 1.2rem 3.4rem;
  border-radius: 12px;
  margin-bottom: 1rem;
  font-size: 0.9rem;
  line-height: 1.7;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s ease;
}

.cta-box::before {
  position: absolute;
  left: 1.2rem;
  top: 1.2rem;
  width: 1.6rem;
  height: 1.6rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-family: "Font Awesome 6 Free";
  font-weight: 900;
  font-size: 0.95rem;
  border-radius: 8px;
}

.cta-box:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 24px rgba(0,0,0,0.06);
}

.cta-box.recruit {
  background: linear-gradient(135deg, #fff5f5 0%, #fee2e2 100%);
  border: 1px solid #fecaca;
  color: #991b1b;
}

.cta-box.recruit::before {
  content: "\f0a1"; /* bullhorn */
  background: #fecaca;
  color: #b91c1c;
}

.cta-box.recruit a {
  color: #dc2626;
  font-weight: 600;
}

.cta-box.info {
  background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
  border: 1px solid #bbf7d0;
  color: #166534;
}

.cta-box.info::before {
  content: "\f167"; /* youtube */
  font-family: "Font Awesome 6 Brands";
  background: #bbf7d0;
  color: #15803d;
}

.cta-box.note {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  color: #555;
  font-size: 0.85rem;
}

.cta-box.note::before {
  content: "\f05a"; /* info-circle */
  background: #e5e7eb;
  color: #6b7280;
}

.cta-box.note a {
  color: #4285f4;
  font-weight: 600;
}

.section-label {
  font-size: 0.95rem;
  font-weight: 600;
  color: #333;
  margin-bottom: 0.8rem;
}

/* News spotlight (top placement, eye-catching) */
.news-spotlight {
  position: relative;
  margin: 0 0 2rem 0;
  padding: 1.4rem 1.5rem 1.2rem;
  background: linear-gradient(135deg, #ffffff 0%, #f5f8ff 100%);
  border: 1px solid #e0e7ef;
  border-radius: 16px;
  box-shadow: 0 4px 18px rgba(66, 133, 244, 0.06);
}

.news-spotlight::before {
  content: "";
  position: absolute;
  top: 0;
  left: 1.5rem;
  right: 1.5rem;
  height: 3px;
  background: linear-gradient(90deg, #4285f4, #34a853, #fbbc04, #ea4335);
  border-radius: 0 0 3px 3px;
}

.news-spotlight-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
  flex-wrap: wrap;
  gap: 0.5rem;
}

.news-spotlight-title {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  margin: 0;
  font-size: 1.15rem;
  font-weight: 700;
  background: linear-gradient(135deg, #4285f4, #34a853);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.news-spotlight-title .live-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #ea4335;
  -webkit-text-fill-color: #ea4335;
  box-shadow: 0 0 0 0 rgba(234, 67, 53, 0.6);
  animation: live-pulse 2s infinite;
}

@keyframes live-pulse {
  0%   { box-shadow: 0 0 0 0 rgba(234, 67, 53, 0.6); }
  70%  { box-shadow: 0 0 0 8px rgba(234, 67, 53, 0); }
  100% { box-shadow: 0 0 0 0 rgba(234, 67, 53, 0); }
}

.news-spotlight-title .label-badge {
  font-size: 0.65rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  color: #fff;
  background: #ea4335;
  -webkit-text-fill-color: #fff;
  padding: 0.15rem 0.45rem;
  border-radius: 4px;
  text-transform: uppercase;
}

.news-view-all {
  font-size: 0.8rem;
  font-weight: 600;
  color: #4285f4;
  text-decoration: none;
  white-space: nowrap;
  transition: transform 0.2s ease;
}

.news-view-all:hover {
  text-decoration: none;
  transform: translateX(3px);
  color: #1a73e8;
}

/* Override the styles inside news.html include for tighter look in spotlight */
.news-spotlight .news-scroll {
  max-height: 260px;
}
.news-spotlight .news-list {
  gap: 0.4rem;
}
.news-spotlight .news-item {
  background: rgba(255, 255, 255, 0.7);
  border-color: #eef2f7;
  padding: 0.6rem 0.85rem;
}
.news-spotlight .news-item:hover {
  background: #ffffff;
  border-color: #c7d6f0;
  box-shadow: 0 4px 14px rgba(66, 133, 244, 0.08);
}
.news-spotlight .news-date {
  font-size: 0.68rem;
}
.news-spotlight .news-content {
  font-size: 0.83rem;
}
</style>

<p class="dept-highlight">
  <span class="dept-ise">Department of Industrial and Systems Engineering</span> & <span class="dept-ds">Graduate School of Data Science</span>, KAIST, South Korea
  <span class="affiliated">Also, affiliated with <span class="dept-ai">Department of AX at the KAIST College of AI</span></span>
</p>

<div class="cta-box recruit reveal">
  <strong>Internship (상시 모집)</strong><br>
  관심 있는 학생은 아래 양식을 작성하고 저에게 이메일 보내주세요.<br>
  Internships are offered on a rolling basis. Interested students are encouraged to complete the form and email me.
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSezVnp3eepLI4CTD3_lLABNwDtvFue6EqhXKq1zhK5zLW9ZsQ/viewform?usp=sharing&ouid=114425768257170495941" target="_blank">[Apply Here]</a>
</div>

<div class="hero-section reveal">
  <div class="img-col">
    <div class="slideshow" id="heroSlideshow">
      <div class="slide active">
        <img src="/assets/img/main/26-04-02.png" alt="2026 Strawberry Party at KAIST">
      </div>
      <div class="slide">
        <img src="/assets/img/main/26-02-12.png" alt="2026 Graduation Ceremony at KAIST">
      </div>
      <div class="slide">
        <img src="/assets/img/main/25-07-04.png" alt="2025 KCC at Jeju Island">
      </div>
      <div class="slide">
        <img src="/assets/img/main/25-04-07.png" alt="2025 Strawberry Party at KAIST">
      </div>
    </div>
    <p class="slide-caption" id="slideCaption">2026 Strawberry Party at KAIST</p>
    <div class="slide-dots" id="slideDots">
      <button class="dot active" onclick="goToSlide(0)"></button>
      <button class="dot" onclick="goToSlide(1)"></button>
      <button class="dot" onclick="goToSlide(2)"></button>
      <button class="dot" onclick="goToSlide(3)"></button>
    </div>
  </div>
  <div class="text-col">
    <p>
      Welcome to <span style="background-color: #e8f0fe; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 700;">DISLab</span>! We are dedicated to building trustworthy Agentic AI systems grounded in <span style="background-color: #fff8e1; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 600;">data-centric</span> intelligence. We believe that intelligence does not emerge from model scale alone, but from how data is perceived, structured, remembered, and used throughout an agent's lifecycle. We study how <span style="background-color: #e6f4ea; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 600;">data quality</span>, <span style="background-color: #e6f4ea; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 600;">data structure</span>, and <span style="background-color: #e6f4ea; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 600;">data utilization</span> fundamentally shape an agent's ability to reason, act, and adapt in complex real-world environments. Our goal is to design AI agents that can operate reliably under noisy inputs, long contexts, and imperfect information.
    </p>
  </div>
</div>

<div class="news-spotlight reveal">
  <div class="news-spotlight-header">
    <h2 class="news-spotlight-title">
      <span class="live-dot"></span>
      <span class="label-badge">News</span>
      Latest Updates
    </h2>
    <a href="{{ '/news/' | relative_url }}" class="news-view-all">View All →</a>
  </div>
  {% include news.html limit=true %}
</div>

<p class="section-label">Our research is organized around four core components of Agentic AI:</p>

<div class="pillars-grid reveal">
  <div class="pillar-card">
    <p class="pillar-title">Agent Perception</p>
    <p class="pillar-desc">Understanding multi-modal and long-context signals across text, images, video, and other sensory inputs to perceive complex environments.</p>
  </div>
  <div class="pillar-card">
    <p class="pillar-title">Agent Intelligence</p>
    <p class="pillar-desc">Developing reasoning and decision-making capabilities that integrate world understanding with value alignment to enable purposeful and safe agent behavior.</p>
  </div>
  <div class="pillar-card">
    <p class="pillar-title">Agent Memory</p>
    <p class="pillar-desc">Designing memory and information compression mechanisms that organize, store, and retrieve knowledge over long horizons for consistent agent behaviors.</p>
  </div>
  <div class="pillar-card">
    <p class="pillar-title">Agent Modeling</p>
    <p class="pillar-desc">Building efficient and controllable agent models through knowledge distillation, compression, safety guardrails, and automatic evaluation.</p>
  </div>
</div>

<div class="cta-box note reveal">
  <span style="background-color: #fff3bf; padding: 0.15rem 0.4rem; border-radius: 3px; font-weight: 700; color: #8a6d00;">We are recruiting MS students for Spring/Fall 2027 (1 Korean MS position).</span> If you are interested in joining our lab for graduate studies, we strongly encourage you to apply for an internship first, as priority will be given to those with prior research experience in our group. Intern positions are always open. During the internship, students will work closely with graduate students on ongoing academic research projects and gain hands-on experience in conducting research, developing ideas, and contributing to publications.
</div>

<div class="cta-box info reveal">
  You can catch up on our recent research on <a href="https://www.youtube.com/channel/UCrEpnN7_2BmrHsPWns_Vx3Q" target="_blank" style="color: #166534; font-weight: 600;">our YouTube channel</a>.
</div>

<div class="visitor-counter reveal">
  <span class="vc-pill">
    <span class="vc-dot"></span>
    <i class="fas fa-eye vc-eye"></i>
    <span class="vc-seg">
      <span class="vc-num" id="vcToday">—</span>
      <span class="vc-cap">today</span>
    </span>
    <span class="vc-sep">·</span>
    <span class="vc-seg">
      <span class="vc-num" id="vcTotal">—</span>
      <span class="vc-cap">total</span>
    </span>
  </span>
  <span class="vc-since">since Apr 27, 2026</span>
</div>

<style>
.visitor-counter {
  margin-top: 2.2rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
}

.visitor-counter .vc-pill {
  display: inline-flex;
  align-items: center;
  gap: 0.55rem;
  padding: 0.4rem 0.95rem;
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid #e0e7ef;
  border-radius: 999px;
  box-shadow: 0 2px 8px rgba(66, 133, 244, 0.06), 0 1px 2px rgba(0,0,0,0.03);
  font-size: 0.82rem;
  color: #555;
  transition: transform 0.25s ease, box-shadow 0.25s ease;
  position: relative;
  overflow: hidden;
}

.visitor-counter .vc-pill::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  padding: 1px;
  background: linear-gradient(135deg, rgba(66,133,244,0.25), rgba(52,168,83,0.25), rgba(251,188,4,0.25));
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  pointer-events: none;
  opacity: 0.6;
}

.visitor-counter .vc-pill:hover {
  transform: translateY(-1px);
  box-shadow: 0 6px 18px rgba(66, 133, 244, 0.12), 0 2px 4px rgba(0,0,0,0.04);
}

.visitor-counter .vc-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #34a853;
  flex-shrink: 0;
  box-shadow: 0 0 0 0 rgba(52, 168, 83, 0.55);
  animation: vc-pulse 2s infinite;
}

@keyframes vc-pulse {
  0%   { box-shadow: 0 0 0 0 rgba(52, 168, 83, 0.55); }
  70%  { box-shadow: 0 0 0 6px rgba(52, 168, 83, 0); }
  100% { box-shadow: 0 0 0 0 rgba(52, 168, 83, 0); }
}

.visitor-counter .vc-eye {
  font-size: 0.82rem;
  background: linear-gradient(135deg, #4285f4, #34a853);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.visitor-counter .vc-seg {
  display: inline-flex;
  align-items: baseline;
  gap: 0.3rem;
}

.visitor-counter .vc-num {
  font-size: 0.95rem;
  font-weight: 800;
  line-height: 1;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.01em;
  background: linear-gradient(135deg, #4285f4, #34a853);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.visitor-counter .vc-seg:last-of-type .vc-num {
  background: linear-gradient(135deg, #34a853, #fbbc04);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.visitor-counter .vc-cap {
  font-size: 0.7rem;
  color: #888;
  font-weight: 500;
  letter-spacing: 0.02em;
}

.visitor-counter .vc-sep {
  color: #d1d5db;
  font-weight: 400;
  margin: 0 0.05rem;
}

.visitor-counter .vc-since {
  font-size: 0.68rem;
  color: #aaa;
  font-style: italic;
  letter-spacing: 0.02em;
}

@keyframes vc-num-in {
  from { opacity: 0; transform: translateY(4px); }
  to   { opacity: 1; transform: none; }
}

.visitor-counter .vc-num.loaded {
  animation: vc-num-in 0.4s ease;
}
</style>

<script>
(function() {
  const captions = [
    "2026 Strawberry Party at KAIST",
    "2026 Graduation Ceremony at KAIST",
    "2025 KCC at Jeju Island",
    "2025 Strawberry Party at KAIST"
  ];
  const slides = document.querySelectorAll('#heroSlideshow .slide');
  const dots = document.querySelectorAll('#slideDots .dot');
  const caption = document.getElementById('slideCaption');
  let current = 0;
  let timer;

  function goTo(idx) {
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = idx;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
    caption.textContent = captions[current];
  }

  function next() {
    goTo((current + 1) % slides.length);
  }

  function startTimer() {
    timer = setInterval(next, 5000);
  }

  window.goToSlide = function(idx) {
    clearInterval(timer);
    goTo(idx);
    startTimer();
  };

  startTimer();
})();

(function() {
  const fmt = n => Number(n).toLocaleString('en-US');

  const animate = (el, target) => {
    const dur = 800;
    const start = performance.now();
    const ease = t => 1 - Math.pow(1 - t, 3);
    const step = (now) => {
      const t = Math.min(1, (now - start) / dur);
      el.textContent = fmt(Math.round(target * ease(t)));
      if (t < 1) requestAnimationFrame(step);
    };
    el.classList.add('loaded');
    requestAnimationFrame(step);
  };

  const setNum = (id, v) => {
    const el = document.getElementById(id);
    if (!el) return;
    animate(el, v);
  };

  const NS = 'disl-lab-github-io';
  const today = new Date().toISOString().slice(0, 10);
  const totalUrl = 'https://abacus.jasoncameron.dev/hit/' + NS + '/total';
  const todayUrl = 'https://abacus.jasoncameron.dev/hit/' + NS + '/' + today;

  fetch(totalUrl)
    .then(r => r.ok ? r.json() : Promise.reject())
    .then(d => setNum('vcTotal', d.value))
    .catch(() => {});

  fetch(todayUrl)
    .then(r => r.ok ? r.json() : Promise.reject())
    .then(d => setNum('vcToday', d.value))
    .catch(() => {});
})();

(function() {
  const els = document.querySelectorAll('.reveal');
  if (!('IntersectionObserver' in window) || !els.length) {
    els.forEach(el => el.classList.add('is-visible'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('is-visible');
        io.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
  els.forEach(el => io.observe(el));
})();
</script>
