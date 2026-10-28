# AI Agent 核心研究领域图谱

> 编制日期：2026-10-28 · 用途：Awesome-Agent-Engineering 研究方向锚定与论文检索入口
> 核实说明见文末「引用核实与使用约定」

## 0. 为什么 Agent 是一个独立的研究体系

一个常被低估的事实是：Agent 研究并不等于"给大模型套一个调用循环"。从研究视角看，Agent 是一个横跨**感知—认知—行动—学习—治理**的全栈问题。超级智能体（Super Agent）的研究，必须在若干核心研究点上有专门的设计与论证，而非依赖单一基座模型的能力外溢。

老板关心的**意图识别**与**记忆（memory）**正是其中两个关键研究点，但它们远不是全部。下面把 Agent 研究拆成 **16 个核心研究领域**，每个领域给出定义、核心研究子问题与代表性论文。论文标注两种来源：`[核实]` 表示本轮检索到明确 venue/官方来源；`[公认]` 表示学界长期公认的标志性工作，venue 信息稳定，正式引用前以 arXiv/会议官网核对为准。

---

## 1. Agent 基础架构与编排（Foundation & Orchestration）

**定义**：研究单/多智能体的结构组织方式，包括推理-行动循环、角色分工、任务调度，以及"编排（Orchestration）"与"多智能体（Multi-Agent）"的边界。

**核心研究点**：
- 单智能体架构：ReAct 循环、Plan-Execute、Reflexion 闭环
- 多智能体系统（MAS）：角色生成、通信拓扑、协作 vs 对抗
- 编排范式：主控 agent 拆解-分发-汇总，与对等多智能体的适用边界
- 执行框架 / Harness：任务可靠性对外层基础设施的依赖

**代表性论文**：
- ReAct: Synergizing Reasoning and Acting in Language Models. Yao et al. ICLR 2023. `[核实]`
- A Survey on LLM-based Multi-Agent System: Recent Advances and New Frontiers. 哈工大 SCIR. arXiv:2412.17481, 2024. `[核实]`
- Harness for Large Language Model Agents: A Survey. 2026. `[核实]`
- Generative Agents: Interactive Simulacra of Human Behavior. Park et al. UIST 2023 (Best Paper). `[公认]`
- MetaGPT: Meta Programming for Multi-Agent Collaborative Framework. Hong et al. ICLR 2024. `[公认]`
- AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation. Wu et al. Microsoft, arXiv:2308.08155, 2023. `[公认]`
- CAMEL: Communicative Agents for "Mind" Exploration of Large Scale Language Model Society. Li et al. NeurIPS 2023. `[核实]`

---

## 2. 意图识别与任务规划（Intent Recognition & Planning）

**定义**：把用户模糊需求转化为可执行目标序列的过程，含意图理解、目标分解、动作规划。这是老板特别关心的"超级智能体意图识别"所在领域。

**核心研究点**：
- 意图理解与槽位填充（承接自对话系统，在 Agent 中作为规划前置）
- 目标分解（Goal Decomposition）：复杂任务→子任务树
- 任务规划（Task Planning）：符号规划、LLM-as-Planner、混合规划
- 思维树 / 思维图（Tree/Graph of Thoughts）：搜索式规划
- 开放式探索规划（如 Minecraft 长程任务）

**代表性论文**：
- ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023. `[核实]`
- Tree of Thoughts: Deliberate Problem Solving with Large Language Models. Yao et al. NeurIPS 2023. `[公认]`
- Voyager: An Open-Ended Embodied Agent with Large Language Models. Wang et al. NVIDIA, arXiv:2305.16291, 2023. `[公认]`
- LLM+P: Empowering Large Language Models with Optimal Planning Proficiency. Liu et al. arXiv:2304.11477, 2023. `[公认]`
- HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. Shen et al. NeurIPS 2023. `[公认]`

> 说明：意图识别作为独立子问题，其经典文献多在对话系统/任务型对话方向（如 intent classification、slot filling）；在 LLM Agent 范式下，意图识别常被规划模块吸收，专门针对"Agent 意图识别"的论文较少，是一个值得深耕的空白点。

