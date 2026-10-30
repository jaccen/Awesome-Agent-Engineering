# Reviewed additions — 2026-10-30

Added 24 papers, 7 benchmark records and 4 frameworks. Each of the 24 papers now carries its official arXiv abstract (`abstract` field) and a one-line factual Chinese summary (`summary_zh` field), both sourced from the arXiv API metadata retrieved by the repo's daily scan. Benchmark records refer to benchmarks announced in seven of the added papers; these are record counts, not distinct project counts. Framework records are four open-source projects verified via their official GitHub repositories.

arXiv records are public preprints, not confirmed peer-reviewed publications. Review establishes source metadata and topical relevance; reported performance has not been reproduced. Official API evidence was retrieved at 2026-10-30T12:50:00+00:00.

Sources this round: the repo's own daily arXiv scan (`scripts/daily_arxiv_scan.py`, 8 query families, 3-day window, 81 candidates after deduplication against 246 known arXiv IDs), the weekly GitHub trending scan, and supplementary online discovery across Chinese tech media (CSDN, 知乎, IT之家, Ofweek), industry newsletters, and public product announcements. Candidates were cross-checked against the existing knowledge base (942 unique arXiv IDs in `papers.json`, 280 in `methods.json`) before admission.

## Papers

### World Models & Simulation

