
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