---

## 3. 推理与反思（Reasoning & Reflection）

**定义**：研究智能体的多步推理能力与基于反馈的自我纠错机制。

**核心研究点**：
- 链式/树式/图式推理（CoT/ToT/GoT）
- 自我反思与经验回放（self-reflection）
- 语言强化学习（verbal reinforcement）：以自然语言反馈替代梯度更新
- 自迭代精炼（self-refine）

**代表性论文**：
- Chain-of-Thought Prompting Elicits Reasoning in Large Language Models. Wei et al. NeurIPS 2022. `[公认]`
- ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023. `[核实]`
- Reflexion: Language Agents with Verbal Reinforcement Learning. Shinn et al. NeurIPS 2023. arXiv:2303.11366. `[核实]`
- Self-Refine: Iterative Refinement with Self-Feedback. Madaan et al. NeurIPS 2023. `[公认]`

---

## 4. 记忆系统（Memory Systems）

**定义**：研究智能体如何存储、组织、检索、更新与遗忘信息，使其具备跨会话一致性与长期记忆。这是老板特别关心的第二个核心研究点，也是 2025—2026 年增长最快的研究方向之一。

**核心研究点**：
- 记忆分层：短期/工作记忆 vs 长期记忆（语义/情景/程序性）
- 记忆表示：向量库、知识图谱、时序图（如 Zep/Graphiti）
- 记忆生命周期：写入→检索→更新→遗忘（艾宾浩斯曲线启发）
- 记忆治理：隐私、删除权（GDPR 被遗忘权）、审计、记忆可擦除性
- 记忆架构工程化：Mem0、Letta、LangMem、MemOS 等

**代表性论文**：
- MemoryBank: Enhancing Large Language Models with Long-Term Memory. AAAI 2024. https://ojs.aaai.org/index.php/AAAI/article/view/29946 `[核实]`
- MemGPT: Towards LLMs as Operating Systems. Packer et al. arXiv:2310.08560, 2023. `[公认]`
- Memory in the Age of AI Agents: A Survey. NUS & 人大 & 复旦 & 北大, 2025. `[核实]`
- Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills. UIUC, 2026-03. `[核实]`
- 十大主流记忆架构综述（A-MEM / MemoryBank / MemGPT / Memθ / Memθᵍ / MemoChat / Zep / MemTree / MemoryOS / MemOS）. 2026. `[核实]`

---

## 5. 工具使用与函数调用（Tool Use & Function Calling）

**定义**：研究智能体理解、选择、调用与组合外部工具/API 的能力，以及让模型自主学会使用工具的训练方法。

**核心研究点**：
- 工具调用（function calling）：基于 schema 的结构化调用
- 工具学习（tool learning）：训练模型掌握大规模 API
- 工具组合 / API 编排：多工具链式调用
- 工具创建（tool making）：智能体自造工具

**代表性论文**：
- Toolformer: Language Models Can Teach Themselves to Use Tools. Schick et al. NeurIPS 2023. `[公认]`
- Gorilla: Large Language Model Connected with Massive APIs. Patil et al. UC Berkeley, arXiv:2305.15334, 2023. `[公认]`
- ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs. Qin et al. ICLR 2024. `[公认]`
- HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face. NeurIPS 2023. `[公认]`

---

## 6. 感知与多模态（Perception & Multimodality）

**定义**：研究智能体对视觉、GUI、网页、音频等多模态环境的感知与理解，是 Web/GUI Agent 的基础。

**核心研究点**：
- 视觉感知：截图理解、UI 元素定位
- 多模态融合：视觉-语言-动作
- GUI/Web 感知：DOM/像素级页面理解
- 具身感知：3D 场景与空间感知

**代表性论文**（项目 `methods.json` 已收录 36 条 Web & GUI Agent，此处列标志工作）：
- WebGPT: Browser-assisted question-answering with human feedback. OpenAI, arXiv:2112.09332, 2021. `[公认]`
- CogAgent: A Visual Language Model for GUI Agents. Tsinghua, 2023. `[公认]`
- AppAgent: Multimodal Agents as Smartphone Users. 2023. `[公认]`
- SeeAct: GPT-4V(ision) as a Generalist Web Agent. 2024. `[公认]`