- [Continuous-Action World Models: Learning Cross-Embodiment Spatiotemporal Dynamics Priors](https://arxiv.org/abs/2610.40401) — 2026-10-29; World Models & Simulation; preprint.
- [HiFOR: Hierarchical Foresight with Action-Guided World Groundding for Vision-Language-Action Model](https://arxiv.org/abs/2610.40373) — 2026-10-29; Embodied AI / World Models & Simulation; preprint.
- [PRIME W0: Physical Priors from World Models for Embodied Manipulation](https://arxiv.org/abs/2610.39528) — 2026-10-29; Embodied AI / World Models & Simulation; preprint.
- [Predict the Reward, Not the World: World Reward Models for ML Agents](https://arxiv.org/abs/2610.38439) — 2026-10-28; World Models & Simulation; preprint.
- [MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model](https://arxiv.org/abs/2610.37175) — 2026-10-27; World Models & Simulation; preprint.

### Embodied AI & VLA

- [Gym-Anything for Robotics: Scaling physical simulations with digital agents](https://arxiv.org/abs/2610.40565) — 2026-10-29; Embodied AI; preprint.
- [Recursive Self-Improvement in Physical AI: Mechanisms, Evidence, and Evaluation](https://arxiv.org/abs/2610.38266) — 2026-10-28; Self-Evolution & Learning / Embodied AI; preprint.
- [Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory](https://arxiv.org/abs/2610.39446) — 2026-10-29; Memory Systems / Embodied AI; preprint.

### Multi-Agent Systems

- [EpiAgent: Epistemic Self-Play for LLM Agents](https://arxiv.org/abs/2610.40227) — 2026-10-29; Multi-Agent Systems; preprint.
- [EvoTeam: Multi-Agent Collaboration via Evolving Teams](https://arxiv.org/abs/2610.39813) — 2026-10-29; Multi-Agent Systems; preprint.
- [Locating and Closing Information Gaps in Multi-Agent Systems](https://arxiv.org/abs/2610.40186) — 2026-10-29; Multi-Agent Systems; preprint.
- [Goal-Aware Dynamic Multi-Agent Collaboration for Long-Horizon Tasks](https://arxiv.org/abs/2610.39193) — 2026-10-29; Multi-Agent Systems / Planning; preprint.
- [Auditable Belief Updates as a Missing Safety Layer for LLM-Powered Multi-Agent Systems](https://arxiv.org/abs/2610.38869) — 2026-10-28; Safety & Alignment / Multi-Agent Systems; preprint.

### Safety & Alignment

- [Where You Inject Matters: The Trust Region Effect in LLM Agents](https://arxiv.org/abs/2610.38867) — 2026-10-28; Safety & Alignment / Tool Use; preprint.

### Web/GUI Agents

- [DynaRev: Benchmarking Web Agents under Dynamic Goal Revision](https://arxiv.org/abs/2610.40133) — 2026-10-29; Web/GUI Agent / Evaluation & Benchmarks; preprint.
- [AgentHeal: Evaluating Goal-Preserving Resource Recovery of Web Agents under Access Barriers](https://arxiv.org/abs/2610.39234) — 2026-10-29; Web/GUI Agent / Evaluation & Benchmarks; preprint.

### Code Agents

- [When Relevant Code Is Wrong: Runtime-Aware Context for AI Coding Agents](https://arxiv.org/abs/2610.38800) — 2026-10-28; Code Agent; preprint.
- [Think Before You Act: Decision Gate for LLM Agents](https://arxiv.org/abs/2610.38620) — 2026-10-28; Code Agent / Safety & Alignment; preprint.
- [Security Impact of Coding Agent's Memory Files](https://arxiv.org/abs/2610.38521) — 2026-10-28; Code Agent / Safety & Alignment; preprint.
- [MUSE: Multi-Level Memory with Selective Runtime Injection for Scientific Coding Agents](https://arxiv.org/abs/2610.38332) — 2026-10-28; Memory Systems / Code Agent; preprint.

### Tool Use & Evaluation

- [Prefix Executability: Evaluating Tool-Using Agents Beyond Final Success](https://arxiv.org/abs/2610.40444) — 2026-10-29; Evaluation & Benchmarks / Tool Use; preprint.
- [MRC-MMAgent: Reinforcement Learning for Multi-Role Collaboration in Multimodal Tool-Using Agents](https://arxiv.org/abs/2610.39324) — 2026-10-29; Tool Use; preprint.
- [ATLAS-Bench: An Agentic Tool-Use Benchmark for Local Area Search](https://arxiv.org/abs/2610.39438) — 2026-10-29; Tool Use / Evaluation & Benchmarks; preprint.
- [RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models](https://arxiv.org/abs/2610.40026) — 2026-10-29; Evaluation & Benchmarks / Embodied AI; preprint.

## Frameworks

- [Cline](https://github.com/cline/cline) — Autonomous coding agent as SDK, IDE extension (VS Code, JetBrains), CLI, and desktop app; multi-agent teams, scheduled agents, MCP and plugin extensibility. Existing project, first admitted here today. Apache-2.0, 71.1k stars.
- [DeerFlow](https://github.com/bytedance/deer-flow) — Open-source long-horizon SuperAgent harness by ByteDance using sandboxes, memories, tools, skills, subagents and a message gateway. Existing project, first admitted here today. MIT, 84.7k stars.
- [Goose](https://github.com/aaif-goose/goose) — Open-source, extensible general-purpose AI agent (desktop, CLI, API) built in Rust; 15+ providers and 70+ MCP extensions; Linux Foundation Agentic AI Foundation. Existing project, first admitted here today. Apache-2.0, 56.0k stars.
- [Nanobot](https://github.com/HKUDS/nanobot) — Ultra-lightweight, self-hosted personal AI agent framework with WebUI, TUI, and chat-app channels; built-in file tools, long-term memory, MCP, and scheduled automations. Existing project, first admitted here today. MIT, 49.7k stars.

## Benchmarks

- [DynaRev](https://arxiv.org/abs/2610.40133) — 181 tasks evaluating web agents under dynamic goal revision where users change requirements during interaction. Paper-announced; artifact availability has not been checked.
- [AgentHeal](https://arxiv.org/abs/2610.39234) — Evaluates goal-preserving resource recovery of web agents facing access barriers (dead links, authentication walls, rate limits). Paper-announced; artifact availability has not been checked.
- [ATLAS-Bench](https://arxiv.org/abs/2610.39438) — Agentic tool-use benchmark for local area search, testing whether results satisfy mandatory requirements at given times and locations. Paper-announced; artifact availability has not been checked.
- [Prefix Executability](https://arxiv.org/abs/2610.40444) — Trajectory-level evaluation protocol for tool-using agents, measuring whether intermediate tool-call prefixes are executable beyond final success. Paper-announced; artifact availability has not been checked.
- [RoboSeed](https://arxiv.org/abs/2610.40026) — Multidimensional evaluation of VLA and world-action models across capability, resource affordability and research evidence reliability. Paper-announced; artifact availability has not been checked.
- [MAServeBench](https://arxiv.org/abs/2610.40293) — Benchmark for multi-agent LLM serving systems with hierarchical collaboration workloads and interdependent model/tool operations. Paper-announced; artifact availability has not been checked.
- [AgentDecept](https://arxiv.org/abs/2610.39377) — Benchmark for deceptive behavior in tool-using LLM agents under pressure. Paper-announced; artifact availability has not been checked.

## Industry signals (not yet admitted to industries.json)

The following were noted from supplementary online discovery but have not been added to `industries.json` because production-deployment status requires per-case official verification beyond this round:

- **Anthropic Claude Duet** (announced 2026-10-21) — proactive AI agent for SMBs and professionals; sends daily briefings, monitors apps, builds dashboards; research preview via waitlist for Claude Pro/Max in the US; based on Opus 5.5 with an independent browser VM; supports iOS, Android and web.
- **JetBrains ThinkRail** (2026-10-26) — open-sourced agentic IDE.
- **OpenMobile-2** (2026-10-26, Nanjing University & SenseTime) — open-source mobile agent; 59.6 on real-device SPA-Bench.
- **Agentic SecOps evaluation** (2026-10-29, 电子技术应用) — vendor assessment of agentic security-operations capabilities across finance, energy, government, manufacturing and internet sectors.
- **《2026 中国 AI 智能体产业应用标杆案例蓝皮书》** (2026-10-28, OFweek) — industry benchmark case-study blue book covering task closure rate, human-takeover rate and per-ticket cost metrics.

These are flagged for follow-up; no production deployment, funding figure or benchmark score is inferred from a news listing alone.

## Deferred

45 of the 69 net-new arXiv candidates remain unreviewed this round. Candidates whose titles and abstracts concern methods outside the repo's current 12-category scope, or whose agent relevance is incidental, were held back. No funding, production deployment or benchmark score is inferred from a candidate listing.
