
<div align="center">

# Awesome Agent Engineering

### 最全面的 AI Agent 知识中枢 — 518 条目，四大板块，每日自动更新

**从研究论文到生产部署，从创业项目到行业落地。一个仓库，整个 Agent 生态。**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![方法数](https://img.shields.io/badge/方法-280-9cf.svg)](data/methods.json)
[![框架数](https://img.shields.io/badge/框架-52-green.svg)](data/frameworks.json)
[![行业案例](https://img.shields.io/badge/行业案例-107-orange.svg)](data/industries.json)
[![创业公司](https://img.shields.io/badge/创业公司-47-red.svg)](data/startups.json)
[![基准测试](https://img.shields.io/badge/基准测试-32-purple.svg)](data/benchmarks.json)
[![自动更新](https://img.shields.io/badge/自动更新-每日-brightgreen.svg)](reports/arxiv-daily/)
[![欢迎PR](https://img.shields.io/badge/欢迎PR-Contributing-brightgreen.svg)](CONTRIBUTING.md)

[English](README.md) | [中文](README_CN.md)

</div>

## 为什么是这个仓库？

其他 awesome-list 只给你论文标题。**我们给你一个会自己更新的活知识库。**

Agent 生态发展极快——每天都有新论文，每周都有新框架，每月都有新创业公司。静态列表几周就过时了。本仓库不同：

| 你的需求 | 静态列表 | 本仓库 |
|----------|---------|--------|
| 最新 Agent 论文 | 三个月前最后更新 | **每日 arXiv 扫描** — 8 个查询族自动发现 |
| 对比框架 | 开 10 个标签页 | 52 个框架，含 star 数、许可证、语言、一句话描述 |
| 找行业案例 | 博客文章 | 107 个真实部署，覆盖 17+ 行业，含状态和组织 |
| 追踪创业公司 | Crunchbase 订阅 | 47 家融资公司，含融资额、分类和描述 |
| 选基准测试 | 靠猜 | 32 个基准，含领域、会议和测试内容 |
| 保持最新 | 手动提 PR | **GitHub Actions CI** 每日运行，自动提交 |

**518 个可验证条目**，横跨 5 个知识库，每个条目都有证据链。不编造名称，不放死链，不写营销话术。

## 四大板块

| 板块 | 条目数 | 内容 |
|------|--------|------|
| **学术研究** | 280 | Agent 论文方法库，12 个类别，从基础架构到安全评估 |
| **行业应用** | 107 | 真实生产部署，17 个领域，从金融到能源 |
| **创意创业** | 47 | 融资公司库，12 个分类，从基础模型到机器人 |
| **产业落地** | 52 + 32 | 开源框架 + 评测基准，从编排到可观测性 |

## 知识库一览

| 知识库 | 数量 | 数据文件 | 说明 |
|--------|------|----------|------|
| **方法库** | 280 | `data/methods.json` | 学术 Agent 论文 — 12 个类别 |
| **框架库** | 52 | `data/frameworks.json` | 开源 Agent 框架 — 编排/记忆/工具/可观测性 |
| **行业库** | 107 | `data/industries.json` | 真实部署案例 — 17 个领域 |
| **创业库** | 47 | `data/startups.json` | 融资公司 — 12 个分类 |
| **基准库** | 32 | `data/benchmarks.json` | 评测基准 — SWE-bench/GAIA/WebArena 等 |

**所有条目均为机器可读 JSON**，而非单纯的 Markdown 表格。可以直接构建工具、仪表盘和 Agent 来消费这些知识。

## 自动更新流水线

本仓库永不过时。三套自动扫描保持持续更新：

| 扫描 | 频率 | 数据源 | 输出 |
|------|------|--------|------|
| **arXiv 发现** | 每日（UTC 06:00） | 8 个 arXiv 查询族，覆盖 Agent 全景 | `reports/arxiv-daily/` |
| **GitHub 趋势** | 每周一（UTC 06:00） | GitHub Search API，7 个 Agent 相关查询 | `reports/weekly-trending/` |
| **HuggingFace 趋势** | 每周一（UTC 06:00） | HF API，按周点赞排序的 Agent/VLA/RAG 模型 | `reports/weekly-trending/` |

所有扫描通过 **GitHub Actions CI** 运行，自动提交报告。候选条目需审核后方可纳入知识库——不自动收录未经验证的条目。

```bash
# 手动运行扫描
python scripts/daily_arxiv_scan.py 3        # 扫描最近 3 天的 arXiv
python scripts/weekly_industry_scan.py      # 扫描 GitHub + HuggingFace 趋势
python scripts/validate_kb.py               # 校验全部 5 个知识库
```

## 快速开始

```bash
git clone https://github.com/your-username/Awesome-Agent-Engineering.git
cd Awesome-Agent-Engineering

# 查看知识库
python -c "
import json
data = json.load(open('data/methods.json'))
for m in data['methods']:
    if 'Web & GUI' in m['category']:
        print(f\"  {m['name']} ({m['venue']}) — {m['desc'][:80]}\")
"

# 查看本周趋势
cat reports/weekly-trending/latest.json | python -m json.tool
```

## 学术研究 — 方法库

**280 个已验证方法**，12 个类别，覆盖 Agent 研究全栈：

| 类别 | 数量 | 代表方法 |
|------|------|----------|
| 基础架构 | 24 | ReAct、Reflexion、AutoGPT、Toolformer、Voyager、MetaGPT、AutoGen |
| 规划与推理 | 17 | Chain-of-Thought、Tree of Thoughts、LLM+P、Self-Refine |
| 工具使用 | 13 | Gorilla、ToolLLM、ToolkenGPT、AnyTool |
| 记忆与上下文 | 12 | MemGPT、Mem0、Letta、A-MEM、CoALA |
| 多智能体系统 | 17 | ChatDev、AgentVerse、MoA、AgentScope、Camel-AI OWL |
| 代码与软件 Agent | 25 | SWE-agent、Devin、OpenHands、Agentless、SWE-bench |
| 具身与机器人 Agent | 22 | RT-1/2、OpenVLA、π0、GR00T N1、RDT-1B |
| 世界模型与仿真 | 11 | DreamerV3、Genie、DIAMOND、Sora、Oasis |
| Web 与 GUI Agent | 25 | Mind2Web、WebArena、OSWorld、Browser Use、OmniParser |
| 知识与 RAG Agent | 15 | RAG、Self-RAG、GraphRAG、RAPTOR、LightRAG |
| 安全对齐与评估 | 17 | GAIA、AgentBench、ToolEmu、InjecAgent |
| 框架与基础设施 | 18 | LangChain、LangGraph、AutoGen、Swarm、Smolagents |

完整数据见 [`data/methods.json`](data/methods.json)。

<details>
<summary><b>研究图谱与科研专家团 →</b></summary>

- **[`references/agent-research-areas.md`](references/agent-research-areas.md)** — AI/Agent 16 个核心研究领域（意图识别、记忆、规划、工具使用、世界模型、知识工程与本体等），含代表性论文与 venue 核实
- **[`references/agent-research-expert-team.md`](references/agent-research-expert-team.md)** — AI/Agent 论文科研专家团：9 角色（R1-R9）覆盖选题评估、实验设计、写作、审稿、投稿检查；含已核实期刊论文与投稿速查表

</details>

## 行业应用 — 真实部署

**107 个真实生产系统**，覆盖 17+ 行业——不是 demo，不是概念，是生产级系统：

| 领域 | 数量 | 亮点 |
|------|------|------|
| 金融 | 11 | 摩根大通 COiN、Klarna AI（月230万对话）、彭博 BloombergGPT |
| 医疗 | 12 | Nuance DAX、Epic AI Hub、Hippocratic AI、Nabla |
| 政务 | 8 | 新加坡 GovGPT、英国 GOV.UK Chat、国数通超级智能体平台 |
| 制造 | 8 | 西门子 Industrial Copilot、NVIDIA Omniverse、宝马 AI |
| 法律 | 7 | Harvey AI、Lexis+ AI、Casetext CoCounsel |
| 教育 | 8 | Khanmigo、Duolingo Max、松鼠 AI |
| 客服 | 8 | Salesforce Einstein、Zendesk AI、Sierra AI |
| RPA | 6 | UiPath AI Center、Automation Anywhere、微软 Copilot Studio |
| 零售电商 | 5 | Amazon Rufus、Shopify Sidekick、阿里通义千问 |
| 研发 | 6 | DeepMind AlphaFold、Sakana AI Scientist、OpenAI o 系列 |
| 人力 | 4 | Workday AI、Eightfold AI |
| IT 运维 | 5 | PagerDuty AIOps、Datadog AI、Splunk AI |
| 物流 | 5 | 马士基 AI、Flexport AI、DHL AI |
| 房地产 | 4 | Zillow AI、Redfin AI、Compass AI |
| 媒体内容 | 6 | Adobe Firefly、Jasper AI、Synthesia、Canva |
| 电信 | 5 | 中国电信 TeleAgent、SK Telecom、BT、AT&T |
| 能源 | 3 | Google DeepMind 电网（降耗40%）、壳牌、Enel |

完整数据见 [`data/industries.json`](data/industries.json)。

## 创意创业 — 创业公司库

**47 家融资公司**，构建 Agent 经济——从基础模型到机器人：

| 分类 | 数量 | 代表公司 |
|------|------|----------|
| 基础模型 | 7 | OpenAI、Anthropic、xAI、Mistral AI、DeepSeek |
| 代码 Agent | 7 | Cognition（Devin）、Anysphere（Cursor）、Magic.dev |
| 客服 Agent | 4 | Sierra AI、Decagon、Forethought |
| 行动 Agent | 3 | Adept AI、MultiOn AI、Imbue |
| Agent 记忆 | 3 | Mem0、Zep、Letta |
| 基础设施 | 3 | LangChain、CrewAI、LlamaIndex |
| 机器人 Agent | 5 | Physical Intelligence、Figure AI、1X |
| 自动驾驶 | 2 | Wayve、Waabi |
| 角色 Agent | 3 | Inworld AI、Replika、Character.AI |

完整数据见 [`data/startups.json`](data/startups.json)。

## 产业落地 — 框架与基准

**52 个开源框架** + **32 个评测基准**：

| 层级 | 框架 |
|------|------|
| 编排 | LangChain、LangGraph、AutoGen、CrewAI、DSPy、Swarm |
| RAG | LlamaIndex、Haystack、RAGFlow、Dify、AnythingLLM |
| 代码 Agent | OpenHands、SWE-agent、Aider |
| Web 自动化 | Browser Use、Playwright、Crawl4AI、Firecrawl |
| 记忆 | Mem0、Letta、Zep |
| 工具与 MCP | MCP、Composio |
| 推理服务 | vLLM、Ollama、LiteLLM |
| 可观测性 | Phoenix、LangSmith、Helicone |
| 安全 | Guardrails AI、NeMo Guardrails、Llama Guard |
| 界面 | OpenWebUI、LibreChat、LobeChat |

## 配套专著

本仓库以 git submodule 形式挂载了配套专著 **《AI 落地工程：从数据治理到超级智能体》**，路径为 [`deployment-book/`](deployment-book/)。

它是知识库背后的方法论主轴——双卷 16 章（约 35 万字），覆盖 AI 落地全栈：

```
数据治理 → 知识工程 → 智能体工程 → FDE → 产业实战
```

- **上卷《数据与知识底座》（第 1–8 章）**：AI 落地鸿沟、数据治理成熟度、RAG 工程化、LLM Wiki、**本体驱动（第 7 章）**、GraphRAG 混合架构
- **下卷《智能体与落地交付》（第 9–16 章）**：Agent 架构设计、多 Agent 协作、**超级智能体（第 11 章）**、FDE 方法论、部署与运营、政务/金融/制造实战

专著的"知识工程"主线（本体 → RAG → GraphRAG）直接对应 [`references/agent-research-areas.md`](references/agent-research-areas.md) 研究图谱第 13 节（知识工程、本体与 RAG）。

```bash
# 克隆时一并拉取子模块
git clone --recurse-submodules https://github.com/jaccen2007/Awesome-Agent-Engineering.git

# 已克隆的仓库，单独拉取子模块
git submodule update --init --recursive
```

> 专著仓库独立维护于 [jaccen/AI-deployment-engineering](https://github.com/jaccen/AI-deployment-engineering)，在线阅读地址 [jaccen.github.io/AI-deployment-engineering](https://jaccen.github.io/AI-deployment-engineering/)。

## AI 技能

本仓库内置一个覆盖 Agent 科研全流程的 AI 技能：

### agent-research-pipeline

**位置：** [`skills/agent-research-pipeline/`](skills/agent-research-pipeline/)

面向 AI/Agent 论文的一站式科研辅导，覆盖全生命周期 8 阶段：

| 阶段 | 职责 |
|---|---|
| 1. 选题评估 | 五维评估 + 致命伤审计 + 可行性检查 |
| 2. 论文骨架 | 思维模板七格 + 四点自洽检查 |
| 3. 文献检索 | 多源检索（arXiv/Scholar/GitHub/HF）+ 知识库查询 + 引用核实 |
| 4. 绘图制表 | 三核心图设计 + 工具选型 + 质量检查 |
| 5. 实验设计 | 假设→实验矩阵→指标→基准→消融设计 |
| 6. 数据分析 | 统计报告 + 可视化 + 归因分析 |
| 7a. 润色 | 语法 + 术语 + 去AI味 + claim校准 |
| 7b. 审稿自查 | 三身份交叉审查 + 33条拒稿规律 |
| 8. 返修改稿 | 逐条回复策略 + Cover Letter + Marked Manuscript |

**知识库挂接：** 查询 `data/methods.json`（280）、`data/frameworks.json`（52）、`data/benchmarks.json`（32）及 `references/agent-research-areas.md`（16 领域），确保每个回答有据可查。

**内置参考文件：**
- [`references/paper-database.md`](skills/agent-research-pipeline/references/paper-database.md) — 16 子领域 80+ 篇已核实论文（含 NeurIPS 2026 EvoMemBench/LITMUS/HarnessPro、OSWorld、SWE-bench 等）
- [`references/venues.md`](skills/agent-research-pipeline/references/venues.md) — 15 顶会 + 20 期刊，含 CCF 分级、页数、截稿、审稿偏好

## 贡献

欢迎贡献！详见 [`CONTRIBUTING.md`](CONTRIBUTING.md)。

**核心原则：** 每个条目必须可验证。我们遵循证据协议（A1–A5）——方法名必须是论文自述的，arXiv ID 必须可访问，GitHub 链接必须有效。不编造。

## 许可证

[Apache License 2.0](LICENSE) — 商业和非商业均可免费使用。

---

<div align="center">

**如果这个仓库对你有帮助，请点个 Star。Watch 可获取每日 Agent 更新。**

与 [Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) 同一理念——活的知识库，而非静态列表。

</div>
