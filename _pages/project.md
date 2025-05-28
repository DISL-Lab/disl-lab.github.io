---
layout: page
permalink: /Lab_Project/
title: Projects
description: 
nav: true
nav_order: 3
---

<style>
.project-block {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 1.5rem;
  margin-bottom: 2rem;
  flex-wrap: wrap;
}

.project-block .img-col {
  flex: 1 1 35%;
  max-width: 300px;
}

.project-block .text-col {
  flex: 1 1 60%;
}

.project-block img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

/* 모바일: 이미지 위, 텍스트 아래 */
@media (max-width: 768px) {
  .project-block {
    flex-direction: column;
  }

  .project-block .img-col,
  .project-block .text-col {
    flex: 1 1 100%;
    max-width: 100%;
  }
}
</style>

### Ongoing research projects 

Here are our current ongoing research projects, mainly focusing on (1) Human-AI Alignment; (2) Collaborative Intelligence; (3) Data Quality and Robustness; and (4) Automated Evaluation.

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/nrf-logo.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      고품질 데이터 및 자동 품질 평가를 통한 언어 모델 신뢰성 향상 시스템  
      <br>(A System for Enhancing Language Model Reliability with High-Quality Data and Automated Quality Assessment)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to construct benchmark datasets and develop an automated evaluation system for the reliable assessment of AI-generated text. Ultimately, it seeks to devise methodologies that reduce hallucinations and biases in generative language models while enhancing completeness and conciseness.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2024.04 – 2027.03 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 600M
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/iitp-logo.png" alt="Project 2">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      도메인 특화 자동 가치 연계 평가를 통한 AI 모델 신뢰성 향상  
      <br>(Enhancing AI Model Reliability Through Domain-Specific Automated Value Alignment Assessment)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project, through a Korea-Canada international joint research collaboration (KAIST-GIST-UBC), aims to significantly enhance the reliability of AI models by constructing expert-reviewed, high-quality, value-aligned benchmark datasets specialized in language, mathematics, and medicine, and by developing core technologies for high-performance automated value alignment evaluation.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2024.09 – 2027.08 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 1.5B
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/kisti-logo.png" alt="Project 3">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      과학기술정보에 대한 RAG 시스템의 출력 품질 향상 기술 연구  
      <br>(Improving the Output Quality of the Scientific Information Specialized RAG System)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      Retrieval-Augmented Generation (RAG) is effective in improving the response accuracy of large language models (LLMs) and reducing hallucinations. However, existing approaches may not be optimal for the science and technology domain. This project aims to identify the unique requirements of domain-specific RAG for scientific and technical information, and to enhance the accuracy and reliability of RAG systems in this domain by developing optimized retrieval strategies, generation techniques, and evaluation metrics.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.06 – 2025.12 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 180M
    </p>
  </div>
</div>

### Completed research projects 

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/kisti-logo.png" alt="Project 4">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      과학기술정보 특화 LLM을 위한 RAG 지원 데이터 구축  
      <br>(RAG-Supported Data Building for Scientific Information Specialized LLMs)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to develop data construction algorithms that effectively support Retrieval-Augmented Generation (RAG) systems specialized for science and technology–focused large language models (LLMs). RAG enhances the accuracy and reliability of generative AI by incorporating information retrieved from external sources, and has recently gained significant attention as a key technique for improving model trustworthiness.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2024.06 – 2024.12 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 80M
    </p>
  </div>
</div>
