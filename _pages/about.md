---
layout: about
title: About
permalink: /
full_title: Data Intelligence System Lab (DISLab)
subtitle: Department of Industrial and Systems Engineering & Graduate School of Data Science, KAIST, South Korea

news: true
latest_posts: false
selected_papers: false
social: false
---

<style>
/* Title styling */
.post-header .post-title {
  font-size: 2rem;
  font-weight: 800;
  background: linear-gradient(135deg, #4285f4, #34a853);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  margin-bottom: 0.3rem;
}

.post-header .desc {
  font-size: 0.9rem;
  color: #777;
  font-weight: 400;
  letter-spacing: 0.02em;
}

.hero-section {
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
  grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.pillar-card {
  padding: 1.2rem;
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 12px;
  border-top: 3px solid transparent;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.pillar-card:hover {
  box-shadow: 0 8px 25px rgba(0,0,0,0.07);
  transform: translateY(-3px);
}

.pillar-card:nth-child(1) { border-top-color: #4285f4; }
.pillar-card:nth-child(2) { border-top-color: #34a853; }
.pillar-card:nth-child(3) { border-top-color: #fbbc04; }
.pillar-card:nth-child(4) { border-top-color: #ea4335; }

.pillar-card .pillar-title {
  font-size: 0.9rem;
  font-weight: 700;
  margin: 0 0 0.4rem 0;
  color: #222;
}

.pillar-card:nth-child(1) .pillar-title { color: #4285f4; }
.pillar-card:nth-child(2) .pillar-title { color: #34a853; }
.pillar-card:nth-child(3) .pillar-title { color: #b8960c; }
.pillar-card:nth-child(4) .pillar-title { color: #ea4335; }

.pillar-card .pillar-desc {
  font-size: 0.8rem;
  color: #666;
  line-height: 1.6;
  margin: 0;
}

/* CTA Boxes */
.cta-box {
  padding: 1.2rem 1.5rem;
  border-radius: 12px;
  margin-bottom: 1rem;
  font-size: 0.9rem;
  line-height: 1.7;
}

.cta-box.recruit {
  background: linear-gradient(135deg, #fff5f5 0%, #fee2e2 100%);
  border: 1px solid #fecaca;
  color: #991b1b;
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

.cta-box.note {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  color: #555;
  font-size: 0.85rem;
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
</style>

<div class="hero-section">
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

<p class="section-label">Our research is organized around four core components of Agentic AI:</p>

<div class="pillars-grid">
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

<div class="cta-box recruit">
  <strong>Internship (상시 모집)</strong><br>
  관심 있는 학생은 아래 양식을 작성하고 저에게 이메일 보내주세요.<br>
  Internships are offered on a rolling basis. Interested students are encouraged to complete the form and email me.
  <a href="https://docs.google.com/forms/d/e/1FAIpQLSezVnp3eepLI4CTD3_lLABNwDtvFue6EqhXKq1zhK5zLW9ZsQ/viewform?usp=sharing&ouid=114425768257170495941" target="_blank">[Apply Here]</a>
</div>

<div class="cta-box note">
  We are not recruiting MS/PhD students for Fall 2026, as all positions have been filled. If you are interested in joining our lab for graduate studies, we strongly encourage you to apply for an internship first, as priority will be given to those with prior research experience in our group.
</div>

<div class="cta-box info">
  You can catch up on our recent research on <a href="https://www.youtube.com/channel/UCrEpnN7_2BmrHsPWns_Vx3Q" target="_blank" style="color: #166534; font-weight: 600;">our YouTube channel</a>.
</div>

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
</script>
