
<div align="center">

# Awesome Agent Engineering

### The Most Comprehensive AI Agent Knowledge Hub — 518 Entries, 4 Domains, Auto-Updated Daily

**From research papers to production deployment. From startup ideas to industry playbooks. One repo, the entire Agent ecosystem.**

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Methods](https://img.shields.io/badge/Methods-280-9cf.svg)](data/methods.json)
[![Frameworks](https://img.shields.io/badge/Frameworks-52-green.svg)](data/frameworks.json)
[![Industries](https://img.shields.io/badge/Industries-107-orange.svg)](data/industries.json)
[![Startups](https://img.shields.io/badge/Startups-47-red.svg)](data/startups.json)
[![Benchmarks](https://img.shields.io/badge/Benchmarks-32-purple.svg)](data/benchmarks.json)
[![Auto-Update](https://img.shields.io/badge/Auto_Update-Daily-brightgreen.svg)](reports/arxiv-daily/)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen.svg)](CONTRIBUTING.md)

[English](README.md) | [中文](README_CN.md)

</div>

<details>
<summary><b>Table of Contents</b></summary>

- [Why This Repo?](#why-this-repo)
- [The Four Domains](#the-four-domains)
- [Knowledge Base at a Glance](#knowledge-base-at-a-glance)
- [Auto-Update Pipeline](#auto-update-pipeline)
- [Quick Start](#quick-start)
- [Research — Academic Methods](#research--academic-methods)
- [Industry — Real-World Applications](#industry--real-world-applications)
- [Startup — Innovation & Business](#startup--innovation--business)
- [Deployment — Frameworks & Infrastructure](#deployment--frameworks--infrastructure)
- [Benchmarks — Evaluation](#benchmarks--evaluation)
- [What's New](#whats-new)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)

</details>

## Why This Repo?

Other awesome lists give you paper titles. **We give you a living knowledge base that updates itself.**

The Agent ecosystem moves fast — new papers daily, new frameworks weekly, new startups monthly. Static lists go stale in weeks. This repo is different:

| What You Need | Static Lists | This Repo |
|---------------|-------------|-----------|
| Latest Agent papers | Last updated 3 months ago | **Daily arXiv scan** — 17 query families, auto-discovered |
| Compare frameworks | Open 10 tabs | 52 frameworks with stars, license, language, one-line description |
| Find industry cases | Blog posts | 107 real deployments across 15+ industries, with status and org |
| Track startups | Crunchbase subscription | 47 funded companies with funding, category, and description |
| Pick a benchmark | Guess | 32 benchmarks with domain, venue, and what they test |
| Keep it current | Manual PRs | **GitHub Actions CI** runs daily, commits automatically |

**518 verified entries** across 5 knowledge bases, each with an evidence trail. No fabricated names, no dead links, no marketing fluff.

## The Four Domains

```
┌─────────────────────────────────────────────────────────────┐
│                  AWESOME AGENT ENGINEERING                    │
│                                                              │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐    │
│  │ RESEARCH │  │ INDUSTRY │  │ STARTUP  │  │DEPLOYMENT│    │
│  │          │  │          │  │          │  │          │    │
│  │ 280      │  │ 107      │  │ 47       │  │ 52       │    │
│  │ methods  │  │ cases    │  │ companies│  │frameworks│    │
│  │ 12 cats  │  │ 15 doms  │  │ 12 cats  │  │ + 32     │    │
│  │          │  │          │  │          │  │benchmarks│    │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘    │
│       │             │             │             │           │
│       └─────────────┴─────────────┴─────────────┘           │
│                         │                                    │
│                  ┌──────┴──────┐                             │
│                  │  AUTO-UPDATE │                             │
│                  │   PIPELINE   │                             │
│                  │             │                             │
│                  │ Daily arXiv │                             │
│                  │ Weekly GH   │                             │
│                  │ Weekly HF   │                             │
│                  └─────────────┘                             │
└─────────────────────────────────────────────────────────────┘
```

## Knowledge Base at a Glance

| Knowledge Base | Count | Source File | Description |
|----------------|-------|-------------|-------------|
| **Methods** | 280 | `data/methods.json` | Academic Agent papers — 12 categories from Foundation to Safety |
| **Frameworks** | 52 | `data/frameworks.json` | OSS agent frameworks — orchestration, memory, tools, observability |
| **Industries** | 107 | `data/industries.json` | Real-world deployments — 15 domains from Finance to Energy |
| **Startups** | 47 | `data/startups.json` | Funded companies — 12 categories from Foundation Models to Robotics |
| **Benchmarks** | 32 | `data/benchmarks.json` | Evaluation suites — SWE-bench, GAIA, WebArena, OSWorld, and more |

**Every entry is machine-readable JSON** — not just markdown tables. Build tools, dashboards, and agents that consume this knowledge directly.

## Auto-Update Pipeline

This repo never goes stale. Three automated scans keep it current:

| Scan | Frequency | Sources | Output |
|------|-----------|---------|--------|
| **arXiv Discovery** | Daily (UTC 06:00) | 8 arXiv query families covering the full Agent landscape | `reports/arxiv-daily/YYYY-MM-DD.md` |
| **GitHub Trending** | Weekly (Mon UTC 06:00) | GitHub Search API — 7 agent-related queries, stars > 50 | `reports/weekly-trending/YYYY-MM-DD.md` |
| **HuggingFace Trending** | Weekly (Mon UTC 06:00) | HF API — agent/tool-use/VLA/RAG models sorted by weekly likes | `reports/weekly-trending/YYYY-MM-DD.md` |

All scans run via **GitHub Actions CI** and commit reports automatically. Candidates are flagged for review before admission to the knowledge base — no auto-admission without verification.

```bash
# Run scans manually
python scripts/daily_arxiv_scan.py 3        # scan last 3 days of arXiv
python scripts/weekly_industry_scan.py      # scan GitHub + HuggingFace trending
python scripts/validate_kb.py               # validate all 5 knowledge bases
```

## Quick Start

```bash
git clone https://github.com/your-username/Awesome-Agent-Engineering.git
cd Awesome-Agent-Engineering

# Explore the knowledge bases
cat data/methods.json | python -m json.tool | head -50

# Find all web/GUI agent methods
python -c "
import json
data = json.load(open('data/methods.json'))
for m in data['methods']:
    if 'Web & GUI' in m['category']:
        print(f\"  {m['name']} ({m['venue']}) — {m['desc'][:80]}\")
"

# Check what's trending this week
cat reports/weekly-trending/latest.json | python -m json.tool
```

## Research — Academic Methods

**280 verified methods** across 12 categories, covering the full Agent research stack:

| Category | Count | Key Methods |
|----------|-------|-------------|
| Foundation & Architecture | 24 | ReAct, Reflexion, AutoGPT, Toolformer, Voyager, MetaGPT, AutoGen |
| Planning & Reasoning | 17 | Chain-of-Thought, Tree of Thoughts, LLM+P, Self-Refine, AdaPlanner |
| Tool Use & Function Calling | 13 | Gorilla, ToolLLM, ToolkenGPT, AnyTool, ToolACE |
| Memory & Context | 12 | MemGPT, Mem0, Letta, A-MEM, CoALA, Infini-attention |
| Multi-Agent Systems | 17 | ChatDev, AgentVerse, MoA, AgentScope, EvoAgent, Camel-AI OWL |
| Code & Software Agents | 25 | SWE-agent, Devin, OpenHands, Agentless, SWE-bench, CodeAct |
| Embodied & Robotics Agents | 22 | RT-1/2, OpenVLA, π0, GR00T N1, RDT-1B, DiffusionPolicy |
| World Models & Simulation | 11 | DreamerV3, Genie, DIAMOND, Sora, Oasis, GameNGen |
| Web & GUI Agents | 25 | Mind2Web, WebArena, OSWorld, Browser Use, OmniParser, SeeClick |
| Knowledge & RAG Agents | 15 | RAG, Self-RAG, GraphRAG, RAPTOR, LightRAG, MemoRAG |
| Safety, Alignment & Evaluation | 17 | GAIA, AgentBench, ToolEmu, InjecAgent, Agent-SafetyBench |
| Agent Frameworks & Infrastructure | 18 | LangChain, LangGraph, AutoGen, Swarm, Smolagents, A2A-Protocol |

<details>
<summary><b>Browse all 280 methods →</b></summary>

See [`data/methods.json`](data/methods.json) for the full machine-readable database, or [`references/agent-research-areas.md`](references/agent-research-areas.md) for a browsable markdown table.

</details>

<details>
<summary><b>Research map & expert team →</b></summary>

- **[`references/agent-research-areas.md`](references/agent-research-areas.md)** — 16 core research areas of AI/Agent (intent recognition, memory, planning, tool use, world models, knowledge engineering & ontology, etc.) with representative papers and venue verification
- **[`references/agent-research-expert-team.md`](references/agent-research-expert-team.md)** — Research expert team for AI/Agent papers: 9 roles (R1–R9) covering idea evaluation, experiment design, writing, review, and venue check; with verified journal papers and a journal/conference submission cheat sheet

</details>

## Industry — Real-World Applications

**107 real-world deployments** across 15+ industries — not demos, not concepts, but production systems:

| Domain | Count | Highlights |
|--------|-------|------------|
| Finance | 11 | JPMorgan COiN, Klarna AI (2.3M conversations/month), BloombergGPT |
| Healthcare | 12 | Nuance DAX, Epic AI Hub, Hippocratic AI, Nabla Copilot |
| Government | 8 | Singapore GovGPT, UK GOV.UK Chat, 国数通超级智能体平台 |
| Manufacturing | 8 | Siemens Industrial Copilot, NVIDIA Omniverse, BMW AI Production |
| Legal | 7 | Harvey AI, Lexis+ AI, Casetext CoCounsel, Robin AI |
| Education | 8 | Khanmigo, Duolingo Max, Squirrel AI, BYJU'S |
| Customer Service | 8 | Salesforce Einstein, Zendesk AI, Intercom Fin, Sierra AI |
| RPA & Automation | 6 | UiPath AI Center, Automation Anywhere, Microsoft Copilot Studio |
| Retail & E-commerce | 5 | Amazon Rufus, Shopify Sidekick, Alibaba Tongyi Qianwen |
| Research & Development | 6 | DeepMind AlphaFold, Sakana AI Scientist, OpenAI o-series |
| Human Resources | 4 | Workday AI, Eightfold AI, Paradox Olivia |
| IT Operations | 5 | PagerDuty AIOps, Datadog AI, New Relic AI |
| Logistics | 5 | Maersk AI Route, Flexport AI, Amazon Logistics, DHL AI |
| Real Estate | 4 | Zillow AI, Redfin AI, Compass AI, JLL AI |
| Media & Content | 6 | Adobe Firefly, Jasper AI, Synthesia, Canva Magic Studio |
| Telecommunications | 5 | 中国电信 TeleAgent, SK Telecom, BT, AT&T, Deutsche Telekom |
| Energy | 3 | Google DeepMind Grid (40% energy reduction), Shell, Enel |

<details>
<summary><b>Browse all 107 industry cases →</b></summary>

See [`data/industries.json`](data/industries.json) for the full database.

</details>

## Startup — Innovation & Business

**47 funded companies** building the Agent economy — from foundation models to robotics:

| Category | Count | Notable Companies |
|----------|-------|-------------------|
| Foundation Models | 7 | OpenAI, Anthropic, xAI, Mistral AI, DeepSeek, Cohere, AI21 Labs |
| Code Agents | 7 | Cognition (Devin), Anysphere (Cursor), Magic.dev, Codeium, Replit |
| Customer Service Agents | 4 | Sierra AI, Decagon, Forethought, Aisera |
| Action Agents | 3 | Adept AI, MultiOn AI, Imbue |
| Agent Memory | 3 | Mem0, Zep, Letta |
| Agent Infrastructure | 3 | LangChain, CrewAI, LlamaIndex |
| Robotics Agents | 5 | Physical Intelligence, Skild AI, Figure AI, 1X, Sanctuary AI |
| Autonomous Agents | 2 | Wayve, Waabi |
| Character Agents | 3 | Inworld AI, Replika, Character.AI |
| Healthcare Agents | 2 | Hippocratic AI, Glass Health |
| Legal Agents | 1 | Harvey |
| Web Agents | 2 | Browser Use, Crawl4AI |

See [`data/startups.json`](data/startups.json) for funding details and descriptions.

## Deployment — Frameworks & Infrastructure

**52 open-source frameworks** for building, deploying, and monitoring Agent systems:

| Layer | Frameworks |
|-------|-----------|
| **Orchestration** | LangChain, LangGraph, AutoGen, CrewAI, Semantic Kernel, DSPy, Swarm, Smolagents |
| **RAG & Data** | LlamaIndex, Haystack, RAGFlow, Dify, FastGPT, AnythingLLM, Unstructured |
| **Coding Agents** | OpenHands, SWE-agent, Aider, Cursor, Replit |
| **Web Automation** | Browser Use, Playwright, Crawl4AI, Firecrawl, SearXNG, Tavily |
| **Memory** | Mem0, Letta, Zep |
| **Tools & MCP** | MCP, MCP Server Registry, Composio, CrewAI Tools |
| **Serving** | vLLM, Ollama, LiteLLM |
| **Observability** | Phoenix, LangSmith, Helicone, Braintrust |
| **Safety** | Guardrails AI, NeMo Guardrails, Llama Guard |
| **UI** | OpenWebUI, LibreChat, LobeChat, Flowise, n8n |

See [`data/frameworks.json`](data/frameworks.json) for stars, license, and language details.

## Benchmarks — Evaluation

**32 benchmarks** for evaluating Agent capabilities across domains:

| Domain | Benchmarks |
|--------|-----------|
| General Agent | GAIA, AgentBench, MINT-Bench, AgentBench-Multi |
| Software Engineering | SWE-bench, SWE-bench Verified, HumanEval, MBPP, LiveCodeBench, BigCodeBench, MLE-Bench |
| Web Agent | Mind2Web, WebArena, OSWorld, WebShop, VisualWebArena, WorkArena, GUI-World |
| Tool Use | ToolBench, API-Bank, Tau-Bench |
| Embodied Agent | VLABench, CALVIN, RoboCasa, LIBERO, ALFRED |
| Safety | Agent-SafetyBench, AdvBench, HarmBench, InjecAgent |
| Research Agent | MLAgentBench, DS-1000, TheAgentCompany |

See [`data/benchmarks.json`](data/benchmarks.json) for venue and URL details.

## What's New

### v0.1.0 — Initial Release (Oct 2026)

**518 verified entries** across 5 knowledge bases:

- **280 academic methods** in 12 categories — from ReAct (2022) to GR00T N1 and π0.5 (2025)
- **52 open-source frameworks** — orchestration, RAG, memory, tools, serving, observability
- **107 industry deployments** across 17 domains — production systems from JPMorgan to 国数通
- **47 funded startups** — $200B+ in combined funding, from foundation models to robotics
- **32 evaluation benchmarks** — SWE-bench, GAIA, WebArena, OSWorld, and beyond

**Auto-update pipeline operational:**
- Daily arXiv scan (8 query families, Agent-paper discovery)
- Weekly GitHub Trending scan (7 agent-related queries)
- Weekly HuggingFace Trending scan (agent/tool-use/VLA models)
- Knowledge base validation CI (5 JSON files, field + count consistency)

See [`changelog/`](changelog/) for the full history.

## Roadmap

- [x] **Phase 1** — Knowledge base skeleton + 518 seed entries + auto-update scripts
- [ ] **Phase 2** — Interactive web explorer (search, filter, sort 518 entries)
- [x] **Phase 2** — AI-powered Skills: agent-research-pipeline (full 8-stage research lifecycle) → [`skills/agent-research-pipeline/`](skills/agent-research-pipeline/)
- [ ] **Phase 3** — Online book: "Agent Engineering — From Research to Production"
- [ ] **Phase 3** — MCP server (let any AI agent consume this knowledge base)
- [ ] **Phase 3** — Community contributions (PR-based entry submission with auto-validation)

## Companion Book

This repo also ships the companion book **《AI 落地工程：从数据治理到超级智能体》** (*AI Deployment Engineering: From Data Governance to Superintelligent Agents*) as a git submodule, mounted at [`deployment-book/`](deployment-book/).

It is the methodology backbone behind the knowledge base — a two-volume, 16-chapter work (~350K Chinese characters) covering the full AI-landing stack:

```
Data Governance → Knowledge Engineering → Agent Engineering → FDE → Industry Practice
```

- **Volume I (Data & Knowledge Foundation, Ch.1–8)**: the AI adoption gap, data governance maturity, RAG engineering, LLM Wiki, **ontology-driven AI (Ch.7)**, GraphRAG hybrid architectures
- **Volume II (Agents & Delivery, Ch.9–16)**: agent architecture, multi-agent collaboration, **superintelligent agents (Ch.11)**, FDE methodology, deployment & operations, government/finance/manufacturing playbooks

The book's "Knowledge Engineering" arc (ontology → RAG → GraphRAG) directly informs the [`references/agent-research-areas.md`](references/agent-research-areas.md) research map's Section 13 (Knowledge Engineering, Ontology & RAG).

```bash
# Clone with the submodule
git clone --recurse-submodules https://github.com/jaccen2007/Awesome-Agent-Engineering.git

# If already cloned, fetch the submodule
git submodule update --init --recursive
```

> The book repo is independently maintained at [jaccen/AI-deployment-engineering](https://github.com/jaccen/AI-deployment-engineering); online reading is at [jaccen.github.io/AI-deployment-engineering](https://jaccen.github.io/AI-deployment-engineering/).

## AI Skills

This repo ships an AI skill for the full Agent research lifecycle:

### agent-research-pipeline

**Location:** [`skills/agent-research-pipeline/`](skills/agent-research-pipeline/)

A one-stop research assistant for AI/Agent papers, covering the full 8-stage pipeline:

| Stage | What it does |
|---|---|
| 1. Idea Evaluation | Five-dimension assessment + fatal-flaw audit + feasibility check |
| 2. Skeleton | Seven-cell thinking template + four-point self-consistency check |
| 3. Literature | Multi-source search (arXiv/Scholar/GitHub/HF) + knowledge-base query + citation verification |
| 4. Figures & Tables | Three core figure design + tool selection + quality checklist |
| 5. Experiments | Hypothesis → experiment matrix → metrics → benchmarks → ablation design |
| 6. Data Analysis | Statistical reporting + visualization + causal attribution |
| 7a. Polishing | Grammar + terminology + AI-tone removal + claim calibration |
| 7b. Self-Review | Three-role cross-review (reviewer/researcher/expert) + 33 rejection patterns |
| 8. Rebuttal | Per-comment response strategy + cover letter + marked manuscript |

**Knowledge base integration:** queries `data/methods.json` (280), `data/frameworks.json` (52), `data/benchmarks.json` (32), `data/papers.json` (120 papers), and `references/agent-research-areas.md` (16 areas) to ground every answer in verified data.

**Bundled references:**
- [`references/paper-database.md`](skills/agent-research-pipeline/references/paper-database.md) — 120 verified papers across 16 sub-areas (including 40+ new 2026 papers with arXiv IDs spot-checked; NeurIPS 2026 EvoMemBench/LITMUS, ICLR 2026 LightMem, AAMAS 2026 μACP, and more)
- [`references/venues.md`](skills/agent-research-pipeline/references/venues.md) — 15 top conferences + 20 journals with CCF ranking, page limits, deadlines, and review preferences
- [`references/experiment-template.md`](skills/agent-research-pipeline/references/experiment-template.md) — Fill-in experiment template (contribution-experiment mapping, ablation design, multi-seed statistics, negative results, pre-submission checklist)
- [`data/papers.json`](data/papers.json) — Machine-readable paper database (120 papers with arXiv ID/venue/verification status/categories)

**Editor integration:** [`CLAUDE.md`](CLAUDE.md) (Claude Code / generic AI project instructions) and [`.cursor/rules/agent-research.mdc`](.cursor/rules/agent-research.mdc) (Cursor auto-activate rule) are configured to load this skill automatically when editing paper-related files in VS Code/Cursor.

## Contributing

We welcome contributions! See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the full guide.

**Key principle:** Every entry must be verifiable. We follow an evidence protocol (A1–A5) — method names must be self-stated, arXiv IDs must resolve, GitHub URLs must be live. No fabrication.

```bash
# Validate your changes before submitting
python scripts/validate_kb.py
```

## License

[Apache License 2.0](LICENSE) — free for commercial and non-commercial use.

---

<div align="center">

**Star this repo if it helped you. Watch it to get daily Agent updates.**

Built with the same philosophy as [Awesome-Gaussian-Skills](https://github.com/jaccen/Awesome-Gaussian-Skills) — living knowledge bases, not static lists.

</div>
