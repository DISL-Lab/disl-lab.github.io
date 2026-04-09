---
layout: page
permalink: /teaching/
title: Teaching
description: ""
nav: true
nav_order: 5
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

.post-header .post-description {
  font-size: 0.9rem;
  color: #777;
  font-weight: 400;
  letter-spacing: 0.02em;
}

.teaching-timeline {
  position: relative;
  padding-left: 2rem;
  margin-top: 1.5rem;
}

.teaching-timeline::before {
  content: '';
  position: absolute;
  left: 0.5rem;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(to bottom, #4285f4, #e0e0e0);
}

.teaching-semester {
  position: relative;
  margin-bottom: 2rem;
}

.teaching-semester::before {
  content: '';
  position: absolute;
  left: -1.75rem;
  top: 0.45rem;
  width: 10px;
  height: 10px;
  border-radius: 50%;
  background: #4285f4;
  border: 2px solid #fff;
  box-shadow: 0 0 0 2px #4285f4;
}

.semester-label {
  font-size: 0.78rem;
  font-weight: 600;
  color: #4285f4;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 0.3rem;
}

.course-card {
  display: inline-flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.8rem 1.2rem;
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 10px;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.course-card:hover {
  box-shadow: 0 6px 20px rgba(0,0,0,0.07);
  border-color: #e0e0e0;
  transform: translateY(-2px);
}

.course-code {
  font-size: 0.8rem;
  font-weight: 700;
  color: #fff;
  background: #4285f4;
  padding: 0.2rem 0.6rem;
  border-radius: 6px;
  white-space: nowrap;
}

.course-name {
  font-size: 0.9rem;
  font-weight: 500;
  color: #333;
}

.semester-current::before {
  background: #34a853;
  box-shadow: 0 0 0 2px #34a853, 0 0 8px rgba(52,168,83,0.4);
}

@media (max-width: 768px) {
  .course-card {
    display: flex;
    width: 100%;
  }
}
</style>

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%); border-radius: 12px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #e0e7ef;">
  <p style="font-size: 0.95rem; color: #444; line-height: 1.7; margin: 0;">
    If it has <span style="background-color: #fff8e1; padding: 0.1rem 0.4rem; border-radius: 3px; font-weight: 600;">Data</span> in the course title at KAIST, there's a good chance I'm teaching it.
  </p>
</div>

<div class="teaching-timeline">

  <div class="teaching-semester semester-current">
    <div class="semester-label">2026 Spring</div>
    <div class="course-card">
      <span class="course-code">DS801</span>
      <span class="course-name">Programming for Data Science</span>
    </div>
  </div>

  <div class="teaching-semester">
    <div class="semester-label">2025 Fall</div>
    <div class="course-card">
      <span class="course-code">DS801</span>
      <span class="course-name">Data Engineering for Big Data Analytics</span>
    </div>
  </div>

  <div class="teaching-semester">
    <div class="semester-label">2025 Spring</div>
    <div class="course-card">
      <span class="course-code">IE260</span>
      <span class="course-name">Data Structure and Analysis</span>
    </div>
  </div>

  <div class="teaching-semester">
    <div class="semester-label">2024 Fall</div>
    <div class="course-card">
      <span class="course-code">IE261</span>
      <span class="course-name">Introduction to Data Science for IE</span>
    </div>
  </div>

  <div class="teaching-semester">
    <div class="semester-label">2024 Spring</div>
    <div class="course-card">
      <span class="course-code">DS801</span>
      <span class="course-name">Data Engineering for Big Data Analytics</span>
    </div>
  </div>

</div>