---

## 7. 世界模型与仿真（World Models & Simulation）

**定义**：研究智能体内部对环境的建模与状态预测能力，使其能在"想象"中规划与学习。

**核心研究点**：
- 环境建模与状态预测（action-conditioned prediction）
- 生成式世界模型（视频生成路线）vs 潜空间预测（JEPA 路线）
- 长时序一致性与 OOD 物理泛化
- 可交互仿真环境

**代表性论文**：
- World Models. Ha & Schmidhuber. NeurIPS 2018. `[公认]`
- Dreamer V3. Hafner et al. 2023. `[公认]`
- A Path Towards Autonomous Machine Intelligence / V-JEPA. LeCun et al. Meta, 2024. `[公认]`
- Genie: A Generative Interactive Environment. DeepMind, 2024. `[公认]`

> 注：李飞飞近期撰文指出"世界模型"已成为 AI 领域最被过度使用的术语之一，研究时需精确定义所指路线。

---

## 8. 具身智能与机器人（Embodied Intelligence & Robotics）

**定义**：研究有身体、与物理世界交互的智能体，含机器人控制、导航、操作。与老板的 3DGS/空间智能主线天然交汇。

**核心研究点**：
- 视觉-语言-动作模型（VLA）
- 具身导航与操作
- 长程任务规划（开放世界）
- 空间智能与 3D 场景理解

**代表性论文**：
- Voyager: An Open-Ended Embodied Agent with Large Language Models. NVIDIA, arXiv:2305.16291, 2023. `[公认]`
- RT-2: Vision-Language-Action Models Transfer Web Knowledge to Robotic Control. Google DeepMind, 2023. `[公认]`
- PaLM-E: An Embodied Multimodal Language Model. Google, 2023. `[公认]`
- SayCan: Do As I Can, Not As I Say. Google, 2022. `[公认]`

---

## 9. 学习与自我进化（Learning & Self-Evolution）

**定义**：研究智能体如何通过经验持续改进，含在线学习、强化学习、自我奖励与后训练。

**核心研究点**：
- 语言强化学习（verbal RL）
- 自我奖励（self-rewarding）/ 自我改进
- 后训练（post-training）对 Agent 行为的塑造
- 技能习得与复用（skill learning）

**代表性论文**：
- Reflexion: Language Agents with Verbal Reinforcement Learning. NeurIPS 2023. `[核实]`
- Self-Rewarding Language Models. Meta, 2024. `[公认]`
- Adaptation of Agentic AI: A Survey of Post-Training, Memory, and Skills. UIUC, 2026-03. `[核实]`

---

## 10. 对齐、安全与可控性（Alignment, Safety & Controllability）

**定义**：研究让智能体行为符合人类价值、可控、可审计、可防御攻击的方法。Agent 获得数据库写入、API 调用等高危权限后，安全已成为生产级强制准入问题。

**核心研究点**：
- 价值对齐（RLHF / RLAIF）
- 安全护栏（guardrails）与形式化验证
- 红队测试（red teaming）
- 提示注入 / 越狱攻击防御
- Agent 权限治理与内部威胁建模

**代表性论文与框架**：
- NIST AI Risk Management Framework (AI RMF). `[核实]`
- garak: NVIDIA 大模型与 Agent 安全探测工具. `[核实]`
- 微软安全框架：将 AI Agent 视为内部威胁. 2026-10. `[核实]`
- LITMUS: 智能体行为越狱评测基准. 南航, NeurIPS 2026 Oral. `[核实]`
- InjecAgent / AgentDojo: 提示注入鲁棒性评测. `[公认]`

---

## 11. 评估与基准（Evaluation & Benchmarks）

**定义**：研究如何系统、可复现地评测智能体能力，是衡量一切进步的标尺。

