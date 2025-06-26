---
layout: page
permalink: /Photo/
title: Photo
description: Explore memorable moments from our lab.
nav: true
nav_order: 7
---

<style>
.photo-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1rem;
}

.photo-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  text-align: center;
  padding: 0.5rem;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.photo-card img {
  width: 100%;
  height: auto;
  border-bottom: 1px solid #ddd;
}

.photo-card .caption {
  font-weight: bold;
  margin-top: 0.5rem;
}

.photo-card .sub-caption {
  font-size: 0.9rem;
  color: #555;
}
</style>

<div class="photo-grid">
  <div class="photo-card">
    <img src="/assets/images/your_photo1.jpg" alt="Hwanjun Song">
    <div class="sub-caption">Assistant Professor<br>Lab Director</div>
  </div>
  <div class="photo-card">
    <img src="/assets/images/your_photo2.jpg" alt="Sun-Min Jeong">
    <div class="sub-caption">Administrative Staff<br>Spring 2025~</div>
  </div>
  <!-- 필요에 따라 더 추가 -->
</div>