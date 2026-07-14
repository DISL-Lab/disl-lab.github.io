---
layout: page
title: Members
permalink: /projects/
description: ""
nav: true
nav_order: 1
display_categories: 
horizontal: false
---

{% capture members_stats %}
<span class="ph-stat s3"><span class="num">1</span> Faculty</span>
<span class="ph-stat s2"><span class="num">1</span> Postdoc</span>
<span class="ph-stat s1"><span class="num">12</span> Graduate Students</span>
<span class="ph-stat s4"><span class="num">7</span> Research Interns</span>
<span class="ph-stat s5"><span class="num">3</span> Industry Internships</span>
{% endcapture %}
{% include page_hero.html
   eyebrow="Our Team"
   title="Meet the People at DISLab"
   subtitle="A growing team of researchers building trustworthy, data-centric Agentic AI — from foundational reasoning and memory to perception and modeling. We collaborate across KAIST and with leading industry labs around the world."
   stats=members_stats
   orb_a="#4285f4"
   orb_b="#34a853"
   eyebrow_color="#4285f4" %}

<style>
.member-section-title {
  font-size: 1.05rem;
  font-weight: 600;
  color: #555;
  letter-spacing: 0.03em;
  margin-top: 2.5rem;
  margin-bottom: 1rem;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%);
  border-radius: 8px;
  border: none;
  text-align: center;
}

.member-section-title .count {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 600;
  color: #4285f4;
  background: #e8f0fe;
  padding: 0.1rem 0.5rem;
  border-radius: 10px;
  margin-left: 0.5rem;
  vertical-align: middle;
}

.member-grid {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 1.2rem;
  margin-bottom: 1.5rem;
}

.member-card {
  width: 170px;
}

.member-card {
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 16px;
  overflow: hidden;
  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1);
  text-align: center;
  position: relative;
}

.member-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: linear-gradient(90deg, #4285f4, #34a853, #fbbc04, #ea4335);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.member-card:hover::before {
  opacity: 1;
}

.member-card:hover {
  box-shadow: 0 12px 30px rgba(0,0,0,0.1), 0 4px 12px rgba(0,0,0,0.05);
  border-color: transparent;
  transform: translateY(-5px);
}

.member-card .img-wrapper {
  width: 100%;
  padding: 1.2rem 1.2rem 0;
  display: flex;
  justify-content: center;
}

.member-card .img-wrapper img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  border: 3px solid #f0f0f0;
  transition: all 0.4s ease;
}

.member-card:hover .img-wrapper img {
  transform: scale(1.06);
  border-color: #4285f4;
  box-shadow: 0 4px 15px rgba(66,133,244,0.2);
}

.member-card .info {
  padding: 0.8rem 0.8rem 1rem;
}

.member-card .name {
  font-size: 0.92rem;
  font-weight: 600;
  color: #222;
  margin: 0;
}

.member-card .role {
  font-size: 0.72rem;
  color: #666;
  margin: 0.2rem 0 0 0;
  line-height: 1.4;
}

.member-card .note {
  font-size: 0.65rem;
  color: #999;
  margin: 0.15rem 0 0 0;
  font-style: italic;
}