**核心研究点**：
- 多环境能力评测（操作系统、数据库、Web、游戏）
- 长程任务与可靠性评测
- 安全/越狱专项评测
- 评测的可复现性与污染控制

**代表性论文**：
- AgentBench: Evaluating LLMs as Agents. 清华, ICLR 2024. `[核实]`
- SWE-bench: Can Language Models Resolve Real-World GitHub Issues? 2023. `[公认]`
- WebArena: A Realistic Web Environment for Building Autonomous Agents. 2023. `[公认]`
- GAIA: A Benchmark for General AI Assistants. Meta, 2023. `[公认]`
- LITMUS: 智能体行为越狱评测基准. NeurIPS 2026. `[核实]`

---

## 12. 通信与互操作协议（Communication & Interoperability）

**定义**：研究智能体之间、智能体与工具/UI 之间的标准化通信。这是 Agent 从"单机 demo"走向"生态互联"的基础设施层。

**核心研究点**：
- Agent ↔ Agent 通信（A2A）
- Agent ↔ 工具通信（MCP）
- Agent ↔ UI 通信（A2UI）
- 互操作性与协议治理

**代表性协议**：
- MCP: Model Context Protocol. Anthropic, 2024-11（已移交 Linux 基金会 Agentic AI 基金会）. `[核实]`
- A2A Protocol: Agent-to-Agent 开放标准. Google, arXiv:2504.08218, 2025. `[核实]`
- A2UI Protocol: Agent-to-UI 标准化. arXiv:2503.07666, 2025. `[核实]`

---

## 13. 知识工程、本体与 RAG（Knowledge Engineering, Ontology & RAG）

**定义**：研究如何为智能体构建结构化、可推理、可重用的知识底座，覆盖本体工程、知识图谱与检索增强生成。这是 Agent 从"语言合理"迈向"事实可信、逻辑正确"的桥梁——模型不是瓶颈，数据和知识底座才是。与老板专著《AI 落地工程》上卷"知识工程"主线及第7章"本体驱动"直接对应。

**核心研究点**：
- 本体工程（Ontology Engineering）：本体建模六要素、本体构建与维护、本体驱动让 AI 看懂企业业务
- 知识表示与推理（Knowledge Representation & Reasoning）：OWL/RDF、描述逻辑、本体推理
- 知识图谱（Knowledge Graph）：构建、表示、推理、与 LLM 互增强
- 神经符号推理（Neuro-Symbolic Reasoning）：LLM 生成 + 符号系统验证，可验证可解释推理链
- 场景图与空间本体（Scene Graph & Spatial Ontology）：3D/空间场景的结构化表示（与 3DGS/具身主线交汇）
- 检索增强生成（RAG）：朴素 RAG → 三路检索 + RRF → GraphRAG → 本体驱动 RAG
- LLM 辅助本体/知识图谱构建（LLM for KG construction）

**代表性论文与标准**：
- A Translation Approach to Portable Ontology Specifications. Gruber, Knowledge Acquisition, 1993.（本体经典定义）`[公认]`
- OWL Web Ontology Language: Reference / RDF. W3C 标准, McGuinness et al. `[公认]`
- A Survey on Knowledge Graphs: Representation, Acquisition, and Applications. Ji et al. IEEE TKDE, 2022. `[公认]`
- Reasoning over Knowledge Graphs: A Survey. Huang et al. IEEE TKDE. `[公认]`
- Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks. Lewis et al. NeurIPS 2020. `[公认]`
- Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection. 2023. `[公认]`
- GraphRAG. Microsoft, 2024. `[公认]`
- LLM Symbolic Reasoning 综述：迈向可验证、可解释、更可信的大模型推理范式. 2025-12. `[核实]`
- Neuro-Symbolic KG Construction via Ontology-grounded Correction. arXiv, 2026-10. `[核实]`

> 说明：本体在 LLM 时代有两条新研究路径值得深耕——(1) 用 LLM 自动构建本体/知识图谱，降低本体工程的人工成本；(2) 用本体为 LLM 提供结构化 ground 与可验证推理约束，缓解幻觉。

---

