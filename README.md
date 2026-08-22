<div align="center">

# Awesome Medical Reasoning

**Papers on reasoning in medical LLMs and MLLMs.**

医学大模型推理方向的论文列表

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
![Papers](https://img.shields.io/badge/papers-303-blue)
![Last commit](https://img.shields.io/github/last-commit/JXLiu-AI/Awesome-Medical-Reasoning)

</div>

---

**303** papers indexed (2023: 1 · 2024: 46 · 2025: 180 · 2026: 76) across 6 sections / 14 categories. 1052 more under consideration.

Last updated: 2026-08-22.

**Scope** — papers where reasoning itself is the contribution: the chain, the reward, the search, or the
evaluation of the chain. Medical LLMs reported only as end-task accuracy, and agent frameworks with no
reasoning mechanism, are out of scope. Entries with a note beneath them have been read and placed by hand;
the rest are categorized by keyword and should be treated as provisional.

## Contents

- [🏋️ Training-Time Methods](#training-time-methods--训练期方法) <sub>42</sub>
- [🧭 Test-Time Methods](#test-time-methods--测试期方法) <sub>54</sub>
- [🖼️ Multimodal Medical Reasoning](#multimodal-medical-reasoning--多模态医学推理) <sub>75</sub>
- [🩺 Agentic Diagnostic Reasoning](#agentic-diagnostic-reasoning--智能体式诊断推理) <sub>23</sub>
- [📊 Evaluation, Benchmarks & Trustworthiness](#evaluation-benchmarks--trustworthiness--评测基准与可信度) <sub>100</sub>
- [📚 Surveys & Position Papers](#surveys--position-papers--综述与立场文章) <sub>9</sub>

- [Related lists](#related-lists)
- [Contributing](#contributing)

---

## 🏋️ Training-Time Methods · 训练期方法

> Baking reasoning into the weights: SFT, CoT distillation, and RL.  
> <sub>把推理能力写进权重：监督微调、推理链蒸馏、强化学习。</sub>

### SFT & Reasoning-Chain Distillation · SFT 与推理链蒸馏 <sub>10</sub>

- [A Cost-Effective Multimodal LLM Reasoning Framework for Question Answering over Irregular Clinical Time Series](https://arxiv.org/abs/2607.25947) <sub>2026-07 · 1 citation</sub>
- [PowerOPD: Stabilizing On-Policy Distillation with Bounded Power Transformation](https://arxiv.org/abs/2606.17199) <sub>2026-06 · 3 citations</sub>
- [Stable On-Policy Distillation through Adaptive Target Reformulation](https://arxiv.org/abs/2601.07155) — **ACL** <sub>2026-01 · 35 citations</sub>
- [Knowledge Graph Augmented Large Language Models for Disease Prediction](https://arxiv.org/abs/2512.01210) — **AMIA Summits** <sub>2025-12 · 3 citations</sub>
- [Knowledge or Reasoning? A Close Look at How LLMs Think Across Domains](https://arxiv.org/abs/2506.02126) <sub>2025-06 · 14 citations</sub>
- [Beyond Distillation: Pushing the Limits of Medical LLM Reasoning with Minimalist Rule-Based RL](https://arxiv.org/abs/2505.17952) <sub>2025-05 · 33 citations</sub>
- [TrialMatchAI: An End-to-End AI-powered Clinical Trial Recommendation System to Streamline Patient-to-Trial Matching](https://arxiv.org/abs/2505.08508) — **Nature Communications** <sub>2025-05 · 10 citations</sub>
- [X-Reasoner: Towards Generalizable Reasoning Across Modalities and Domains](https://arxiv.org/abs/2505.03981) <sub>2025-05 · 30 citations</sub>
- [O1 Replication Journey -- Part 3: Inference-time Scaling for Medical Reasoning](https://arxiv.org/abs/2501.06458) <sub>2025-01 · 38 citations</sub>
- [MedThink: Explaining Medical Visual Question Answering via Multimodal Decision-Making Rationale](https://arxiv.org/abs/2404.12372) — **LREC-COLING 2024** <sub>2024-04</sub>
  <sub>Supervises Med-VQA with multimodal decision rationales, so the explanation and the answer share a source instead of being rationalized after the fact.</sub>

### RL with Verifiable Rewards (RLVR / GRPO) · 强化学习与可验证奖励（RLVR / GRPO） <sub>29</sub>

- [Reinforcement Learning for Evidence-Seeking Diagnostic Reasoning with Large Language Models](https://arxiv.org/abs/2607.02983) <sub>2026-07 · 1 citation</sub>
- [RLCSD: Reinforcement Learning with Contrastive On-Policy Self-Distillation](https://arxiv.org/abs/2606.11709) <sub>2026-06 · 15 citations</sub>
- [Healthcare AI GYM for Medical Agents](https://arxiv.org/abs/2605.02943) <sub>2026-05 · 4 citations</sub>
- [Generate, Filter, Control, Replay: A Comprehensive Survey of Rollout Strategies for LLM Reinforcement Learning](https://arxiv.org/abs/2605.02913) <sub>2026-04 · 6 citations</sub>
- [Beyond Accuracy: Evaluating Visual Grounding In Multimodal Medical Reasoning](https://arxiv.org/abs/2603.03437) <sub>2026-03 · 7 citations</sub>
- [Overconfident Errors Need Stronger Correction: Asymmetric Confidence Penalties for Reinforcement Learning](https://arxiv.org/abs/2602.21420) <sub>2026-02 · 7 citations</sub>
- [Beyond Outcome Verification: Verifiable Process Reward Models for Structured Reasoning](https://arxiv.org/abs/2601.17223) — **ACL** <sub>2026-01 · 11 citations</sub>
- [CURE-Med: Curriculum-Informed Reinforcement Learning for Multilingual Medical Reasoning](https://arxiv.org/abs/2601.13262) — **ACL** <sub>2026-01 · 8 citations</sub>
- [MedEyes: Learning Dynamic Visual Focus for Medical Progressive Diagnosis](https://arxiv.org/abs/2511.22018) — **AAAI** <sub>2025-11 · 34 citations</sub>
- [Exploiting Tree Structure for Credit Assignment in RL Training of LLMs](https://arxiv.org/abs/2509.18314) <sub>2025-09 · 24 citations</sub>
- [Reward Hacking Mitigation using Verifiable Composite Rewards](https://arxiv.org/abs/2509.15557) — **ACM BCB** <sub>2025-09 · 8 citations</sub>
- [Dream-Coder 7B: An Open Diffusion Language Model for Code](https://arxiv.org/abs/2509.01142) <sub>2025-09 · 71 citations</sub>
- [MedGR$^2$: Breaking the Data Barrier for Medical Reasoning via Generative Reward Learning](https://arxiv.org/abs/2508.20549) — **AAAI** <sub>2025-08 · 9 citations</sub>
- [MedResearcher-R1: Expert-Level Medical Deep Researcher via A Knowledge-Informed Trajectory Synthesis Framework](https://arxiv.org/abs/2508.14880) <sub>2025-08 · 21 citations</sub>
- [DocThinker: Explainable Multimodal Large Language Models with Rule-based Reinforcement Learning for Document Understanding](https://arxiv.org/abs/2508.08589) — **ICCV** <sub>2025-08 · 15 citations</sub>
- [MedVLThinker: Simple Baselines for Multimodal Medical Reasoning](https://arxiv.org/abs/2508.02669) <sub>2025-08 · 28 citations</sub>
- [CX-Mind: A Pioneering Multimodal Large Language Model for Interleaved Reasoning in Chest X-ray via Curriculum-Guided Reinforcement Learning](https://arxiv.org/abs/2508.03733) — **Information Fusion** <sub>2025-07 · 3 citations</sub>
- [Rubrics as Rewards: Reinforcement Learning Beyond Verifiable Domains](https://arxiv.org/abs/2507.17746) <sub>2025-07 · 268 citations</sub>
- [MedGround-R1: Advancing Medical Image Grounding via Spatial-Semantic Rewarded Group Relative Policy Optimization](https://arxiv.org/abs/2507.02994) — **MICCAI** <sub>2025-07 · 20 citations</sub>
- [GEMeX-RMCoT: An Enhanced Med-VQA Dataset for Region-Aware Multimodal Chain-of-Thought Reasoning](https://arxiv.org/abs/2506.17939) — **ACM MM** <sub>2025-06 · 5 citations</sub>
- [Doctor Approved: Generating Medically Accurate Skin Disease Images through AI-Expert Feedback](https://arxiv.org/abs/2506.12323) — **NeurIPS** <sub>2025-06 · 12 citations</sub>
- [QoQ-Med: Building Multimodal Clinical Foundation Models with Domain-Aware GRPO Training](https://arxiv.org/abs/2506.00711) — **NeurIPS** <sub>2025-05 · 42 citations</sub>
- [Training LLMs for EHR-Based Reasoning Tasks via Reinforcement Learning](https://arxiv.org/abs/2505.24105) <sub>2025-05 · 12 citations</sub>
- [Improving Medical Reasoning with Curriculum-Aware Reinforcement Learning](https://arxiv.org/abs/2505.19213) <sub>2025-05 · 17 citations</sub>
- [Patho-R1: A Multimodal Reinforcement Learning-Based Pathology Expert Reasoner](https://arxiv.org/abs/2505.11404) — **AAAI** <sub>2025-05 · 35 citations</sub>
- [GMAI-VL-R1: Harnessing Reinforcement Learning for Multimodal Medical Reasoning](https://arxiv.org/abs/2504.01886) <sub>2025-04 · 31 citations</sub>
- [Med-R1: Reinforcement Learning for Generalizable Medical Reasoning in Vision-Language Models](https://arxiv.org/abs/2503.13939) — **IEEE TMI** <sub>2025-03 · 146 citations</sub>
- [Med-RLVR: Emerging Medical Reasoning from a 3B base model via reinforcement Learning](https://arxiv.org/abs/2502.19655) <sub>2025-02 · 38 citations</sub>
- [HuatuoGPT-o1, Towards Medical Complex Reasoning with LLMs](https://arxiv.org/abs/2412.18925) <sub>2024-12 · 270 citations</sub>

### Process Rewards & Step-Level Supervision · 过程奖励与步骤级监督 <sub>3</sub>

- [Med-PRM: Medical Reasoning Models with Stepwise, Guideline-verified Process Rewards](https://arxiv.org/abs/2506.11474) — **EMNLP** <sub>2025-06 · 26 citations</sub>
- [ChestX-Reasoner: Advancing Radiology Foundation Models with Reasoning through Step-by-Step Verification](https://arxiv.org/abs/2504.20930) <sub>2025-04 · 33 citations</sub>
- [Bridging Stepwise Lab-Informed Pretraining and Knowledge-Guided Learning for Diagnostic Reasoning](https://arxiv.org/abs/2410.19955) — **IEEE JBHI** <sub>2024-10 · 4 citations</sub>

## 🧭 Test-Time Methods · 测试期方法

> No weight updates — think harder at inference: prompting structures, search and scaling, external knowledge.  
> <sub>不改权重，在推理时把答案想得更对：提示结构、搜索与扩展、外部知识。</sub>

### Prompting & Thought Structures · 提示与思维结构 <sub>30</sub>

- [HealthAgentBench: A Unified Benchmark Suite of Realistic Agentic Healthcare Environments for Challenging Frontier AI Agents](https://arxiv.org/abs/2606.31179) <sub>2026-06 · 6 citations</sub>
- [COTCAgent: Preventive Consultation via Probabilistic Chain-of-Thought Completion](https://arxiv.org/abs/2605.15016) <sub>2026-05 · 3 citations</sub>
- [MedSynapse-V: Bridging Visual Perception and Clinical Intuition via Latent Memory Evolution](https://arxiv.org/abs/2604.26283) <sub>2026-04 · 16 citations</sub>
- [TARSE: Test-Time Adaptation via Retrieval of Skills and Experience for Reasoning Agents](https://arxiv.org/abs/2603.01241) <sub>2026-03 · 5 citations</sub>
- [DEEPMED: Building a Medical DeepResearch Agent via Multi-hop Med-Search Data and Turn-Controlled Agentic Training & Inference](https://arxiv.org/abs/2601.18496) — **ACL** <sub>2026-01 · 5 citations</sub>
- [OpenTSLM: Time-Series Language Models for Reasoning over Multivariate Medical Text- and Time-Series Data](https://arxiv.org/abs/2510.02410) <sub>2025-10 · 22 citations</sub>
- [MuSLR: Multimodal Symbolic Logical Reasoning](https://arxiv.org/abs/2509.25851) — **NeurIPS** <sub>2025-09 · 4 citations</sub>
- [MedCoT-RAG: Causal Chain-of-Thought RAG for Medical Question Answering](https://arxiv.org/abs/2508.15849) — **BSN** <sub>2025-08 · 10 citations</sub>
- [Affective-ROPTester: Capability and Bias Analysis of LLMs in Predicting Retinopathy of Prematurity](https://arxiv.org/abs/2507.05816) — **IEEE TAFFC** <sub>2025-07 · 13 citations</sub>
- [Conformal Information Pursuit for Interactively Guiding Large Language Models](https://arxiv.org/abs/2507.03279) — **NeurIPS** <sub>2025-07 · 8 citations</sub>
- [VAP-Diffusion: Enriching Descriptions with MLLMs for Enhanced Medical Image Generation](https://arxiv.org/abs/2506.23641) — **MICCAI** <sub>2025-06 · 3 citations</sub>
- [PPMI: Privacy-Preserving LLM Interaction with Socratic Chain-of-Thought Reasoning and Homomorphically Encrypted Vector Databases](https://arxiv.org/abs/2506.17336) <sub>2025-06 · 10 citations</sub>
- [Instruction Tuning and CoT Prompting for Contextual Medical QA with LLMs](https://arxiv.org/abs/2506.12182) — **2025 International Conference on Arti…** <sub>2025-06 · 14 citations</sub>
- [MA-RAG: Multi-Agent Retrieval-Augmented Generation via Collaborative Chain-of-Thought Reasoning](https://arxiv.org/abs/2505.20096) <sub>2025-05 · 39 citations</sub>
- [Detecting PTSD in Clinical Interviews: A Comparative Analysis of NLP Methods and Large Language Models](https://arxiv.org/abs/2504.01216) — **PSB** <sub>2025-04 · 7 citations</sub>
- [AutoMedPrompt: A New Framework for Optimizing LLM Medical Prompts Using Textual Gradients](https://arxiv.org/abs/2502.15944) <sub>2025-02 · 14 citations</sub>
- [Enhancing Depression Detection with Chain-of-Thought Prompting: From Emotion to Reasoning Using Large Language Models](https://arxiv.org/abs/2502.05879) — **EMBC** <sub>2025-02 · 14 citations</sub>
- [Large Language Models with Temporal Reasoning for Longitudinal Clinical Summarization and Prediction](https://arxiv.org/abs/2501.18724) — **EMNLP** <sub>2025-01 · 17 citations</sub>
- [Layered Chain-of-Thought Prompting for Multi-Agent LLM Systems: A Comprehensive Approach to Explainable Large Language Models](https://arxiv.org/abs/2501.18645) <sub>2025-01 · 19 citations</sub>
- [Benchmarking Generative AI for Scoring Medical Student Interviews in Objective Structured Clinical Examinations (OSCEs)](https://arxiv.org/abs/2501.13957) — **AIED** <sub>2025-01 · 17 citations</sub>
- [MedCoT: Medical Chain of Thought via Hierarchical Expert](https://arxiv.org/abs/2412.13736) — **EMNLP 2024** <sub>2024-12</sub>
  <sub>Hierarchical experts generate and cross-verify the reasoning chain, rather than one model walking a single chain end to end.</sub>
- [Synthetic Data Generation with LLM for Improved Depression Prediction](https://arxiv.org/abs/2411.17672) <sub>2024-11 · 26 citations</sub>
- [From Medprompt to o1: Exploration of Run-Time Strategies for Medical Challenge Problems and Beyond](https://arxiv.org/abs/2411.03590) <sub>2024-11 · 36 citations</sub>
- [Large Language Models for Medical OSCE Assessment: A Novel Approach to Transcript Analysis](https://arxiv.org/abs/2410.12858) <sub>2024-10 · 11 citations</sub>
- [PASS:Test-Time Prompting to Adapt Styles and Semantic Shapes in Medical Image Segmentation](https://arxiv.org/abs/2410.01573) — **IEEE TMI** <sub>2024-10 · 13 citations</sub>
- [LLMs are not Zero-Shot Reasoners for Biomedical Information Extraction](https://arxiv.org/abs/2408.12249) — **Insights@NLP** <sub>2024-08 · 21 citations</sub>
- [IgnitionInnovators at "Discharge Me!": Chain-of-Thought Instruction Finetuning Large Language Models for Discharge Summaries](https://arxiv.org/abs/2407.17636) — **BioNLP** <sub>2024-07 · 5 citations</sub>
- [FZI-WIM at SemEval-2024 Task 2: Self-Consistent CoT for Complex NLI in Biomedical Domain](https://arxiv.org/abs/2406.10040) — **SemEval** <sub>2024-06 · 3 citations</sub>
- [Chain-of-Though (CoT) prompting strategies for medical error detection and correction](https://arxiv.org/abs/2406.09103) — **ClinicalNLP** <sub>2024-06 · 11 citations</sub>
- [A ChatGPT Aided Explainable Framework for Zero-Shot Medical Image Diagnosis](https://arxiv.org/abs/2307.01981) <sub>2023-07</sub>
  <sub>Early work making the decision process of zero-shot medical image diagnosis explicit and inspectable.</sub>

### Test-Time Scaling & Search · 测试期扩展与搜索 <sub>4</sub>

- [Med-VRAgent: A Framework for Medical Visual Reasoning-Enhanced Agents](https://arxiv.org/abs/2510.18424) — **EMNLP** <sub>2025-10 · 3 citations</sub>
- [Rethinking Inference-Time Scaling: Efficiency Limits and Linguistic Signals](https://arxiv.org/abs/2504.14047) <sub>2025-04 · 21 citations</sub>
- [m1: Unleash the Potential of Test-Time Scaling for Medical Reasoning with Large Language Models](https://arxiv.org/abs/2504.00869) <sub>2025-04 · 41 citations</sub>
- [RARE: Retrieval-Augmented Reasoning Enhancement for Large Language Models](https://arxiv.org/abs/2412.02830) — **ACL** <sub>2024-12 · 32 citations</sub>

### Knowledge-Grounded Reasoning (RAG / KG) · 知识增强推理（RAG / 知识图谱） <sub>20</sub>

- [NeuroGRIP: Retrieval-Augmented Graph Refinement for Knowledge-Grounded EEG Seizure Diagnosis](https://arxiv.org/abs/2607.14314) <sub>2026-07 · 1 citation</sub>
- [Expert-Guided Prompting and Retrieval-Augmented Generation for Emergency Medical Service Question Answering](https://arxiv.org/abs/2511.10900) — **AAAI** <sub>2025-11 · 4 citations</sub>
- [RAR$^2$: Retrieval-Augmented Medical Reasoning via Thought-Driven Retrieval](https://arxiv.org/abs/2509.22713) — **EMNLP** <sub>2025-09 · 3 citations</sub>
- [MIRAGE: Scaling Test-Time Inference with Parallel Graph-Retrieval-Augmented Reasoning Chains](https://arxiv.org/abs/2508.18260) — **AAAI** <sub>2025-08 · 7 citations</sub>
- [End-to-End Agentic RAG System Training for Traceable Diagnostic Reasoning](https://arxiv.org/abs/2508.15746) <sub>2025-08 · 13 citations</sub>
- [HierSearch: A Hierarchical Enterprise Deep Search Framework Integrating Local and Web Searches](https://arxiv.org/abs/2508.08088) — **AAAI** <sub>2025-08 · 7 citations</sub>
- [Patho-AgenticRAG: Towards Multimodal Agentic Retrieval-Augmented Generation for Pathology VLMs via Reinforcement Learning](https://arxiv.org/abs/2508.02258) — **AAAI** <sub>2025-08 · 13 citations</sub>
- [Multi-step retrieval and reasoning improves radiology question answering with large language models](https://arxiv.org/abs/2508.00743) — **npj Digital Medicine** <sub>2025-08 · 18 citations</sub>
- [DoctorRAG: Medical RAG Fusing Knowledge with Patient Analogy through Textual Gradients](https://arxiv.org/abs/2505.19538) <sub>2025-05 · 10 citations</sub>
- [A Multimodal Multi-Agent Framework for Radiology Report Generation](https://arxiv.org/abs/2505.09787) <sub>2025-05 · 13 citations</sub>
- [Medical Reasoning in LLMs: An In-Depth Analysis of DeepSeek R1](https://arxiv.org/abs/2504.00016) — **Frontiers in AI** <sub>2025-03 · 50 citations</sub>
- [Experience Retrieval-Augmentation with Electronic Health Records Enables Accurate Discharge QA](https://arxiv.org/abs/2503.17933) — **ACL** <sub>2025-03 · 12 citations</sub>
- [Bias Evaluation and Mitigation in Retrieval-Augmented Medical Question-Answering Systems](https://arxiv.org/abs/2503.15454) — **AMIA** <sub>2025-03 · 8 citations</sub>
- [Integrating Chain-of-Thought and Retrieval Augmented Generation Enhances Rare Disease Diagnosis from Clinical Notes](https://arxiv.org/abs/2503.12286) — **Medicine Bulletin** <sub>2025-03 · 13 citations</sub>
- [Towards Conversational AI for Disease Management](https://arxiv.org/abs/2503.06074) <sub>2025-03 · 14 citations</sub>
- [Causal Graphs Meet Thoughts: Enhancing Complex Reasoning in Graph-Augmented LLMs](https://arxiv.org/abs/2501.14892) <sub>2025-01 · 17 citations</sub>
- [Tree-based RAG-Agent Recommendation System: A Case Study in Medical Test Data](https://arxiv.org/abs/2501.02727) <sub>2025-01 · 12 citations</sub>
- [Multi-OphthaLingua: A Multilingual Benchmark for Assessing and Debiasing LLM Ophthalmological QA in LMICs](https://arxiv.org/abs/2412.14304) <sub>2024-12 · 15 citations</sub>
- [HealthQ: Unveiling Questioning Capabilities of LLM Chains in Healthcare Conversations](https://arxiv.org/abs/2409.19487) — **Smart Health** <sub>2024-09 · 49 citations</sub>
- [DiReCT: Diagnostic Reasoning for Clinical Notes via Large Language Models](https://arxiv.org/abs/2408.01933) — **NeurIPS** <sub>2024-08 · 25 citations</sub>

## 🖼️ Multimodal Medical Reasoning · 多模态医学推理

> Reasoning chains that must land on pixels, slides, and waveforms — not just text.  
> <sub>推理链要落在像素、切片、波形上，而不只是文本。</sub>

### Imaging VLM Reasoning · 影像推理 VLM <sub>51</sub>

- [Scaling Up Formal Representation of Clinical Trial Protocols in Ensemble Logic Using LLMs: A Preliminary Study](https://arxiv.org/abs/2607.21307) <sub>2026-07 · 1 citation</sub>
- [Med-OPD: Improving Medical Vision-Language Models via Evidence-Aware On-Policy Distillation](https://arxiv.org/abs/2607.16303) <sub>2026-07 · 1 citation</sub>
- [BioMedVR: Confusion-Aware Mixture-of-Prompt Experts for Biomedical Visual Reprogramming](https://arxiv.org/abs/2606.24740) — **ECCV 2026** <sub>2026-06</sub>
  <sub>Mixture-of-prompt experts targeted at confusable cases in biomedical visual reasoning.</sub>
- [Enhancing Pathological VLMs with Cross-scale Reasoning](https://arxiv.org/abs/2606.17412) <sub>2026-06 · 2 citations</sub>
- [Lost in Volume: The CT-SpatialVQA Benchmark for Evaluating Semantic-Spatial Understanding of 3D Medical Vision-Language Models](https://arxiv.org/abs/2605.08787) <sub>2026-05 · 4 citations</sub>
- [MedVR: Annotation-Free Medical Visual Reasoning via Agentic Reinforcement Learning](https://arxiv.org/abs/2604.08203) <sub>2026-04 · 6 citations</sub>
- [A Reasoning-Enabled Vision-Language Foundation Model for Chest X-ray Interpretation](https://arxiv.org/abs/2604.00493) <sub>2026-04 · 4 citations</sub>
- [CarePilot: A Multi-Agent Framework for Long-Horizon Computer Task Automation in Healthcare](https://arxiv.org/abs/2603.24157) <sub>2026-03 · 5 citations</sub>
- [MedMO: Grounding and Understanding Multimodal Large Language Model for Medical Images](https://arxiv.org/abs/2602.06965) <sub>2026-02 · 9 citations</sub>
- [MedGRPO: Multi-Task Reinforcement Learning for Heterogeneous Medical Video Understanding](https://arxiv.org/abs/2512.06581) <sub>2025-12 · 8 citations</sub>
- [Med-CMR: A Fine-Grained Benchmark Integrating Visual Evidence and Clinical Logic for Medical Complex Multimodal Reasoning](https://arxiv.org/abs/2512.00818) <sub>2025-11 · 12 citations</sub>
- [S-Chain: Structured Visual Chain-of-Thought For Medicine](https://arxiv.org/abs/2510.22728) <sub>2025-10 · 10 citations</sub>
- [3DReasonKnee: Advancing Grounded Reasoning in Medical Vision Language Models](https://arxiv.org/abs/2510.20967) — **PSB** <sub>2025-10 · 5 citations</sub>
- [MedReason-R1: Learning to Reason for CT Diagnosis with Reinforcement Learning and Local Zoom](https://arxiv.org/abs/2510.19626) — **ISBI** <sub>2025-10 · 3 citations</sub>
- [Think Twice to See More: Iterative Visual Reasoning in Medical VLMs](https://arxiv.org/abs/2510.10052) <sub>2025-10 · 13 citations</sub>
- [Hulu-Med: A Transparent Generalist Model towards Holistic Medical Vision-Language Understanding](https://arxiv.org/abs/2510.08668) <sub>2025-10 · 90 citations</sub>
- [Toward a Vision-Language Foundation Model for Medical Data: Multimodal Dataset and Benchmarks for Vietnamese PET/CT Report Generation](https://arxiv.org/abs/2509.24739) — **NeurIPS** <sub>2025-09 · 8 citations</sub>
- [EditGRPO: Reinforcement Learning with Post-Rollout Edits for Clinically Accurate Chest X-Ray Report Generation](https://arxiv.org/abs/2509.22812) — **AACL-IJCNLP** <sub>2025-09 · 11 citations</sub>
- [Knowing or Guessing? Robust Medical Visual Question Answering via Joint Consistency and Contrastive Learning](https://arxiv.org/abs/2508.18687) — **MICCAI** <sub>2025-08 · 4 citations</sub>
- [DINOv3 with Test-Time Training for Medical Image Registration](https://arxiv.org/abs/2508.14809) — **SPIE Medical Imaging** <sub>2025-08 · 8 citations</sub>
- [Benchmarking GPT-5 for Zero-Shot Multimodal Medical Reasoning in Radiology and Radiation Oncology](https://arxiv.org/abs/2508.13192) — **SPIE Medical Imaging** <sub>2025-08 · 8 citations</sub>
- [Performance of GPT-5 in Brain Tumor MRI Reasoning](https://arxiv.org/abs/2508.10865) — **SPIE Medical Imaging** <sub>2025-08 · 8 citations</sub>
- [MedAtlas: Evaluating LLMs for Multi-Round, Multi-Task Medical Reasoning Across Diverse Imaging Modalities and Clinical Text](https://arxiv.org/abs/2508.10947) — **AAAI** <sub>2025-08 · 6 citations</sub>
- [MedReasoner: Reinforcement Learning Drives Reasoning Grounding from Clinical Thought to Pixel-Level Precision](https://arxiv.org/abs/2508.08177) — **AAAI** <sub>2025-08 · 9 citations</sub>
- [PriorRG: Prior-Guided Contrastive Pre-training and Coarse-to-Fine Decoding for Chest X-ray Report Generation](https://arxiv.org/abs/2508.05353) — **AAAI** <sub>2025-08 · 11 citations</sub>
- [CLARIFID: Improving Radiology Report Generation by Reinforcing Clinically Accurate Impressions and Enforcing Detailed Findings](https://arxiv.org/abs/2507.17234) — **Expert Systems with Applications** <sub>2025-07 · 3 citations</sub>
- [MedGemma Technical Report](https://arxiv.org/abs/2507.05201) <sub>2025-07 · 416 citations</sub>
- [MOTOR: Multimodal Optimal Transport via Grounded Retrieval in Medical Visual Question Answering](https://arxiv.org/abs/2506.22900) — **MICCAI** <sub>2025-06 · 10 citations</sub>
- [Thought Graph Traversal for Test-time Scaling in Chest X-ray VLLMs](https://arxiv.org/abs/2506.11989) — **Pattern Recognition** <sub>2025-06 · 5 citations</sub>
- [Lingshu: A Generalist Foundation Model for Unified Multimodal Medical Understanding and Reasoning](https://arxiv.org/abs/2506.07044) <sub>2025-06 · 212 citations</sub>
- [DrVD-Bench: Do Vision-Language Models Reason Like Human Doctors in Medical Image Diagnosis?](https://arxiv.org/abs/2505.24173) — **NeurIPS** <sub>2025-05 · 12 citations</sub>
- [Are Vision Language Models Ready for Clinical Diagnosis? A 3D Medical Benchmark for Tumor-centric Visual Question Answering](https://arxiv.org/abs/2505.18915) <sub>2025-05 · 17 citations</sub>
- [CXReasonBench: A Benchmark for Evaluating Structured Diagnostic Reasoning in Chest X-rays](https://arxiv.org/abs/2505.18087) — **NeurIPS** <sub>2025-05 · 5 citations</sub>
- [RadZero: Similarity-Based Cross-Attention for Explainable Vision-Language Alignment in Chest X-ray with Zero-Shot Multi-Task Capability](https://arxiv.org/abs/2504.07416) — **NeurIPS** <sub>2025-04 · 6 citations</sub>
- [Med3DVLM: An Efficient Vision-Language Model for 3D Medical Image Analysis](https://arxiv.org/abs/2503.20047) — **IEEE JBHI** <sub>2025-03 · 60 citations</sub>
- [Progressive Test Time Energy Adaptation for Medical Image Segmentation](https://arxiv.org/abs/2503.16616) — **ICCV** <sub>2025-03 · 4 citations</sub>
- [MedVLM-R1: Incentivizing Medical Reasoning Capability of Vision-Language Models (VLMs) via Reinforcement Learning](https://arxiv.org/abs/2502.19634) — **MICCAI** <sub>2025-02 · 204 citations</sub>
- [RadAlign: Advancing Radiology Report Generation with Vision-Language Concept Alignment](https://arxiv.org/abs/2501.07525) — **MICCAI** <sub>2025-01 · 23 citations</sub>
- [Libra: Leveraging Temporal Images for Biomedical Radiology Analysis](https://arxiv.org/abs/2411.19378) — **ACL** <sub>2024-11 · 33 citations</sub>
- [MAIRA-Seg: Enhancing Radiology Report Generation with Segmentation-Aware Multimodal Large Language Models](https://arxiv.org/abs/2411.11362) — **ML4H@NeurIPS** <sub>2024-11 · 11 citations</sub>
- [R-LLaVA: Improving Med-VQA Understanding through Visual Region of Interest](https://arxiv.org/abs/2410.20327) <sub>2024-10</sub>
  <sub>Injects clinician-prior regions of interest into Med-VQA so answers are anchored to specific image regions.</sub>
- [CheXalign: Preference fine-tuning in chest X-ray interpretation models without human feedback](https://arxiv.org/abs/2410.07025) — **ACL** <sub>2024-10 · 8 citations</sub>
- [MC-CoT: A Modular Collaborative CoT Framework for Zero-shot Medical-VQA with LLM and MLLM Integration](https://arxiv.org/abs/2410.04521) <sub>2024-10 · 28 citations</sub>
- [An X-Ray Is Worth 15 Features: Sparse Autoencoders for Interpretable Radiology Report Generation](https://arxiv.org/abs/2410.03334) <sub>2024-10 · 27 citations</sub>
- [KARGEN: Knowledge-enhanced Automated Radiology Report Generation Using Large Language Models](https://arxiv.org/abs/2409.05370) — **MICCAI** <sub>2024-09 · 17 citations</sub>
- [M4CXR: Exploring Multi-task Potentials of Multi-modal Large Language Models for Chest X-ray Interpretation](https://arxiv.org/abs/2408.16213) — **IEEE TNNLS** <sub>2024-08 · 24 citations</sub>
- [Beyond the Hype: A dispassionate look at vision-language models in medical scenario](https://arxiv.org/abs/2408.08704) — **IEEE TNNLS** <sub>2024-08 · 16 citations</sub>
- [GPT-4V Cannot Generate Radiology Reports Yet](https://arxiv.org/abs/2407.12176) — **NAACL** <sub>2024-07 · 10 citations</sub>
- [CXR-Agent: Vision-language models for chest X-ray interpretation with uncertainty aware radiology reporting](https://arxiv.org/abs/2407.08811) <sub>2024-07 · 18 citations</sub>
- [Evidential Concept Embedding Models: Towards Reliable Concept Explanations for Skin Disease Diagnosis](https://arxiv.org/abs/2406.19130) — **MICCAI** <sub>2024-06 · 9 citations</sub>
- [FPN-IAIA-BL: A Multi-Scale Interpretable Deep Learning Model for Classification of Mass Margins in Digital Mammography](https://arxiv.org/abs/2406.06386) — **CVPRW** <sub>2024-06 · 5 citations</sub>

### Pathology & Whole-Slide Reasoning · 病理与全切片推理 <sub>17</sub>

- [PathAgentBench: Benchmarking Evidence-Seeking Vision-Language Models on Whole-Slide Pathology Image](https://arxiv.org/abs/2607.19261) <sub>2026-07 · 2 citations</sub>
- [ActWorld: From Explorable to Interactive World Model via Action-Aware Memory](https://arxiv.org/abs/2606.17730) <sub>2026-06 · 4 citations</sub>
- [Learnable Token Sparsification for Efficient Gigapixel Whole Slide Image Reasoning](https://arxiv.org/abs/2606.08641) <sub>2026-06 · 2 citations</sub>
- [MedGemma 1.5 Technical Report](https://arxiv.org/abs/2604.05081) <sub>2026-04 · 23 citations</sub>
- [MIRAGE: The Illusion of Visual Understanding](https://arxiv.org/abs/2603.21687) <sub>2026-03 · 45 citations</sub>
- [Multimodal Model for Computational Pathology:Representation Learning and Image Compression](https://arxiv.org/abs/2603.18660) <sub>2026-03 · 6 citations</sub>
- [TC-SSA: Token Compression via Semantic Slot Aggregation for Gigapixel Pathology Reasoning](https://arxiv.org/abs/2603.01143) <sub>2026-03 · 16 citations</sub>
- [Histopath-C: Towards Realistic Domain Shifts for Histopathology Vision-Language Adaptation](https://arxiv.org/abs/2601.12493) — **WACV** <sub>2026-01 · 3 citations</sub>
- [PathAgent: Toward Interpretable Analysis of Whole-slide Pathology Images via Large Language Model-based Agentic Reasoning](https://arxiv.org/abs/2511.17052) <sub>2025-11 · 15 citations</sub>
- [Augmentation-based Domain Generalization and Joint Training from Multiple Source Domains for Whole Heart Segmentation](https://arxiv.org/abs/2508.04552) — **CARE@MICCAI** <sub>2025-08 · 3 citations</sub>
- [Evidence-based diagnostic reasoning with multi-agent copilot for human pathology](https://arxiv.org/abs/2506.20964) <sub>2025-06 · 26 citations</sub>
- [Historical Report Guided Bi-modal Concurrent Learning for Pathology Report Generation](https://arxiv.org/abs/2506.18658) — **MICCAI** <sub>2025-06 · 7 citations</sub>
- [RadFabric: Agentic AI System with Reasoning Capability for Radiology](https://arxiv.org/abs/2506.14142) <sub>2025-06 · 10 citations</sub>
- [PRISM2: Unlocking Multi-Modal General Pathology AI with Clinical Dialogue](https://arxiv.org/abs/2506.13063) <sub>2025-06 · 12 citations</sub>
- [CoC: Chain-of-Cancer based on Cross-Modal Autoregressive Traction for Survival Prediction](https://arxiv.org/abs/2506.15696) — **MICCAI** <sub>2025-05 · 3 citations</sub>
- [CPathAgent: An Agent-based Foundation Model for Interpretable High-Resolution Pathology Image Analysis Mimicking Pathologists' Diagnostic Logic](https://arxiv.org/abs/2505.20510) — **NeurIPS** <sub>2025-05 · 26 citations</sub>
- [GRAPHITE: Graph-Based Interpretable Tissue Examination for Enhanced Explainability in Breast Cancer Histopathology](https://arxiv.org/abs/2501.04206) — **Computers in Biology and Medicine** <sub>2025-01 · 6 citations</sub>

### Cross-Modal Fusion & Modality Generalization · 跨模态融合与模态泛化 <sub>7</sub>

- [Resource-Efficient Iterative LLM-Based NAS with Feedback Memory](https://arxiv.org/abs/2603.12091) <sub>2026-03 · 12 citations</sub>
- [ECG-R1: Protocol-Guided and Modality-Agnostic MLLM for Reliable ECG Interpretation](https://arxiv.org/abs/2602.04279) <sub>2026-02 · 11 citations</sub>
- [EEG-VLM: A Hierarchical Vision-Language Model with Multi-Level Feature Alignment and Visually Enhanced Language-Guided Reasoning for EEG Image-Based Sleep Stage Prediction](https://arxiv.org/abs/2511.19155) — **IEEE JBHI** <sub>2025-11 · 4 citations</sub>
- [Constructing Ophthalmic MLLM for Positioning-diagnosis Collaboration Through Clinical Cognitive Chain Reasoning](https://arxiv.org/abs/2507.17539) — **ICCV** <sub>2025-07 · 9 citations</sub>
- [InsertRank: LLMs can reason over BM25 scores to Improve Listwise Reranking](https://arxiv.org/abs/2506.14086) — **WSDM** <sub>2025-06 · 4 citations</sub>
- [Test-time Adaptation for Foundation Medical Segmentation Model without Parametric Updates](https://arxiv.org/abs/2504.02008) — **ICCV** <sub>2025-04 · 8 citations</sub>
- [MotionTTT: 2D Test-Time-Training Motion Estimation for 3D Motion Corrected MRI](https://arxiv.org/abs/2409.09370) — **NeurIPS** <sub>2024-09 · 4 citations</sub>

## 🩺 Agentic Diagnostic Reasoning · 智能体式诊断推理

> Multi-turn, multi-role, tool-using diagnostic reasoning. Only works with a novel reasoning mechanism — plain pipeline orchestration is out of scope.  
> <sub>多轮、多角色、可调用工具的诊断推理。只收推理机制有创新的工作，纯流程编排不收。</sub>

### Interactive & Proactive Diagnostic Reasoning · 交互式与主动式诊断推理 <sub>23</sub>

- [CausalFlow: Causal Attribution and Counterfactual Repair for LLM Agent Failures](https://arxiv.org/abs/2605.25338) <sub>2026-05 · 3 citations</sub>
- [Act Wisely: Cultivating Meta-Cognitive Tool Use in Agentic Multimodal Models](https://arxiv.org/abs/2604.08545) <sub>2026-04 · 10 citations</sub>
- [XrayClaw: Cooperative-Competitive Multi-Agent Alignment for Trustworthy Chest X-ray Diagnosis](https://arxiv.org/abs/2604.02695) <sub>2026-04 · 6 citations</sub>
- [Meissa: Multi-modal Medical Agentic Intelligence](https://arxiv.org/abs/2603.09018) <sub>2026-03 · 5 citations</sub>
- [Reasoning as Gradient: Scaling MLE Agents Beyond Tree Search](https://arxiv.org/abs/2603.01692) — **ACL** <sub>2026-03 · 3 citations</sub>
- [Do Mixed-Vendor Multi-Agent LLMs Improve Clinical Diagnosis?](https://arxiv.org/abs/2603.04421) — **HeaLing** <sub>2026-02 · 3 citations</sub>
- [LingxiDiagBench: A Multi-Agent Framework for Benchmarking LLMs in Chinese Psychiatric Consultation and Diagnosis](https://arxiv.org/abs/2602.09379) — **KDD** <sub>2026-02 · 5 citations</sub>
- [DemMA: Dementia Multi-Turn Dialogue Agent with Expert-Guided Reasoning and Action Simulation](https://arxiv.org/abs/2601.06373) — **ACL** <sub>2026-01 · 3 citations</sub>
- [MedDialogRubrics: A Comprehensive Benchmark and Evaluation Framework for Multi-turn Medical Consultations in Large Language Models](https://arxiv.org/abs/2601.03023) <sub>2026-01 · 11 citations</sub>
- [DART: Leveraging Multi-Agent Disagreement for Tool Recruitment in Multimodal Reasoning](https://arxiv.org/abs/2512.07132) — **EACL** <sub>2025-12 · 4 citations</sub>
- [LungNoduleAgent: A Collaborative Multi-Agent System for Precision Diagnosis of Lung Nodules](https://arxiv.org/abs/2511.21042) — **AAAI** <sub>2025-11 · 6 citations</sub>
- [MedCoAct: Confidence-Aware Multi-Agent Collaboration for Complete Clinical Decision](https://arxiv.org/abs/2510.10461) — **BIBM** <sub>2025-10 · 4 citations</sub>
- [MedLA: A Logic-Driven Multi-Agent Framework for Complex Medical Reasoning with Large Language Models](https://arxiv.org/abs/2509.23725) — **AAAI** <sub>2025-09 · 12 citations</sub>
- [Automated Clinical Problem Detection from SOAP Notes using a Collaborative Multi-Agent LLM Architecture](https://arxiv.org/abs/2508.21803) — **ACM BCB** <sub>2025-08 · 5 citations</sub>
- [KERAP: A Knowledge-Enhanced Reasoning Approach for Accurate Zero-shot Diagnosis Prediction Using Multi-agent LLMs](https://arxiv.org/abs/2507.02773) — **AMIA** <sub>2025-07 · 15 citations</sub>
- [MMedAgent-RL: Optimizing Multi-Agent Collaboration for Multimodal Medical Reasoning](https://arxiv.org/abs/2506.00555) <sub>2025-05 · 42 citations</sub>
- [A Survey of Slow Thinking-based Reasoning LLMs using Reinforced Learning and Inference-time Scaling Law](https://arxiv.org/abs/2505.02665) <sub>2025-05 · 20 citations</sub>
- [MAGI: Multi-Agent Guided Interview for Psychiatric Assessment](https://arxiv.org/abs/2504.18260) — **ACL** <sub>2025-04 · 19 citations</sub>
- [From Metaphor to Mechanism: How LLMs Decode Traditional Chinese Medicine Symbolic Language for Modern Clinical Relevance](https://arxiv.org/abs/2503.02760) — **IJCNN** <sub>2025-03 · 6 citations</sub>
- [MEDDxAgent: A Unified Modular Agent Framework for Explainable Automatic Differential Diagnosis](https://arxiv.org/abs/2502.19175) — **ACL** <sub>2025-02 · 26 citations</sub>
- [Enhancing Hepatopathy Clinical Trial Efficiency: A Secure, Large Language Model-Powered Pre-Screening Pipeline](https://arxiv.org/abs/2502.18531) — **BioData Mining** <sub>2025-02 · 7 citations</sub>
- [Nuclear Deployed: Analyzing Catastrophic Risks in Decision-making of Autonomous LLM Agents](https://arxiv.org/abs/2502.11355) — **ACL** <sub>2025-02 · 31 citations</sub>
- [Superhuman performance of a large language model on the reasoning tasks of a physician](https://arxiv.org/abs/2412.10849) <sub>2024-12 · 83 citations</sub>

## 📊 Evaluation, Benchmarks & Trustworthiness · 评测、基准与可信度

> Is the reasoning gain real? The section this list most wants to get right.  
> <sub>推理增益是真的吗？这一节是本仓库最想做扎实的部分。</sub>

### Reasoning Benchmarks & Datasets · 推理基准与数据集 <sub>81</sub>

- [PathView-Bench: Can Multimodal Large Language Models Achieve Fine-grained Multiscale Understanding of Pathology Images?](https://arxiv.org/abs/2607.28318) <sub>2026-07 · 1 citation</sub>
- [Can Multimodal Large Language Models Understand OCT?](https://arxiv.org/abs/2607.16609) <sub>2026-07 · 2 citations</sub>
- [Demystifying On-Policy Distillation: Roles, Pathologies, and Regulations](https://arxiv.org/abs/2607.13399) <sub>2026-07 · 4 citations</sub>
- [TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments](https://arxiv.org/abs/2607.12480) <sub>2026-07 · 1 citation</sub>
- [Diagnosing and Mitigating Thinking Collapse in On-Policy Self-Distillation](https://arxiv.org/abs/2607.10805) <sub>2026-07 · 2 citations</sub>
- [CLIR-Bench: Benchmarking Multimodal Question Answering over Irregular Clinical Time Series](https://arxiv.org/abs/2607.09880) <sub>2026-07 · 2 citations</sub>
- [OmniFood-Bench: Evaluating VLMs for Nutrient Reasoning and Personalized Health Advice](https://arxiv.org/abs/2607.08423) <sub>2026-07 · 1 citation</sub>
- [Aligning Clinical Needs and AI Capabilities: A Survey on LLMs for Medical Reasoning](https://arxiv.org/abs/2607.07761) — **MIR** <sub>2026-07 · 3 citations</sub>
- [Overview of the NLPCC 2026 Shared Task 1: Difficulty-Aware Multilingual and Multimodal Medical Instructional Video Understanding Evaluation](https://arxiv.org/abs/2607.06618) <sub>2026-07 · 2 citations</sub>
- [EHR-Complex: Benchmarking Medical Agents for Complex Clinical Reasoning](https://arxiv.org/abs/2606.23301) <sub>2026-06 · 2 citations</sub>
- [Watch, Remember, Reason: Human-View Video Understanding with MLLMs](https://arxiv.org/abs/2606.07433) <sub>2026-06 · 2 citations</sub>
- [Artifact-Bench: Evaluating MLLMs on Detecting and Assessing the Artifacts of AI-Generated Videos](https://arxiv.org/abs/2605.18984) <sub>2026-05 · 3 citations</sub>
- [VT-Bench: A Unified Benchmark for Visual-Tabular Multi-Modal Learning](https://arxiv.org/abs/2605.08146) <sub>2026-05 · 3 citations</sub>
- [Reasoning emerges from constrained inference manifolds in large language models](https://arxiv.org/abs/2605.08142) <sub>2026-05 · 6 citations</sub>
- [Medical thinking with multiple images](https://arxiv.org/abs/2604.16506) <sub>2026-04 · 6 citations</sub>
- [Finding and Reactivating Post-Trained LLMs' Hidden Safety Mechanisms](https://arxiv.org/abs/2604.00012) — **NeurIPS** <sub>2026-03 · 3 citations</sub>
- [MediX-R1: Open Ended Medical Reinforcement Learning](https://arxiv.org/abs/2602.23363) <sub>2026-02 · 6 citations</sub>
- [MM-NeuroOnco: A Multimodal Benchmark and Instruction Dataset for MRI-Based Brain Tumor Diagnosis](https://arxiv.org/abs/2602.22955) <sub>2026-02</sub>
  <sub>MRI brain-tumor benchmark that requires reasoning tied to imaging manifestations, not just the diagnostic label.</sub>
- [LeafNet: A Large-Scale Dataset and Comprehensive Benchmark for Foundational Vision-Language Understanding of Plant Diseases](https://arxiv.org/abs/2602.13662) <sub>2026-02 · 7 citations</sub>
- [LiveMedBench: A Contamination-Free Medical Benchmark for LLMs with Automated Rubric Evaluation](https://arxiv.org/abs/2602.10367) <sub>2026-02 · 7 citations</sub>
- [EHRWorld: A Patient-Centric Medical World Model for Long-Horizon Clinical Trajectories](https://arxiv.org/abs/2602.03569) <sub>2026-02 · 8 citations</sub>
- [Who Endorsed It? Measuring Authority Bias Across Expertise Levels in Language Models](https://arxiv.org/abs/2601.13433) — **GEM** <sub>2026-01 · 3 citations</sub>
- [Patient-Similarity Cohort Reasoning in Clinical Text-to-SQL](https://arxiv.org/abs/2601.09876) — **EACL** <sub>2026-01 · 3 citations</sub>
- [Rewarding the Rare: Uniqueness-Aware RL for Creative Problem Solving in LLMs](https://arxiv.org/abs/2601.08763) — **ACL** <sub>2026-01 · 9 citations</sub>
- [OctoMed: Data Recipes for State-of-the-Art Multimodal Medical Reasoning](https://arxiv.org/abs/2511.23269) <sub>2025-11 · 9 citations</sub>
- [OralGPT-Omni: A Versatile Dental Multimodal Large Language Model](https://arxiv.org/abs/2511.22055) <sub>2025-11 · 10 citations</sub>
- [BioMedSearch: A Multi-Source Biomedical Retrieval Framework Based on LLMs](https://arxiv.org/abs/2510.13926) — **BIBM** <sub>2025-10 · 5 citations</sub>
- [Simulating Viva Voce Examinations to Evaluate Clinical Reasoning in Large Language Models](https://arxiv.org/abs/2510.10278) — **NeurIPS** <sub>2025-10 · 6 citations</sub>
- [A Chain-of-thought Reasoning Breast Ultrasound Dataset Covering All Histopathology Categories](https://arxiv.org/abs/2509.17046) — **Scientific Data** <sub>2025-09 · 6 citations</sub>
- [DischargeSim: A Simulation Benchmark for Educational Doctor-Patient Communication at Discharge](https://arxiv.org/abs/2509.07188) — **EMNLP** <sub>2025-09 · 7 citations</sub>
- [PsychiatryBench: A Multi-Task Benchmark for LLMs in Psychiatry](https://arxiv.org/abs/2509.09711) — **npj Digital Medicine** <sub>2025-09 · 5 citations</sub>
- [Baichuan-M2: Scaling Medical Capability with Large Verifier System](https://arxiv.org/abs/2509.02208) <sub>2025-09 · 49 citations</sub>
- [Exploring Efficiency Frontiers of Thinking Budget in Medical Reasoning: Scaling Laws between Computational Resources and Reasoning Quality](https://arxiv.org/abs/2508.12140) — **JBI** <sub>2025-08 · 5 citations</sub>
- [Capabilities of GPT-5 on Multimodal Medical Reasoning](https://arxiv.org/abs/2508.08224) — **SPIE Medical Imaging** <sub>2025-08 · 80 citations</sub>
- [Neovascularization Segmentation via a Multilateral Interaction-Enhanced Graph Convolutional Network](https://arxiv.org/abs/2508.03197) — **IEEE TPAMI** <sub>2025-08 · 4 citations</sub>
- [ReXGroundingCT: A 3D Chest CT Dataset for Segmentation of Findings from Free-Text Reports](https://arxiv.org/abs/2507.22030) — **NEJM AI** <sub>2025-07 · 18 citations</sub>
- [Single Image Test-Time Adaptation via Multi-View Co-Training](https://arxiv.org/abs/2506.23705) — **MICCAI** <sub>2025-06 · 4 citations</sub>
- [Chiron-o1: Igniting Multimodal Large Language Models towards Generalizable Medical Reasoning via Mentor-Intern Collaborative Search](https://arxiv.org/abs/2506.16962) — **NeurIPS** <sub>2025-06 · 15 citations</sub>
- [Thought Crime: Backdoors and Emergent Misalignment in Reasoning Models](https://arxiv.org/abs/2506.13206) <sub>2025-06 · 64 citations</sub>
- [Med-U1: Incentivizing Unified Medical Reasoning in LLMs via Large-scale Reinforcement Learning](https://arxiv.org/abs/2506.12307) <sub>2025-06 · 11 citations</sub>
- [ReasonMed: A 370K Multi-Agent Generated Dataset for Advancing Medical Reasoning](https://arxiv.org/abs/2506.09513) — **EMNLP** <sub>2025-06 · 28 citations</sub>
- [3D-RAD: A Comprehensive 3D Radiology Med-VQA Dataset with Multi-Temporal Analysis and Diverse Diagnostic Tasks](https://arxiv.org/abs/2506.11147) — **NeurIPS** <sub>2025-06 · 23 citations</sub>
  <sub>3D radiology Med-VQA dataset with multi-temporal comparison tasks, moving the reasoning load from a single frame to a time series.</sub>
- [Kvasir-VQA-x1: A Multimodal Dataset for Medical Reasoning and Robust MedVQA in Gastrointestinal Endoscopy](https://arxiv.org/abs/2506.09958) — **DEMI@MICCAI** <sub>2025-06 · 18 citations</sub>
- [SRPL-SFDA: SAM-Guided Reliable Pseudo-Labels for Source-Free Domain Adaptation in Medical Image Segmentation](https://arxiv.org/abs/2506.09403) — **Neurocomputing** <sub>2025-06 · 14 citations</sub>
- [Artificial Intelligence Should Genuinely Support Clinical Reasoning and Decision Making To Bridge the Translational Gap](https://arxiv.org/abs/2506.05030) — **npj Digital Medicine** <sub>2025-06 · 75 citations</sub>
- [ReXVQA: A Large-scale Visual Question Answering Benchmark for Generalist Chest X-ray Understanding](https://arxiv.org/abs/2506.04353) — **PSB** <sub>2025-06 · 23 citations</sub>
- [DeepSeek in Healthcare: A Survey of Capabilities, Risks, and Clinical Applications of Open-Source Large Language Models](https://arxiv.org/abs/2506.01257) <sub>2025-06 · 14 citations</sub>
- [Medical Large Vision Language Models with Multi-Image Visual Ability](https://arxiv.org/abs/2505.19031) — **MICCAI** <sub>2025-05 · 15 citations</sub>
- [Point, Detect, Count: Multi-Task Medical Image Understanding with Instruction-Tuned Vision-Language Models](https://arxiv.org/abs/2505.16647) — **CBMS** <sub>2025-05 · 3 citations</sub>
- [Beyond Empathy: Integrating Diagnostic and Therapeutic Reasoning with Large Language Models for Mental Health Counseling](https://arxiv.org/abs/2505.15715) <sub>2025-05 · 21 citations</sub>
- [DiagnosisArena: Benchmarking Diagnostic Reasoning for Large Language Models](https://arxiv.org/abs/2505.14107) — **ACL** <sub>2025-05 · 16 citations</sub>
- [NOVA: A Benchmark for Anomaly Localization and Clinical Reasoning in Brain MRI](https://arxiv.org/abs/2505.14064) <sub>2025-05 · 16 citations</sub>
- [MedCaseReasoning: Evaluating and learning diagnostic reasoning from clinical case reports](https://arxiv.org/abs/2505.11733) <sub>2025-05 · 28 citations</sub>
- [Disentangling Reasoning and Knowledge in Medical Large Language Models](https://arxiv.org/abs/2505.11462) <sub>2025-05 · 17 citations</sub>
- [CaReAQA: A Cardiac and Respiratory Audio Question Answering Model for Open-Ended Diagnostic Reasoning](https://arxiv.org/abs/2505.01199) — **CHIL** <sub>2025-05 · 10 citations</sub>
- [LLM Sensitivity Evaluation Framework for Clinical Diagnosis](https://arxiv.org/abs/2504.13475) — **COLING** <sub>2025-04 · 8 citations</sub>
- [UKBOB: One Billion MRI Labeled Masks for Generalizable 3D Medical Image Segmentation](https://arxiv.org/abs/2504.06908) — **ICCV** <sub>2025-04 · 4 citations</sub>
- [MedReason: Eliciting Factual Medical Reasoning Steps in LLMs via Knowledge Graphs](https://arxiv.org/abs/2504.00993) <sub>2025-04 · 107 citations</sub>
- [Self-Evolving Multi-Agent Simulations for Realistic Clinical Interactions](https://arxiv.org/abs/2503.22678) — **MICCAI** <sub>2025-03 · 43 citations</sub>
- [MDTeamGPT: A Self-Evolving LLM-based Multi-Agent Framework for Multi-Disciplinary Team Medical Consultation](https://arxiv.org/abs/2503.13856) <sub>2025-03 · 31 citations</sub>
- [Test-Time Domain Generalization via Universe Learning: A Multi-Graph Matching Approach for Medical Image Segmentation](https://arxiv.org/abs/2503.13012) — **CVPR** <sub>2025-03 · 7 citations</sub>
- [SurgRAW: Multi-Agent Workflow with Chain of Thought Reasoning for Robotic Surgical Video Analysis](https://arxiv.org/abs/2503.10265) — **IEEE RA-L** <sub>2025-03 · 18 citations</sub>
- [MedicalAgentsBench for Complex Medical Reasoning: Comparing Internalized Reasoning Models versus Externalized Agent-based Frameworks](https://arxiv.org/abs/2503.07459) — **Patterns** <sub>2025-03 · 44 citations</sub>
- [Citrus: Leveraging Expert Cognitive Pathways in a Medical Language Model for Advanced Medical Decision Support](https://arxiv.org/abs/2502.18274) <sub>2025-02 · 16 citations</sub>
- [Limitations of Large Language Models in Clinical Problem-Solving Arising from Inflexible Reasoning](https://arxiv.org/abs/2502.04381) — **Scientific Reports** <sub>2025-02 · 91 citations</sub>
- [MedRAX: Medical Reasoning Agent for Chest X-ray](https://arxiv.org/abs/2502.02673) — **ICML** <sub>2025-02 · 68 citations</sub>
- [MedXpertQA: Benchmarking Expert-Level Medical Reasoning and Understanding](https://arxiv.org/abs/2501.18362) — **ICML** <sub>2025-01 · 217 citations</sub>
- [FineMedLM-o1: Enhancing Medical Knowledge Reasoning Ability of LLM from Supervised Fine-Tuning to Test-Time Training](https://arxiv.org/abs/2501.09213) <sub>2025-01 · 12 citations</sub>
- [SAM-DA: Decoder Adapter for Efficient Medical Domain Adaptation](https://arxiv.org/abs/2501.06836) — **WACV** <sub>2025-01 · 6 citations</sub>
- [MedMobile: A mobile-sized language model with clinical capabilities](https://arxiv.org/abs/2410.09019) — **BMJ Digital Health & AI** <sub>2024-10 · 7 citations</sub>
- [CliMedBench: A Large-Scale Chinese Benchmark for Evaluating Medical Large Language Models in Clinical Scenarios](https://arxiv.org/abs/2410.03502) — **EMNLP** <sub>2024-10 · 18 citations</sub>
- [MedViLaM: A multimodal large language model with advanced generalizability and explainability for medical data understanding and generation](https://arxiv.org/abs/2409.19684) <sub>2024-09 · 20 citations</sub>
- [A Preliminary Study of o1 in Medicine: Are We Closer to an AI Doctor?](https://arxiv.org/abs/2409.15277) <sub>2024-09 · 51 citations</sub>
- [MAGDA: Multi-agent guideline-driven diagnostic assistance](https://arxiv.org/abs/2409.06351) — **MedAGI@MICCAI** <sub>2024-09 · 12 citations</sub>
- [Gradient Alignment Improves Test-Time Adaptation for Medical Image Segmentation](https://arxiv.org/abs/2408.07343) — **AAAI** <sub>2024-08 · 17 citations</sub>
- [LADDER: Language-Driven Slice Discovery and Error Rectification in Vision Classifiers](https://arxiv.org/abs/2408.07832) — **ACL** <sub>2024-07 · 7 citations</sub>
- [Learning 3D Gaussians for Extremely Sparse-View Cone-Beam CT Reconstruction](https://arxiv.org/abs/2407.01090) — **MICCAI** <sub>2024-07 · 26 citations</sub>
- [Test-time generative augmentation for medical image segmentation](https://arxiv.org/abs/2406.17608) — **Medical Image Analysis** <sub>2024-06 · 10 citations</sub>
- [BayTTA: Uncertainty-aware medical image classification with optimized test-time augmentation using Bayesian model averaging](https://arxiv.org/abs/2406.17640) — **Knowledge-Based Systems** <sub>2024-06 · 9 citations</sub>
- [Reasoning Like a Doctor: Improving Medical Dialogue Systems via Diagnostic Reasoning Process Alignment](https://arxiv.org/abs/2406.13934) — **ACL** <sub>2024-06 · 29 citations</sub>
- [Comparative Benchmarking of Failure Detection Methods in Medical Image Segmentation: Unveiling the Role of Confidence Aggregation](https://arxiv.org/abs/2406.03323) — **Medical Image Analysis** <sub>2024-06 · 23 citations</sub>

### Faithfulness, Hallucination & Shortcut Learning · 忠实性、幻觉与捷径学习 <sub>9</sub>

- [Dismantling Pathological Shortcuts: A Causal Framework for Faithful LVLM Decoding](https://arxiv.org/abs/2606.27596) <sub>2026-06 · 2 citations</sub>
- [Med-R2: An Adversarial Benchmark for Evidence-Grounded Reasoning in Medical VLMs](https://arxiv.org/abs/2605.24492) <sub>2026-05</sub>
  <sub>Adversarial benchmark with hierarchical perturbations: tests whether a VLM's answer rests on image evidence or on spurious priors.</sub>
- [Toward Better EHR Reasoning in LLMs: Reinforcement Learning with Expert Attention Guidance](https://arxiv.org/abs/2508.13579) — **AAAI** <sub>2025-08 · 5 citations</sub>
- [Reasoning in Computer Vision: Taxonomy, Models, Tasks, and Methodologies](https://arxiv.org/abs/2508.10523) <sub>2025-08 · 25 citations</sub>
- [Neurosymbolic Reasoning Shortcuts under the Independence Assumption](https://arxiv.org/abs/2507.11357) — **NeSy** <sub>2025-07 · 3 citations</sub>
- [DeVisE: Behavioral Testing of Medical Large Language Models](https://arxiv.org/abs/2506.15339) — **EACL** <sub>2025-06 · 3 citations</sub>
- [Spurious Correlations and Beyond: Understanding and Mitigating Shortcut Learning in SDOH Extraction with Large Language Models](https://arxiv.org/abs/2506.00134) — **ACL** <sub>2025-05 · 4 citations</sub>
- [Treble Counterfactual VLMs: A Causal Approach to Hallucination](https://arxiv.org/abs/2503.06169) — **EMNLP** <sub>2025-03 · 32 citations</sub>
- [Hallucination Detox: Sensitivity Dropout (SenD) for Large Language Model Training](https://arxiv.org/abs/2410.15460) — **ACL** <sub>2024-10 · 5 citations</sub>

### Clinical Alignment & Human-AI Evaluation · 临床对齐与人机协同评估 <sub>10</sub>

- [Information-seeking failures of large language models in agentic clinical reasoning](https://arxiv.org/abs/2607.10275) <sub>2026-07 · 1 citation</sub>
- [A prospective clinical feasibility study of a conversational diagnostic AI in an ambulatory primary care clinic](https://arxiv.org/abs/2603.08448) <sub>2026-03 · 7 citations</sub>
- [Diagnosing and Mitigating Sycophancy and Skepticism in LLM Causal Judgment](https://arxiv.org/abs/2601.08258) — **ACL** <sub>2026-01 · 10 citations</sub>
- [Foundation Models in Biomedical Imaging: Turning Hype into Reality](https://arxiv.org/abs/2512.15808) — **Nature Biomedical Engineering** <sub>2025-12 · 7 citations</sub>
- [Reliability of Large Language Model Generated Clinical Reasoning in Assisted Reproductive Technology: Blinded Comparative Evaluation Study](https://arxiv.org/abs/2510.16095) — **JMIR** <sub>2025-10 · 5 citations</sub>
- [Leveraging Imperfection with MEDLEY A Multi-Model Approach Harnessing Bias in Medical AI](https://arxiv.org/abs/2508.21648) — **Frontiers in AI** <sub>2025-08 · 5 citations</sub>
- [PASS: Probabilistic Agentic Supernet Sampling for Interpretable and Adaptive Chest X-Ray Reasoning](https://arxiv.org/abs/2508.10501) — **AAAI** <sub>2025-08 · 4 citations</sub>
- [Automating Expert-Level Medical Reasoning Evaluation of Large Language Models](https://arxiv.org/abs/2507.07988) — **npj Digital Medicine** <sub>2025-07 · 30 citations</sub>
- [Medical Hallucinations in Foundation Models and Their Impact on Healthcare](https://arxiv.org/abs/2503.05777) <sub>2025-02 · 157 citations</sub>
- [From Models to Microtheories: Distilling a Model's Topical Knowledge for Grounded Question Answering](https://arxiv.org/abs/2412.17701) — **ICLR** <sub>2024-12 · 3 citations</sub>

## 📚 Surveys & Position Papers · 综述与立场文章

### Surveys & Positions · 综述与立场 <sub>9</sub>

- [Counteraction-Aware Multi-Teacher On-Policy Distillation for General Capability Recovery with Domain Preservation](https://arxiv.org/abs/2605.27115) <sub>2026-05 · 3 citations</sub>
- [PhysicianBench: Evaluating LLM Agents in Real-World EHR Environments](https://arxiv.org/abs/2605.02240) <sub>2026-05 · 9 citations</sub>
- [Prompt-based Adaptation in Large-scale Vision Models: A Survey](https://arxiv.org/abs/2510.13219) — **TMLR** <sub>2025-10 · 27 citations</sub>
- [Reasoning LLMs in the Medical Domain: A Literature Survey](https://arxiv.org/abs/2508.19097) — **DSAA** <sub>2025-08 · 6 citations</sub>
- [Medical Reasoning in the Era of LLMs: A Systematic Review of Enhancement Techniques and Applications](https://arxiv.org/abs/2508.00669) <sub>2025-08 · 14 citations</sub>
- [Keeping Medical AI Healthy and Trustworthy: A Review of Detection and Correction Methods for System Degradation](https://arxiv.org/abs/2506.17442) — **IEEE TBME** <sub>2025-06 · 15 citations</sub>
- [MediSee: Reasoning-based Pixel-level Perception in Medical Images](https://arxiv.org/abs/2504.11008) — **ACM MM** <sub>2025-04 · 13 citations</sub>
- [A Survey of LLM-based Agents in Medicine: How far are we from Baymax?](https://arxiv.org/abs/2502.11211) — **ACL** <sub>2025-02 · 135 citations</sub>
- [Evaluation of OpenAI o1: Opportunities and Challenges of AGI](https://arxiv.org/abs/2409.18486) <sub>2024-09 · 172 citations</sub>


---

## Related lists

Neighbouring collections, each with a different centre of gravity:

- [Awesome-LLM-Reasoning-on-Medicine](https://github.com/pqpq17/Awesome-LLM-Reasoning-on-Medicine) — organized around Miller's Pyramid, accompanies a survey in *Machine Intelligence Research*.
- [medical-llm-reasoning-survey](https://github.com/zzma2/medical-llm-reasoning-survey) — taxonomy by modality, training-time vs test-time technique, and application.
- [Awesome-Medical-LLM-Agent](https://github.com/yczhou001/Awesome-Medical-LLM-Agent) — centred on single- and multi-agent medical systems.
- [Awesome-Specialized-Medical-LLMs](https://github.com/FreedomIntelligence/Awesome-Specialized-Medical-LLMs) — organized by ICD-10 chapter rather than by method.
- [awesome-multimodal-in-medical-imaging](https://github.com/richard-peng-xia/awesome-multimodal-in-medical-imaging) — multimodal medical imaging broadly, not reasoning-specific.

## Contributing

- **Open an issue** with the arXiv link — fastest, no setup.
- **Send a PR editing `data/papers.json`** — not `README.md`, which is generated from it. Run
  `python3 scripts/build_readme.py` and commit both files.

Corrections are as welcome as additions. If an annotation misreads your paper, say so in an issue and it will
be fixed or removed.

## License

[CC0-1.0](LICENSE) — public domain. The papers themselves belong to their authors.
