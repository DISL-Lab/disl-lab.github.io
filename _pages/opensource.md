---
layout: page
permalink: /opensource/
title: Opensource
description: ""
nav: true
nav_order: 4
---

{% capture os_stats %}
{% endcapture %}
{% include page_hero.html
   eyebrow="Open Source"
   title="Tools, Datasets & Benchmarks"
   subtitle="We release the artifacts behind our research — codebases, datasets, and benchmarks — so the community can reproduce, build on, and stress-test what we publish. Everything below is freely available on GitHub and Hugging Face."
   stats=os_stats
   orb_a="#9333ea"
   orb_b="#0891b2"
   eyebrow_color="#9333ea" %}

<style>
.os-section-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #333;
  border-left: 4px solid #4285f4;
  padding-left: 0.8rem;
  margin-top: 2.5rem;
  margin-bottom: 1rem;
}

.os-subsection-title {
  font-size: 1rem;
  font-weight: 600;
  color: #555;
  margin-top: 1.5rem;
  margin-bottom: 0.8rem;
  padding-left: 0.5rem;
}

.os-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
  gap: 0.8rem;
  margin-bottom: 1rem;
}

.os-card {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 1rem 1.2rem;
  background: #fff;
  border: 1px solid #f0f0f0;
  border-radius: 10px;
  transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
  text-decoration: none;
  color: inherit;
}

.os-card:hover {
  box-shadow: 0 6px 20px rgba(0,0,0,0.07), 0 2px 8px rgba(0,0,0,0.04);
  border-color: #e0e0e0;
  transform: translateY(-2px);
  text-decoration: none;
  color: inherit;
}

.os-card-icon {
  font-size: 1.6rem;
  flex-shrink: 0;
  width: 40px;
  text-align: center;
}

.os-card-body {
  flex: 1;
  min-width: 0;
}

.os-card-title {
  font-size: 0.88rem;
  font-weight: 600;
  color: #222;
  margin: 0;
  line-height: 1.3;
}

.os-card-desc {
  font-size: 0.78rem;
  color: #888;
  margin: 0.2rem 0 0 0;
}

.os-card-arrow {
  color: #bbb;
  font-size: 0.9rem;
  transition: transform 0.2s ease;
  flex-shrink: 0;
}

.os-card:hover .os-card-arrow {
  transform: translateX(3px);
  color: #4285f4;
}

.os-badge {
  display: inline-block;
  font-size: 0.65rem;
  font-weight: 600;
  padding: 0.1rem 0.4rem;
  border-radius: 4px;
  margin-left: 0.4rem;
  vertical-align: middle;
}

.badge-hf {
  background: #fff3cd;
  color: #856404;
}

.badge-gh {
  background: #e8e8e8;
  color: #333;
}

.badge-web {
  background: #e8f0fe;
  color: #1a73e8;
}

@media (max-width: 768px) {
  .os-grid {
    grid-template-columns: 1fr;
  }
}
</style>

<h3 class="os-section-title">Large Language Models</h3>

<div class="os-grid">
  <a class="os-card" href="https://huggingface.co/DISLab/SummLlama3.2-3B" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">SummLlama <span class="os-badge badge-hf">HuggingFace</span></p>
      <p class="os-card-desc">Faithful Summarization Model</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://huggingface.co/DISLab/Ext2Gen-8B-R2" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">Ext2Gen <span class="os-badge badge-hf">HuggingFace</span></p>
      <p class="os-card-desc">Robust Generation Model for RAG</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>
</div>


<h3 class="os-section-title">Benchmark Datasets</h3>

<div class="os-grid">
  <a class="os-card" href="https://github.com/disl-lab/unisumeval-v1.0" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">UniSumEval <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Benchmark Data for Text Summarization</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/amazon-science/tofueval" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">ToFuEval <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Hallucination Benchmark Data</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://dm.kaist.ac.kr/datasets/animal-10n/" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">ANIMAL-10N <span class="os-badge badge-web">Web</span></p>
      <p class="os-card-desc">Real-world Data with Noisy Labels</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>
</div>


<h3 class="os-section-title">Algorithms</h3>

<h4 class="os-subsection-title">Retrieval for RAG</h4>
<div class="os-grid">
  <a class="os-card" href="https://github.com/DISL-Lab/Word2Passage" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">Word2Passage <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Accurate Retrieval Method</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>
</div>

<h4 class="os-subsection-title">Transformers</h4>
<div class="os-grid">
  <a class="os-card" href="https://github.com/naver-ai/vidt" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">ViDT <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">A Fully Transformer-based Object Detector</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/raymin0223/fast_robust_early_exit" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">Fast Autoregressive Decoding <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Fast &amp; Robust Early Exit</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/amazon-science/discal" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">DisCal <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Calibrated Distillation</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/songhwanjun/MEDUSA" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">MEDUSA <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">RGB-D Transformer-based Object Detector</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>
</div>

<h4 class="os-subsection-title">Robust Deep Learning</h4>
<div class="os-grid">
  <a class="os-card" href="https://github.com/songhwanjun/Awesome-Noisy-Labels" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">Awesome Noisy Labels <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Curated List of Noisy Label Research</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/kaist-dmlab/SELFIE" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">SELFIE <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Robust Training against Noisy Labels</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/kaist-dmlab/Prune4Rel" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">Prune4Rel <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Robust Data Pruning</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/kaist-dmlab/MQNet" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">MQNet <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Open-set Active Learning</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/elvinkim/fedrn" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">FedRN <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Federated Learning with Noisy Labels</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>
</div>

<h4 class="os-subsection-title">Continual Learning</h4>
<div class="os-grid">
  <a class="os-card" href="https://github.com/naver-ai/dap-cl" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">DAP <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Instance-level Prompt-based CL with Transformers</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>

  <a class="os-card" href="https://github.com/yonseivnl/sdp" target="_blank">
    <div class="os-card-body">
      <p class="os-card-title">SDP <span class="os-badge badge-gh">GitHub</span></p>
      <p class="os-card-desc">Scheduled Data Prior for Continual Learning</p>
    </div>
    <div class="os-card-arrow">→</div>
  </a>
</div>
