---
layout: page
permalink: /Lab_Project/
title: Projects
description: 
nav: true
nav_order: 3
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

.project-block {
  display: flex;
  flex-direction: row;
  align-items: flex-start;
  gap: 1.5rem;
  margin-bottom: 0.5rem;
  flex-wrap: wrap;
  padding: 1.2rem;
  border-radius: 12px;
  background: #fff;
  border: 1px solid #f0f0f0;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.project-block:hover {
  box-shadow: 0 8px 25px rgba(0,0,0,0.08), 0 2px 10px rgba(0,0,0,0.04);
  border-color: #e0e0e0;
  transform: translateY(-2px);
}

.project-block .img-col {
  flex: 1 1 35%;
  max-width: 280px;
  overflow: hidden;
  border-radius: 8px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.project-block .text-col {
  flex: 1 1 60%;
}

.project-block img {
  width: 100%;
  height: auto;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  transition: transform 0.4s ease;
  object-fit: contain;
}

.project-block:hover img {
  transform: scale(1.03);
}

.project-meta {
  font-size: 0.75rem;
  font-family: 'Roboto', monospace;
  color: #555;
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  align-items: center;
  margin-top: 0.3rem;
}

.project-meta .meta-item {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
}

.project-meta .meta-divider {
  color: #ccc;
}

.section-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #333;
  border-left: 4px solid #4285f4;
  padding-left: 0.8rem;
  margin-top: 2.5rem;
  margin-bottom: 1rem;
}

.role-badge {
  display: inline-block;
  font-size: 0.7rem;
  font-weight: 600;
  padding: 0.15rem 0.5rem;
  border-radius: 4px;
  margin-left: 0.3rem;
}

.role-pi {
  background: #e8f0fe;
  color: #1a73e8;
}

.role-copi {
  background: #fef7e0;
  color: #e8a817;
}

.role-collab {
  background: #e6f4ea;
  color: #137333;
}

/* 모바일: 이미지 위, 텍스트 아래 */
@media (max-width: 768px) {
  .project-block {
    flex-direction: column;
    padding: 0.8rem;
  }

  .project-block .img-col,
  .project-block .text-col {
    flex: 1 1 100%;
    max-width: 100%;
  }
}
</style>

<div style="background: linear-gradient(135deg, #f8f9fa 0%, #e8f0fe 100%); border-radius: 12px; padding: 1.5rem 2rem; margin-bottom: 2rem; border: 1px solid #e0e7ef;">
  <p style="font-size: 0.95rem; color: #444; line-height: 1.7; margin: 0;">
    Here are our current on-going and completed research projects.
  </p>
</div>

<h4 class="section-title">National Research Projects</h4>
<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/nrf-logo.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      고품질 데이터 및 자동 품질 평가를 통한 언어 모델 신뢰성 향상 시스템 (A System for Enhancing Language Model Reliability with High-Quality Data and Automated Quality Assessment)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to construct benchmark datasets and develop an automated evaluation system for the reliable assessment of AI-generated text. Ultimately, it seeks to devise methodologies that reduce hallucinations and biases in generative language models while enhancing completeness and conciseness.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2024.04 – 2027.03 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 600M &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-pi">Principal Investigator</span>
    </p>
  </div>
</div>


<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/iitp-logo.png" alt="Project 2">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      도메인 특화 자동 가치 연계 평가를 통한 AI 모델 신뢰성 향상 (Enhancing AI Model Reliability Through Domain-Specific Automated Value Alignment Assessment)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project, through a Korea-Canada international joint research collaboration (KAIST-GIST-UBC), aims to significantly enhance the reliability of AI models by constructing expert-reviewed, high-quality, value-aligned benchmark datasets specialized in language, mathematics, and medicine, and by developing core technologies for high-performance automated value alignment evaluation.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2024.09 – 2027.08 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 1.5B &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-pi">Principal Investigator</span>
    </p>
  </div>
</div>


<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/iitp-logo.png" alt="Project 2">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      AI가 그려내는 화합의 세계: 공정성과 투명성을 갖춘 갈등 중재용 멀티모달 에이전틱 플랫폼 (AI’s Vision of Harmony: A Fair and Transparent Multimodal Agentic Platform for Conflict Mediation)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to realize a high-performance Agentic AI conflict mediation platform that ensures fairness, transparency, and real-time responsiveness. By integrating multilingual, multicultural contexts with multimodal signals across text, speech, and vision, the research team pursues four core goals:  constructing real-world multimodal mediation datasets, developing real-time conflict and emotion analysis technologies, building personalized and fair interactive mediation mechanisms, and advancing explainable multimodal interpretation techniques for Agentic AI.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.10 – 2028.09 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 1.6B &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-copi">Co-Principal Investigator</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/nrf-logo.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      AI Co-Scientist 실현을 위한 지능형 Survey 에이전트 (Intelligent Survey Agents toward AI Co-Scientists)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to develop core technologies for an AI co-scientist that enables scalable, automated understanding and synthesis of scientific literature, supporting systematic knowledge discovery, structured organization of research landscapes, and continuous adaptation to evolving research trends.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2026.04 – 2027.03 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 170M &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-pi">Principal Investigator</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/kisti-logo.png" alt="Project 4">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      다중문서 분석 및 생성을 위한 RAG 기술 연구 (Research on RAG for Multi-Document Analysis and Generation)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to develop core technologies for a high-efficiency, high-reliability AI agent that supports automated research by efficiently exploring and structuring large-scale scientific and technical literature, and enabling trustworthy knowledge generation based on multiple documents. To this end, we aim to integratively implement citation network-based precise retrieval, multi-document context expansion with efficient inference, and key information-centric summarization with consistency and factuality verification.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2026.04 – 2026.11 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 180M &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-collab">Collaborating Investigator</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/icon_upstage.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      독자 파운데이션 모델 (with Upstage AI Consortium) 
    </h3>    
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      The Ministry of Science and ICT, together with NIPA, NIA, and IITP, is launching the “Independent AI Foundation Model” project to select capable domestic companies for developing globally impactful homegrown AI foundation models. <br><br>Details are confidential.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2026.03 – &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-collab">Collaborating Researcher</span>
    </p>
  </div>