/* Lead Student */
.member-card.lead {
  border: 2px solid #4285f4;
  background: linear-gradient(135deg, #fff 0%, #f0f4ff 100%);
}

.member-card.lead .img-wrapper img {
  border-color: #4285f4;
}

.member-card.lead .name::after {
  content: 'Lead Student';
  display: inline-block;
  font-size: 0.55rem;
  font-weight: 600;
  color: #fff;
  background: #4285f4;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  margin-left: 0.4rem;
  vertical-align: middle;
}

/* Lab Manager */
.member-card.manager {
  border: 2px solid #34a853;
  background: linear-gradient(135deg, #fff 0%, #f0fff4 100%);
}

.member-card.manager .img-wrapper img {
  border-color: #34a853;
}

.member-card.manager:hover .img-wrapper img {
  border-color: #34a853;
  box-shadow: 0 4px 15px rgba(52,168,83,0.25);
}

.member-card.manager .name::after {
  content: 'Lab Manager';
  display: inline-block;
  font-size: 0.55rem;
  font-weight: 600;
  color: #fff;
  background: #34a853;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  margin-left: 0.4rem;
  vertical-align: middle;
}

/* Director */
.member-card.director {
  border: 2px solid #e8a817;
  background: linear-gradient(135deg, #fff 0%, #fffbf0 100%);
}

.member-card.director .img-wrapper img {
  border-color: #e8a817;
}

.member-card.director:hover .img-wrapper img {
  border-color: #e8a817;
  box-shadow: 0 4px 15px rgba(232,168,23,0.25);
}

.member-card.director .name::after {
  content: 'Director';
  display: inline-block;
  font-size: 0.55rem;
  font-weight: 600;
  color: #fff;
  background: #e8a817;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  margin-left: 0.4rem;
  vertical-align: middle;
}

/* Info list (Internship, Graduates) */
.info-list {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.7rem 1rem;
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 10px;
  transition: all 0.3s ease;
}

.info-item:hover {
  border-color: #e0e0e0;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  transform: translateX(4px);
}

.info-item .semester {
  font-size: 0.72rem;
  font-weight: 600;
  color: #fff;
  background: #4285f4;
  padding: 0.15rem 0.5rem;
  border-radius: 5px;
  white-space: nowrap;
}

.info-item .semester.intern-badge {
  background: #34a853;
}

.info-item .detail {
  font-size: 0.85rem;
  color: #444;
}

.info-item .detail strong {
  color: #222;
}

.info-item .company {
  font-size: 0.75rem;
  color: #888;
  margin-left: auto;
  font-style: italic;
}

@media (max-width: 768px) {
  .member-grid {
    grid-template-columns: repeat(auto-fill, minmax(140px, 1fr));
    gap: 0.8rem;
  }
  .member-card .img-wrapper img {
    width: 90px;
    height: 90px;
  }
  .info-item {
    flex-direction: column;
    align-items: flex-start;
    gap: 0.3rem;
  }
  .info-item .company {
    margin-left: 0;
  }
}
</style>


<h3 class="member-section-title">Lab Director & Staff</h3>

<div class="member-grid">
  <div class="member-card director">
    <div class="img-wrapper">
      <img src="/assets/img/bio-hwanjun.png" alt="Hwanjun Song">
    </div>
    <div class="info">
      <p class="name">Hwanjun Song</p>
      <p class="role">Ewon Assistant Professor</p>
      <p class="role">Lab Director</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-sunmin.png" alt="Sun-Min Jeong">
    </div>
    <div class="info">
      <p class="name">Sun-Min Jeong</p>
      <p class="role">Administrative Staff</p>
      <p class="role">Spring 2025~</p>
    </div>
  </div>
</div>


<h3 class="member-section-title">Lab Manager (Postdoctoral Researcher)</h3>

<div class="member-grid">
  <div class="member-card manager">
    <div class="img-wrapper">
      <img src="/assets/img/bio_jeesu_jung.png" alt="Jeesu Jung">
    </div>
    <div class="info">
      <p class="name">Jeesu Jung</p>
      <p class="role">March 2026~</p>
    </div>
  </div>
</div>


<h3 class="member-section-title">Senior Researchers (PhD Students) <span class="count">6</span></h3>

<div class="member-grid">
  <div class="member-card lead">
    <div class="img-wrapper">
      <img src="/assets/img/bio_hyangsuk.jpeg" alt="Hyangsuk Min">
    </div>
    <div class="info">
      <p class="name">Hyangsuk Min</p>
      <p class="role">Full Time, Fall 2024~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-jeonghwan.png" alt="Jeonghwan Choi">
    </div>
    <div class="info">
      <p class="name">Jeonghwan Choi</p>
      <p class="role">Full Time, Spring 2025~</p>
      <p class="role">MS-PhD Integrated</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-yuho.png" alt="Yuho Lee">
    </div>
    <div class="info">
      <p class="name">Yuho Lee</p>
      <p class="role">Full Time, Fall 2025~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-taewon.png" alt="Taewon Yun">
    </div>
    <div class="info">
      <p class="name">Taewon Yun</p>
      <p class="role">Full Time, Fall 2025~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-jihwanoh.png" alt="Jihwan Oh">
    </div>
    <div class="info">
      <p class="name">Jihwan Oh</p>
      <p class="role">Full Time, Spring 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_jisu.png" alt="Jisu Shin">
    </div>
    <div class="info">
      <p class="name">Jisu Shin</p>
      <p class="role">Full Time, Spring 2026~</p>
    </div>
  </div>
</div>


<h3 class="member-section-title">Junior Researchers (MS Students) <span class="count">6</span></h3>

<div class="member-grid">
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-jiaqi.png" alt="Jiaqi Deng">
    </div>
    <div class="info">
      <p class="name">Jiaqi Deng</p>
      <p class="role">Full Time, Fall 2024~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-minjeong.png" alt="Minjeong Ban">
    </div>
    <div class="info">
      <p class="name">Minjeong Ban</p>
      <p class="role">Full Time, Spring 2025~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-kibeom.png" alt="Kibum Kim">
    </div>
    <div class="info">
      <p class="name">Kibum Kim</p>
      <p class="role">Hankook Tire, Spring 2025~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_mingyu_choi.jpg" alt="Mingyu Choi">
    </div>
    <div class="info">
      <p class="name">Mingyu Choi</p>
      <p class="role">Full Time, Spring 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_gyeonghun_sun.jpg" alt="Gyeonghun Sun">
    </div>
    <div class="info">
      <p class="name">Gyeonghun Sun</p>
      <p class="role">Full Time, Spring 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-seonghwan.jpg" alt="Seunghwan Bang">
    </div>
    <div class="info">
      <p class="name">Seunghwan Bang</p>
      <p class="role">Full Time, September 2026~</p>
    </div>
  </div>
    <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_jibin.jpg" alt="Jibin Hwang">
    </div>
    <div class="info">
      <p class="name">Jibin Hwang</p>
      <p class="role">Full Time, September 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_yeeun_choi.jpeg" alt="Yeeun Choi">
    </div>
    <div class="info">
      <p class="name">Yeeun Choi</p>
      <p class="role">Full Time, September 2026~</p>
    </div>
  </div>
</div>


<h3 class="member-section-title">Jointly Supervised Students <span class="count">2</span></h3>

<div class="member-grid">
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-jihwan.png" alt="Jihwan Bang">
    </div>
    <div class="info">
      <p class="name">Jihwan Bang</p>
      <p class="role">Qualcomm, Spring 2023~</p>
      <p class="role">Co-advised by Prof. Jae-Gil Lee</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio-yujin.png" alt="Yujin Kim">
    </div>
    <div class="info">
      <p class="name">Yujin Kim</p>
      <p class="role">Full Time, Spring 2025~</p>
      <p class="role">Co-advised by Se-Young Yun</p>
    </div>
  </div>
</div>


<h3 class="member-section-title">Research Interns <span class="count">7</span></h3>

<div class="member-grid">
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_changhwan.jpg" alt="Hwan Chang">
    </div>
    <div class="info">
      <p class="name">Hwan Chang</p>
      <p class="role">MS Intern, July 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_jisoo_kim.jpg" alt="Jisoo Kim">
    </div>
    <div class="info">
      <p class="name">Jisoo Kim</p>
      <p class="role">BS Intern, July 2025~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_hyeonseng.jpeg" alt="Hyeonseong Park">
    </div>
    <div class="info">
      <p class="name">Hyeonseong Park</p>
      <p class="role">BS Intern, January 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_juseon_do.png" alt="Juseon Do">
    </div>
    <div class="info">
      <p class="name">Juseon Do</p>
      <p class="role">BS Intern, March 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_hayoon.jpg" alt="Hayoon Park">
    </div>
    <div class="info">
      <p class="name">Hayoon Park</p>
      <p class="role">BS Intern, March 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_byeongjun.jpg" alt="Byeongjun Joung">
    </div>
    <div class="info">
      <p class="name">Byeongjun Joung</p>
      <p class="role">BS Intern, July 2026~</p>
    </div>
  </div>
  <div class="member-card">
    <div class="img-wrapper">
      <img src="/assets/img/bio_chanjoong.jpg" alt="Chanjoong Kim">
    </div>
    <div class="info">
      <p class="name">Chanjoong Kim</p>
      <p class="role">BS Intern, July 2026~</p>
    </div>
  </div>
</div>


<h3 class="member-section-title">Internship</h3>

<div class="info-list">
  <div class="info-item">
    <span class="semester intern-badge">Summer 2025</span>
    <span class="detail"><strong>Yuho Lee</strong></span>
    <span class="company">Amazon Web Services, Bedrock — Santa Clara, US</span>
  </div>
  <div class="info-item">
    <span class="semester intern-badge">Summer 2026</span>
    <span class="detail"><strong>Yujin Kim</strong></span>
    <span class="company">NVIDIA Corp. — Santa Clara, US</span>
  </div>
  <div class="info-item">
    <span class="semester intern-badge">Summer 2026</span>
    <span class="detail"><strong>Taewon Yun</strong></span>
    <span class="company">Amazon Web Services, Agentic AI — New York, US</span>
  </div>
</div>


<h3 class="member-section-title">Graduates</h3>

<div class="info-list">
  <div class="info-item">
    <span class="semester">Spring 2025</span>
    <span class="detail"><strong>Jeonghwan Choi</strong> — PhD Program at KAIST</span>
  </div>
  <div class="info-item">
    <span class="semester">Fall 2025</span>
    <span class="detail"><strong>Yuho Lee</strong> — PhD Program at KAIST</span>
  </div>
  <div class="info-item">
    <span class="semester">Fall 2025</span>
    <span class="detail"><strong>Taewon Yun</strong> — PhD Program at KAIST</span>
  </div>
  <div class="info-item">
    <span class="semester">Fall 2025</span>
    <span class="detail"><strong>Jihwan Oh</strong> — PhD Program at KAIST</span>
  </div>
  <div class="info-item">
    <span class="semester">Fall 2025</span>
    <span class="detail"><strong>Heeyoen Kim</strong></span>
  </div>
</div>
