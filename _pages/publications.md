---
layout: page
permalink: /publications/
title: Publications
description: We publish our research in high-impact conferences and journals within the field of Computer Science. We have collaborated top IT tech companies such as AWS AI Labs, Google Research, and NAVER AI Lab. <br>As of now, we published more than 40 CS top confernces in various domains, including NLP (EMNLP), CV (ICCV, CVPR), ML (NeurIPS, ICLR, ICML, AAAI), DM (KDD, CIKM, ICDM, WWW, SIGMOD). <br><br>Asterisk (*) denotes corresponding authors.

nav: true
nav_order: 2
---

<!-- _pages/publications.md -->

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} -q @*[selected=true]* %}

</div>

<h2>International Conferences and Journals</h2>

<div class="publications">

{% bibliography -f {{ site.scholar.bibliography }} %}

</div>