</div>

<h4 class="section-title">Industry Research Projects</h4>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/qualcom-logo.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      개인화 비디오 에이전트 (Personalized Video Agent)
    </h3>    
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project is supported by Qualcomm Inc. The project details are confidencial.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.12 – 2026.12 (1st Round) &nbsp;&nbsp; |&nbsp;&nbsp; Funding: US $50,000 |&nbsp;&nbsp; <span class="role-badge role-pi">Principal Researcher</span>
    </p>
  </div>
</div>


<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/logo_gs.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      리테일 특화 RAG 프레임워크 (Retrieval-augmented Generation for Retail)
    </h3>    
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project is supported by GS Retail (in GS Holdings Corp.). The project details are confidencial.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2026.01 – 2026.05 &nbsp;&nbsp; |&nbsp;&nbsp; Funding: KRW 50M |&nbsp;&nbsp; <span class="role-badge role-pi">Principal Researcher</span>
    </p>
  </div>
</div>

<h4 class="section-title">Completed Projects</h4>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/kisti-logo.png" alt="Project 4">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      과학기술정보 특화 LLM을 위한 RAG 지원 데이터 구축 (RAG-Supported Data Building for Scientific Information Specialized LLMs)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to develop data construction algorithms that effectively support Retrieval-Augmented Generation (RAG) systems specialized for science and technology–focused large language models (LLMs). RAG enhances the accuracy and reliability of generative AI by incorporating information retrieved from external sources, and has recently gained significant attention as a key technique for improving model trustworthiness.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2024.06 – 2024.12 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 80M &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-collab">Collaborating Investigator</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/kisti-logo.png" alt="Project 3">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      과학기술정보에 대한 RAG 시스템의 출력 품질 향상 기술 연구 (Improving the Output Quality of the Scientific Information Specialized RAG System)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      Retrieval-Augmented Generation (RAG) is effective in improving the response accuracy of large language models (LLMs) and reducing hallucinations. However, existing approaches may not be optimal for the science and technology domain. This project aims to identify the unique requirements of domain-specific RAG for scientific and technical information, and to enhance the accuracy and reliability of RAG systems in this domain by developing optimized retrieval strategies, generation techniques, and evaluation metrics.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.06 – 2025.12 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 180M &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-collab">Collaborating Investigator</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/etri-logo.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      VLM 기반 PDF 문서 이해 및 도로 노선 좌표 자동화 기술 개발 (Development of VLM-based PDF Document Understanding and Automated Road Alignment Coordinate Extraction Technology)
    </h3>    
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project aims to build an intelligent system that can automatically recognize diverse information contained in road-related planning and design documents (PDFs), including map images, tables, and structured text—and use it to answer user queries. In particular, it seeks to implement a system capable of efficiently understanding and analyzing complex documents that combine images and text, by leveraging recent advances in multimodal artificial intelligence based on Visual Language Models (VLMs).
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.09 – 2025.11 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 51M &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-pi">Principal Investigator</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/ict-logo3.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      네이버 클라우드 컨소시엄: 옴니 파운데이션 모델 (Omni Foundation Model) 
    </h3>    
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      The Ministry of Science and ICT, together with NIPA, NIA, and IITP, is launching the “Independent AI Foundation Model” project to select capable domestic companies for developing globally impactful homegrown AI foundation models. <br><br>Details are confidential.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.08 – 2025.12 (1st Round) &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-collab">Collaborating Researcher</span>
    </p>
  </div>
</div>

<div class="project-block">
  <div class="img-col">
    <img src="/assets/img/iitp-logo.png" alt="Project 1">
  </div>
  <div class="text-col">
    <h3 style="font-size: 1.1rem; margin-bottom: 0.5rem;">
      튜링 테스트 그 너머: 확장하고 적응하는 인간 수준 게임 플레잉 에이전트 연구 (Beyond the Turing Test: Human-Level Game-Playing Agents with Generalization and Adaptation)
    </h3>
    <p style="font-size: 0.8rem; margin-bottom: 0.5rem;">
      This project develops a human-level game-playing agent, grounded in AGI’s core principles of adaptation and expansion, capable of competing and cooperating with humans in any game environment. The agent will autonomously design learning curricula, acquire knowledge without forgetting, model game causality, and adapt rapidly via language instructions. The resulting technology will be deployed as an API for commercial games, enhancing the competitiveness of Korea’s gaming industry.
    </p>
    <p style="font-size: 0.75rem; font-family: 'Roboto', monospace; color: #555;">
      Duration: 2025.08 – 2025.12 &nbsp;&nbsp;|&nbsp;&nbsp; Funding: KRW 4.03B &nbsp;&nbsp;|&nbsp;&nbsp; <span class="role-badge role-copi">Co-Principal Investigator</span>
    </p>
  </div>
</div>