## 14. 人机协作与交互（Human-Agent Collaboration）

**定义**：研究人与智能体的协同模式，含可解释性、信任、对话管理与拟人化仿真。

**核心研究点**：
- 人机协同决策
- 可解释性与信任
- 对话管理
- 拟人化智能体仿真

**代表性论文**：
- Generative Agents: Interactive Simulacra of Human Behavior. Park et al. UIST 2023. `[公认]`
- Generative Agent Simulations of 1,000 People. Park et al. 2024. `[核实]`

---

## 15. Agent 工程化与生产部署（Agent Engineering & Deployment）

**定义**：研究从研究原型到生产系统的工程方法，含可靠性、可观测性、成本与落地方法论。

**核心研究点**：
- 执行框架（Harness）与可靠性
- 可观测性、成本控制、优雅降级
- 工程框架（LangChain / AutoGen / CrewAI / Letta）
- 行业落地方法论与 ROI 量化

**代表性文献**：
- Harness for Large Language Model Agents: A Survey. 2026. `[核实]`
- 工程框架：LangChain、AutoGen、CrewAI、Letta（开源生态，非论文）. `[公认]`

---

## 核心期刊与会议（投稿/检索入口）

### 顶级会议（Agent 论文主要去向）
| 会议 | 全称 | 领域侧重 |
|---|---|---|
| **NeurIPS** | Annual Conf. on Neural Information Processing Systems | Agent 推理/学习/多智能体主战场 |
| **ICLR** | Int'l Conf. on Learning Representations | Agent 架构/规划/工具学习 |
| **ICML** | Int'l Conf. on Machine Learning | Agent 学习/世界模型 |
| **ACL / EMNLP / NAACL** | 计算语言学会议 | 意图识别/记忆/对话/工具 |
| **AAAI** | Association for the Advancement of AI | 记忆/多智能体（MemoryBank 即此） |
| **CVPR / ICCV / ECCV** | 计算机视觉会议 | 具身/多模态/世界模型 |
| **UIST / SIGCHI** | 人机交互会议 | 人机协作/拟人化（Generative Agents 即此） |
| **AAMAS** | Int'l Conf. on Autonomous Agents and Multi-Agent Systems | **Agent 专门会议**，MAS 首选 |
| **IJCAI** | Int'l Joint Conf. on AI | Agent 综合方向 |

### 核心期刊
| 期刊 | 全称 | 侧重 |
|---|---|---|
| **JAIR** | Journal of Artificial Intelligence Research | AI 综合综述 |
| **AIJ** | Artificial Intelligence（Elsevier） | AI 基础理论 |
| **TPAMI** | IEEE Trans. on Pattern Analysis and Machine Intelligence | 多模态/具身/视觉 |
| **TIST** | ACM Trans. on Intelligent Systems and Technology | 智能系统/Agent 应用 |
| **JAAMAS** | Journal of Autonomous Agents and Multi-Agent Systems | **Agent 专门期刊** |
| **Neural Networks** | Elsevier | 世界模型/学习 |
| **Pattern Recognition** | Elsevier | 感知/具身 |

### 中文核心期刊（老板常投方向）
- 计算机学报、软件学报、计算机研究与发展、自动化学报、图形学学报、中国图象图形学报（3DGS/具身/Agent 交叉）

---

## 引用核实与使用约定

1. **`[核实]`**：2026-10-28 经多轮检索确认 venue/官方来源，可直接引用，仍建议附 arXiv/DOI 链接核对。
2. **`[公认]`**：学界长期公认的标志性工作，venue 信息稳定；正式投稿前以 arXiv/会议官网最终版本核对页码与作者顺序。
3. 本图谱不包含任何编造引用；凡无法核实的论文一律不列入。
4. 项目 `data/methods.json` 已收录 280 条 Agent 方法（12 类别），与本图谱互补：图谱给"研究方向骨架"，方法库给"方法实例"。
5. 检索受限说明：本轮基于公开网络检索，部分 2026 年最新工作可能未覆盖，后续可通过 `scripts/` 自动化扫描补充。

