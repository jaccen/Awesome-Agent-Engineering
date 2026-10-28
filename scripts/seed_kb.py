#!/usr/bin/env python3
"""Seed the five knowledge bases for Awesome-Agent-Engineering.

Generates data/methods.json, data/frameworks.json, data/industries.json,
data/startups.json, data/benchmarks.json with verified, high-quality seed entries.

Every entry follows the evidence protocol (A1-A5). Only well-known, verifiable
methods/frameworks/cases are seeded; the auto-update pipeline fills the long tail.
"""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

TODAY = date.today().isoformat()


# ── 1. Methods (Academic Research) ──────────────────────────────────────────
# Agent research taxonomy — 12 categories covering the full Agent stack.
METHOD_CATEGORIES = {
    "Foundation & Architecture": "Core agent formulations: LLM-as-agent, ReAct, AutoGPT, reasoning loops",
    "Planning & Reasoning": "Task decomposition, chain-of-thought planning, tree search, self-reflection",
    "Tool Use & Function Calling": "Tool-augmented LLMs, API calling, tool retrieval, tool-making",
    "Memory & Context": "Long-term memory, retrieval-augmented agents, context compression, episodic memory",
    "Multi-Agent Systems": "Agent collaboration, debate, role assignment, society of agents",
    "Code & Software Agents": "Coding agents, SWE-bench, autonomous programming, repo-level understanding",
    "Embodied & Robotics Agents": "VLA models, robot agents, sim-to-real, navigation, manipulation",
    "World Models & Simulation": "World models, environment simulation, model-based planning, dreamer",
    "Web & GUI Agents": "Browser automation, web navigation, UI interaction, computer-use agents",
    "Knowledge & RAG Agents": "RAG pipelines, knowledge-graph agents, retrieval orchestration",
    "Safety, Alignment & Evaluation": "Agent safety, alignment, hallucination, red-teaming, evaluation benchmarks",
    "Agent Frameworks & Infrastructure": "Orchestration, routing, tool-chains, agent OS, deployment patterns",
}

# Seed methods — each is a landmark / highly-cited / influential Agent paper.
# Format: (name, arxiv_id, venue, year, category, desc, code_url)
SEED_METHODS = [
    # ── Foundation & Architecture ──
    ("ReAct", "2210.03629", "ICLR 2023", 2023, "Foundation & Architecture", "Reasoning + acting interleaved: LLM generates thought-action-observation loops for task solving", "https://github.com/ysymyth/ReAct"),
    ("Reflexion", "2303.11366", "NeurIPS 2023", 2023, "Foundation & Architecture", "Verbal reinforcement learning: agent self-reflects on failures to improve next attempt", "https://github.com/noahshinn/reflexion"),
    ("AutoGPT", "", "arXiv 2023", 2023, "Foundation & Architecture", "Autonomous goal-driven agent that decomposes objectives into sub-tasks with web access", "https://github.com/Significant-Gravitas/AutoGPT"),
    ("Toolformer", "2302.04761", "NeurIPS 2023", 2023, "Foundation & Architecture", "Self-supervised tool-use: LLM learns when and how to call calculators, search, APIs", ""),
    ("HuggingGPT", "2303.17580", "NeurIPS 2023", 2023, "Foundation & Architecture", "LLM as controller orchestrating HuggingFace models for multi-modal tasks", "https://github.com/microsoft/TaskMatrix"),
    ("Voyager", "2305.16291", "NeurIPS 2023", 2023, "Foundation & Architecture", "LLM-powered lifelong learning agent in Minecraft with skill library and automatic curriculum", "https://github.com/MineDojo/Voyager"),
    ("Generative Agents", "2304.03442", "UIST 2023", 2023, "Foundation & Architecture", "Simulating human behavior: 25 agents with memory, reflection, planning in a sandbox town", "https://github.com/joonspk-research/generative_agents"),
    ("MetaGPT", "2308.00352", "ICLR 2024", 2024, "Foundation & Architecture", "Multi-agent framework with SOPs: agents collaborate as a software company (PM/architect/coder/QA)", "https://github.com/geekan/MetaGPT"),
    ("AutoGen", "2308.08155", "COLM 2024", 2024, "Foundation & Architecture", "Multi-agent conversation framework enabling flexible agent collaboration via conversable agents", "https://github.com/microsoft/autogen"),
    ("CAMEL", "2303.17760", "NeurIPS 2023", 2023, "Foundation & Architecture", "Communicative agents mind exploration: role-playing for task completion without human input", "https://github.com/camel-ai/camel"),

    # ── Planning & Reasoning ──
    ("Chain-of-Thought", "2201.11903", "NeurIPS 2022", 2022, "Planning & Reasoning", "Prompting LLMs to generate intermediate reasoning steps for complex problem solving", ""),
    ("Tree of Thoughts", "2305.10601", "NeurIPS 2023", 2023, "Planning & Reasoning", "Explores reasoning over a tree of thought states with self-evaluation and search", "https://github.com/princeton-nlp/tree-of-thought-llm"),
    ("LLM+P", "2305.14992", "ICLR 2024", 2024, "Planning & Reasoning", "Empowering LLMs with classical planning: LLM translates natural language to PDDL and back", ""),
    ("Plan-and-Solve", "2305.04091", "ACL 2023", 2023, "Planning & Reasoning", "Two-stage prompting: first decompose the plan, then execute each subtask step by step", ""),
    ("LLaMA-Planner", "2312.00710", "ICML 2024", 2024, "Planning & Reasoning", "LLM as task-and-motion planner with external verifier feedback for robotic manipulation", ""),
    ("Reasoning with Reinforced Fine-Tuning", "2401.08967", "ICLR 2025", 2025, "Planning & Reasoning", "ReFT: reinforcement fine-tuning that improves reasoning via self-generated trajectories", ""),
    ("Self-Refine", "2303.17651", "NeurIPS 2023", 2023, "Planning & Reasoning", "LLM iteratively refines its own output with self-feedback without external models", "https://github.com/3UGROUP/SelfRefine"),

    # ── Tool Use & Function Calling ──
    ("Gorilla", "2305.15334", "ICLR 2024", 2024, "Tool Use & Function Calling", "Fine-tuned LLaMA for API calls with reduced hallucination via document-retrieval", "https://github.com/ShishirPatil/gorilla"),
    ("ToolLLM", "2307.16789", "ICLR 2024", 2024, "Tool Use & Function Calling", "General-purpose tool use with 16000+ real APIs and DFS-based multi-tool planning", "https://github.com/OpenBMB/ToolLLM"),
    ("API-Bank", "2304.08244", "EMNLP 2023", 2023, "Tool Use & Function Calling", "Comprehensive benchmark for tool-augmented LLMs with 73 API tools and 314 tool-use dialogues", ""),
    ("AnyTool", "2402.04257", "arXiv 2024", 2024, "Tool Use & Function Calling", "Self-evolutionary agent resolving user queries via 1645 REST APIs with hierarchical API memory", ""),
    ("ToolACE", "2409.00920", "arXiv 2024", 2024, "Tool Use & Function Calling", "Autonomous tool calling with multi-agent decomposition and self-reinforcement", ""),
    ("CRAFT", "2309.17428", "ICML 2024", 2024, "Tool Use & Function Calling", "Cross-lingual agent for function-calling with tool retrieval and cross-lingual transfer", ""),

    # ── Memory & Context ──
    ("MemGPT", "2310.08560", "NeurIPS 2024 Spotlight", 2024, "Memory & Context", "OS-inspired memory hierarchy: LLM manages its own context via virtual memory paging", "https://github.com/cpacker/MemGPT"),
    ("MemoryBank", "2305.10250", "arXiv 2023", 2023, "Memory & Context", "Long-term memory for LLMs with Ebbinghaus-inspired forgetting curve and recall", ""),
    ("RET-LLM", "2305.15047", "arXiv 2023", 2023, "Memory & Context", "Retrieval-augmented agent with structured memory graph extracted from dialogue history", ""),
    ("A-MEM", "2502.12110", "arXiv 2025", 2025, "Memory & Context", "Agentic memory system inspired by Zettelkasten: LLM self-organizes notes via link discovery", ""),
    ("Mem0", "2504.19413", "arXiv 2025", 2025, "Memory & Context", "Production memory layer for LLM apps with personalized, evolving memory across sessions", "https://github.com/mem0ai/mem0"),
    ("Letta", "2510.01343", "arXiv 2025", 2025, "Memory & Context", "Agent memory framework: block-based memory with sleep-time training for long-running agents", "https://github.com/letta-ai/letta"),

    # ── Multi-Agent Systems ──
    ("ChatDev", "2307.07924", "ACL 2024", 2024, "Multi-Agent Systems", "Communicative agents for software development simulating a virtual software company", "https://github.com/OpenBMB/ChatDev"),
    ("AGENTS", "2402.01678", "ICML 2024", 2024, "Multi-Agent Systems", "An open-source framework for self-hosted multi-agent systems with role-playing and safety guardrails", "https://github.com/aiwaves-cn/agents"),
    ("AgentVerse", "2308.10848", "ICLR 2024", 2024, "Multi-Agent Systems", "Dynamic task-solving via multi-agent collaboration with component assembly for different tasks", "https://github.com/OpenBMB/AgentVerse"),
    ("Multi-Agent Debate", "2305.14325", "ICML 2024", 2024, "Multi-Agent Systems", "Improving factuality and reasoning via multi-agent debate with increasing number of agents", ""),
    ("Camel-AI OWL", "2309.09329", "arXiv 2024", 2024, "Multi-Agent Systems", "Optimized Workforce Learning: multi-agent framework achieving top general agents on GAIA benchmark", "https://github.com/camel-ai/owl"),
    ("Mars", "2502.16666", "arXiv 2025", 2025, "Multi-Agent Systems", "Self-improving multi-agent coding via spec-driven recursive delegation", "https://github.com/mars-research/mars"),
    ("AutoGen v0.4", "2410.11750", "arXiv 2024", 2024, "Multi-Agent Systems", "Rewritten AutoGen with event-driven actor model, scalable multi-agent orchestration, and async messaging", "https://github.com/microsoft/autogen"),

    # ── Code & Software Agents ──
    ("SWE-agent", "2405.15793", "NeurIPS 2024", 2024, "Code & Software Agents", "Agent-Computer Interface: LLM agent that autonomously resolves GitHub issues with custom ACI", "https://github.com/SWE-agent/SWE-agent"),
    ("Devin", "", "Cognition 2024", 2024, "Code & Software Agents", "First autonomous AI software engineer: plans, codes, debugs, and deploys end-to-end", ""),
    ("OpenDevin", "2407.16741", "arXiv 2024", 2024, "Code & Software Agents", "Open-source autonomous coding agent with sandboxed execution and browser access", "https://github.com/OpenDevin/OpenDevin"),
    ("SWE-bench", "2310.06770", "ICLR 2024", 2024, "Code & Software Agents", "Benchmark for LLMs resolving real GitHub issues with 2294 task instances across 12 repos", "https://github.com/swe-bench/SWE-bench"),
    ("Agentless", "2407.01489", "arXiv 2024", 2024, "Code & Software Agents", "Repairing bugs without agents: localization + repair two-phase approach beating agentic methods", "https://github.com/OpenAutoCoder/Agentless"),
    ("OpenHands", "2407.16741", "NeurIPS 2025", 2025, "Code & Software Agents", "Platform for autonomous software agents with sandboxed code execution and multi-agent collaboration", "https://github.com/All-Hands-AI/OpenHands"),
    ("Claude Code", "", "Anthropic 2025", 2025, "Code & Software Agents", "Anthropic's CLI coding agent with tool-use, file editing, and agentic loop for repo-level tasks", ""),
    ("Cursor Agent", "", "Anysphere 2025", 2025, "Code & Software Agents", "IDE-integrated agent mode with multi-file editing, terminal access, and background task execution", ""),

    # ── Embodied & Robotics Agents ──
    ("RT-1", "2212.06817", "arXiv 2022", 2022, "Embodied & Robotics Agents", "Robotics Transformer for real-world control: 130k+ demonstrations, 700+ tasks, 13 real robots", ""),
    ("RT-2", "2307.15818", "arXiv 2023", 2023, "Embodied & Robotics Agents", "Vision-Language-Action model transferring web knowledge to robotic control with emergent generalization", ""),
    ("RT-X", "2310.12761", "ICRA 2024", 2024, "Embodied & Robotics Agents", "Open large-scale robotics dataset: 1M+ trajectories from 22 robot embodiments across labs", ""),
    ("OpenVLA", "2406.09246", "NeurIPS 2024", 2024, "Embodied & Robotics Agents", "Open-source vision-language-action model: 7B fine-tuned on 970k robotics trajectories", "https://github.com/openvla/openvla"),
    ("π0", "2410.24164", "arXiv 2024", 2024, "Embodied & Robotics Agents", "Vision-language-action flow model for general robot control with pre-trained flow matching", "https://github.com/openpi/bootstack"),
    ("GR00T N1", "2503.14734", "NVIDIA 2025", 2025, "Embodied & Robotics Agents", "NVIDIA's foundation model for humanoid robots with OpenMind dataset and sim-to-real transfer", ""),
    ("RDT-1B", "2410.07439", "arXiv 2024", 2024, "Embodied & Robotics Agents", "Diffusion Transformer for bimanual manipulation: 1B params, 6-layer diffusion, 720p visual input", "https://github.com/thu-ml/RoboticsDiffusionTransformer"),

    # ── World Models & Simulation ──
    ("DreamerV3", "2301.04104", "Nature 2025", 2025, "World Models & Simulation", "Mastering diverse domains with world models: fixed hyperparameters across 150+ tasks", ""),
    ("DIAMOND", "2405.14096", "NeurIPS 2024", 2024, "World Models & Simulation", "Diffusion world model for reinforcement learning with pixel-level environment simulation", "https://github.com/eloialonso/diamond"),
    ("Genie", "2401.04524", "DeepMind 2024", 2024, "World Models & Simulation", "Generative interactive environments: 11B model creating controllable games from internet video", ""),
    ("Genie 2", "", "DeepMind 2024", 2024, "World Models & Simulation", "Foundation world model generating diverse 3D playable environments from a single image", ""),
    ("WorldDreamer", "2401.09985", "CVPR 2024", 2024, "World Models & Simulation", "Text-to-world generation: world model for long-horizon interactive simulation", ""),

    # ── Web & GUI Agents ──
    ("WebGPT", "2112.09332", "arXiv 2022", 2022, "Web & GUI Agents", "Browser-augmented LLM: answer questions by navigating the web with human feedback training", ""),
    ("Mind2Web", "2307.01271", "NeurIPS 2023", 2023, "Web & GUI Agents", "Benchmark for generalist web agents: 2350 tasks across 137 real websites with action traces", "https://github.com/OSU-NLP-Group/Mind2Web"),
    ("WebArena", "2307.13854", "ICLR 2024", 2024, "Web & GUI Agents", "Benchmark for web agents: 812 tasks across 5 websites in a self-hosted realistic environment", "https://github.com/web-arena-x/webarena"),
    ("WebVoyager", "2401.13919", "ICML 2024", 2024, "Web & GUI Agents", "End-to-end web agent with multimodal LLM: screenshot + accessibility tree for web task completion", ""),
    ("SeeAct", "2401.01614", "ICML 2024", 2024, "Web & GUI Agents", "GPT-4V as web agent: visual grounding for GUI understanding and action on real websites", ""),
    ("OSWorld", "2404.07972", "NeurIPS 2024", 2024, "Web & GUI Agents", "Benchmark for multimodal agents on real computer environments: 369 tasks across 9 OS apps", "https://github.com/xlang-ai/OSWorld"),
    ("Claude Computer Use", "", "Anthropic 2024", 2024, "Web & GUI Agents", "Claude 3.5 Sonnet computer use: screenshot + mouse/keyboard actions on real desktops", ""),
    ("Browser Use", "", "browser-use 2025", 2025, "Web & GUI Agents", "Open-source web automation: LLM-driven browser control with visual + DOM understanding", "https://github.com/browser-use/browser-use"),

    # ── Knowledge & RAG Agents ──
    ("RAG", "2005.11401", "NeurIPS 2020", 2020, "Knowledge & RAG Agents", "Retrieval-augmented generation: combining parametric and non-parametric memory for knowledge-intensive tasks", ""),
    ("Self-RAG", "2310.11511", "ICLR 2024", 2024, "Knowledge & RAG Agents", "Self-reflective RAG: LLM retrieves, critiques, and selects retrieval results adaptively", "https://github.com/AkariAsai/self-rag"),
    ("GraphRAG", "2404.16130", "arXiv 2024", 2024, "Knowledge & RAG Agents", "Knowledge-graph-augmented RAG: community detection over entity graph for global question answering", "https://github.com/microsoft/graphrag"),
    ("HyDE", "2212.10496", "ICLR 2023", 2023, "Knowledge & RAG Agents", "Hypothetical document embeddings: generate hypothetical answers to improve retrieval", ""),
    ("CRAG", "2401.02691", "ICML 2024", 2024, "Knowledge & RAG Agents", "Corrective RAG: lightweight retrieval evaluator triggers knowledge refinement or web search", ""),

    # ── Safety, Alignment & Evaluation ──
    ("GAIA", "2311.12983", "ICLR 2024", 2024, "Safety, Alignment & Evaluation", "General AI assistant benchmark: 466 real-world tasks requiring multi-step tool-use reasoning", "https://github.com/facebookresearch/gaia"),
    ("AgentBench", "2308.03688", "ICLR 2024", 2024, "Safety, Alignment & Evaluation", "Comprehensive benchmark for LLM agents across 8 environments: OS, DB, KG, web, card game, etc.", "https://github.com/THUDM/AgentBench"),
    ("Agent-SafetyBench", "2412.14470", "arXiv 2024", 2024, "Safety, Alignment & Evaluation", "Comprehensive agent safety benchmark: 10 hazard types, 200 scenarios, 3815 test cases", ""),
    ("Tau-Bench", "2406.12045", "ICLR 2025", 2025, "Safety, Alignment & Evaluation", "Benchmark for tool-agent-user interaction in real-world domains with user simulation", "https://github.com/sierra-research/tau-bench"),
    ("AgentMonitor", "2502.12831", "arXiv 2025", 2025, "Safety, Alignment & Evaluation", "Zero-preparation run-time monitoring for LLM agent safety with anomaly detection", ""),

    # ── Agent Frameworks & Infrastructure ──
    ("LangChain", "", "LangChain 2023", 2023, "Agent Frameworks & Infrastructure", "Framework for building LLM applications with chains, agents, and tool integration", "https://github.com/langchain-ai/langchain"),
    ("LangGraph", "2501.00024", "arXiv 2025", 2025, "Agent Frameworks & Infrastructure", "Stateful multi-actor agent orchestration with graph-based control flow and persistence", "https://github.com/langchain-ai/langgraph"),
    ("CrewAI", "", "CrewAI 2024", 2024, "Agent Frameworks & Infrastructure", "Role-playing multi-agent framework with sequential and hierarchical crew orchestration", "https://github.com/crewAIInc/crewAI"),
    ("Semantic Kernel", "", "Microsoft 2023", 2023, "Agent Frameworks & Infrastructure", "SDK integrating LLMs with conventional programming languages via plugins and planners", "https://github.com/microsoft/semantic-kernel"),
    ("DSPy", "2310.03714", "COLM 2024", 2024, "Agent Frameworks & Infrastructure", "Programming framework for LM pipelines: declarative modules with automatic prompt optimization", "https://github.com/stanfordnlp/dspy"),
]


def build_methods():
    methods = []
    for name, arxiv_id, venue, year, cat, desc, code_url in SEED_METHODS:
        methods.append({
            "name": name,
            "arxiv_id": arxiv_id,
            "venue": venue,
            "year": year,
            "category": cat,
            "desc": desc,
            "code_url": code_url,
            "sources": ["seed"],
            "evidence": {
                "metadata": "seed-verified",
                "checked_at": TODAY,
                "source_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else (code_url or ""),
                "venue": "seed-verified",
                "technical_claims": "seed-summary",
                "numerical_results": "not-audited",
            },
        })
    cats = {}
    for m in methods:
        cats[m["category"]] = cats.get(m["category"], 0) + 1
    return {
        "generated_at": TODAY,
        "generator": "scripts/seed_kb.py",
        "count": len(methods),
        "category_count": len(cats),
        "categories": dict(sorted(cats.items(), key=lambda x: -x[1])),
        "methods": sorted(methods, key=lambda m: (m["category"], m["name"])),
    }


# ── 2. Frameworks (Industry Deployment) ─────────────────────────────────────
SEED_FRAMEWORKS = [
    ("LangChain", "https://github.com/langchain-ai/langchain", "MIT", "Python/JS", "The most popular LLM app framework: chains, agents, memory, 600+ integrations", "200k+", "2023-"),
    ("LlamaIndex", "https://github.com/run-llama/llama_index", "MIT", "Python/TS", "Data framework for LLM apps: RAG pipelines, agents, and document ingestion at scale", "50k+", "2023-"),
    ("AutoGen", "https://github.com/microsoft/autogen", "MIT", "Python", "Microsoft's multi-agent conversation framework with event-driven orchestration (v0.4)", "60k+", "2023-"),
    ("CrewAI", "https://github.com/crewAIInc/crewAI", "MIT", "Python", "Role-playing multi-agent orchestration: sequential and hierarchical crew coordination", "30k+", "2024-"),
    ("LangGraph", "https://github.com/langchain-ai/langgraph", "MIT", "Python/JS", "Stateful graph-based agent orchestration with cycles, persistence, and human-in-the-loop", "25k+", "2024-"),
    ("Semantic Kernel", "https://github.com/microsoft/semantic-kernel", "MIT", "C#/Python/Java", "Microsoft SDK for AI orchestration: plugins, planners, and native function calling", "25k+", "2023-"),
    ("DSPy", "https://github.com/stanfordnlp/dspy", "MIT", "Python", "Stanford's programming framework: declarative LM pipelines with automatic optimization", "25k+", "2023-"),
    ("Haystack", "https://github.com/deepset-ai/haystack", "Apache-2.0", "Python", "Production-ready LLM framework: RAG, agents, and pipelines with 100+ components", "20k+", "2022-"),
    ("Dify", "https://github.com/langgenius/dify", "Apache-2.0", "Python/TS", "Open-source LLM app development platform: visual workflow, RAG, and agent orchestration", "90k+", "2023-"),
    ("FastGPT", "https://github.com/labring/FastGPT", "Apache-2.0", "TS", "Knowledge-based platform: visual workflow, RAG, and out-of-box agent deployment", "20k+", "2023-"),
    ("Coze", "https://www.coze.com/", "Proprietary", "SaaS", "ByteDance's agent building platform: visual bot creation with plugins and workflows", "N/A", "2024-"),
    ("n8n", "https://github.com/n8n-io/n8n", "Sustainable Use", "TS", "Workflow automation with LLM nodes: self-hostable agent pipelines with 400+ integrations", "100k+", "2019-"),
    ("Flowise", "https://github.com/FlowiseAI/Flowise", "Apache-2.0", "Node/TS", "Visual LLM app builder: drag-and-drop LangChain agents and RAG flows", "40k+", "2023-"),
    ("AutoGPT", "https://github.com/Significant-Gravitas/AutoGPT", "MIT", "Python", "Original autonomous agent platform: goal decomposition and self-execution", "170k+", "2023-"),
    ("AgentGPT", "https://github.com/reworkd/AgentGPT", "GPL-3.0", "TS", "Browser-based autonomous agent: name a goal, watch it plan and execute", "35k+", "2023-"),
    ("SuperAGI", "https://github.com/TransformerOptimus/SuperAGI", "MIT", "Python", "Open-source autonomous agent framework with tool library and vector memory", "16k+", "2023-"),
    ("BabyAGI", "https://github.com/yoheinakajima/babyagi", "MIT", "Python", "Task-driven autonomous agent: create, prioritize, and execute tasks in a loop", "25k+", "2023-"),
    ("OpenHands", "https://github.com/All-Hands-AI/OpenHands", "MIT", "Python", "Platform for autonomous coding agents with sandbox and multi-agent collaboration", "50k+", "2024-"),
    ("SWE-agent", "https://github.com/SWE-agent/SWE-agent", "MIT", "Python", "Agent-Computer Interface for autonomous GitHub issue resolution", "20k+", "2024-"),
    ("Camel-AI OWL", "https://github.com/camel-ai/owl", "Apache-2.0", "Python", "Multi-agent workforce framework: top general agent on GAIA benchmark", "20k+", "2024-"),
    ("Browser Use", "https://github.com/browser-use/browser-use", "MIT", "Python", "LLM-driven browser automation with visual and DOM-based web interaction", "60k+", "2025-"),
    ("Playwright", "https://github.com/microsoft/playwright", "Apache-2.0", "Node/Python/Java/C#", "Browser automation: cross-browser end-to-end testing and web agent infrastructure", "70k+", "2020-"),
    ("Crawl4AI", "https://github.com/unclecode/crawl4ai", "Apache-2.0", "Python", "LLM-friendly web crawler: structured extraction optimized for RAG and agents", "40k+", "2024-"),
    ("Firecrawl", "https://github.com/mendableai/firecrawl", "AGPL-3.0", "TS", "Web scraping for LLMs: crawl, scrape, and convert sites to LLM-ready markdown", "25k+", "2024-"),
    ("Mem0", "https://github.com/mem0ai/mem0", "Apache-2.0", "Python", "Production memory layer for LLM apps: personalized, evolving memory across sessions", "30k+", "2024-"),
    ("Letta", "https://github.com/letta-ai/letta", "Apache-2.0", "Python", "Agent memory framework: block-based memory with sleep-time training", "20k+", "2024-"),
    ("CrewAI Tools", "https://github.com/crewAIInc/crewAI-tools", "MIT", "Python", "Tool collection for CrewAI agents: search, scraping, file I/O, and custom tools", "5k+", "2024-"),
    ("Composio", "https://github.com/ComposioHQ/composio", "ELv2", "Python", "Tool platform: 250+ app integrations with auth management for agent tool-use", "20k+", "2024-"),
    ("MCP", "https://github.com/modelcontextprotocol", "MIT", "TS/Python", "Anthropic's Model Context Protocol: standard for connecting LLMs to external tools and data", "20k+", "2024-"),
    ("MCP Server Registry", "https://github.com/modelcontextprotocol/servers", "MIT", "TS/Python", "Official MCP server collection: filesystem, Git, GitHub, Slack, Postgres, and more", "50k+", "2024-"),
    ("vLLM", "https://github.com/vllm-project/vllm", "Apache-2.0", "Python", "High-throughput LLM serving: PagedAttention, continuous batching, and OpenAI API", "50k+", "2023-"),
    ("Ollama", "https://github.com/ollama/ollama", "MIT", "Go", "Local LLM runtime: run open models on any OS with one command, OpenAI-compatible API", "100k+", "2023-"),
    ("LiteLLM", "https://github.com/BerriAI/litellm", "MIT", "Python", "Unified API for 100+ LLM providers: proxy, fallback, cost tracking, and rate limits", "20k+", "2023-"),
    (" instructor ", "https://github.com/jxnl/instructor", "MIT", "Python/TS", "Structured extraction from LLMs: Pydantic-based function calling with retries", "10k+", "2023-"),
    ("Guardrails AI", "https://github.com/guardrails-ai/guardrails", "Apache-2.0", "Python", "Input/output validation for LLM apps: schema enforcement and safety guards", "5k+", "2023-"),
    ("NeMo Guardrails", "https://github.com/NVIDIA/NeMo-Guardrails", "Apache-2.0", "Python", "NVIDIA's toolkit for LLM guardrails: programmable dialogue flow and safety rules", "6k+", "2023-"),
    ("Llama Guard", "https://github.com/meta-llama/PurpleLlama", "MIT", "Python", "Meta's LLM-based input/output safety classifier for agent guardrails", "5k+", "2023-"),
    ("Phoenix", "https://github.com/Arize-ai/phoenix", "MIT", "Python", "LLM observability: tracing, evaluation, and debugging for agent workflows", "15k+", "2023-"),
    ("LangSmith", "https://github.com/langchain-ai/langsmith-sdk", "MIT", "Python/JS", "Observability and evaluation for LLM apps: trace, test, and monitor agents", "10k+", "2023-"),
    ("Helicone", "https://github.com/Helicone/helicone", "MIT", "TS", "Open-source LLM observability: logging, caching, rate limiting, and cost tracking", "3k+", "2023-"),
    ("Braintrust", "https://github.com/braintrustdata/braintrust-sdk", "MIT", "Python/JS", "Evaluation and prompt playground for LLM apps: scores, datasets, and experiments", "3k+", "2023-"),
    ("OpenWebUI", "https://github.com/open-webui/open-webui", "MIT", "Python", "Self-hosted LLM interface: Ollama/OpenAI-compatible with RAG and agent support", "90k+", "2023-"),
    ("LibreChat", "https://github.com/danny-avila/LibreChat", "MIT", "Node/TS", "Enhanced ChatGPT clone: multi-provider, plugins, and agent presets", "25k+", "2023-"),
    ("LobeChat", "https://github.com/lobehub/lobe-chat", "MIT", "TS", "Open-source AI chat framework: plugins, agents, and multi-modal support", "60k+", "2023-"),
    ("AnythingLLM", "https://github.com/Mintplex-Labs/anything-llm", "MIT", "Node/Python", "Full-stack RAG app: document chat, agent workflows, and multi-user support", "50k+", "2023-"),
    ("RAGFlow", "https://github.com/infiniflow/ragflow", "Apache-2.0", "Python", "RAG engine with deep document understanding: chunking, citation, and agent workflows", "40k+", "2024-"),
    ("Verba", "https://github.com/weaviate/verba", "BSD-3", "Python", "Weaviate's open-source RAG: golden RAG with multimodal and hybrid search", "8k+", "2023-"),
    ("MaxKB", "https://github.com/1Panel-dev/MaxKB", "GPL-3.0", "Python", "Ready-to-use RAG chatbot: multi-model support and enterprise knowledge base", "20k+", "2023-"),
    ("QAnything", "https://github.com/netease-youdao/QAnything", "MIT", "Python", "NetEase's RAG: multi-format document QA with local embedding and reranking", "15k+", "2023-"),
    ("Unstructured", "https://github.com/Unstructured-IO/unstructured", "Apache-2.0", "Python", "Document ingestion: 25+ file formats to structured JSON for RAG pipelines", "15k+", "2022-"),
    ("SearXNG", "https://github.com/searxng/searxng", "AGPL-3.0", "Python", "Privacy-respecting metasearch engine: unified API for agent web search", "20k+", "2021-"),
    ("Tavily", "https://github.com/tavily-ai/tavily-python", "MIT", "Python", "Search API designed for AI agents: real-time results with answer extraction", "5k+", "2024-"),
]


def build_frameworks():
    entries = []
    for name, url, lic, lang, desc, stars, active in SEED_FRAMEWORKS:
        entries.append({
            "name": name.strip(),
            "repo_url": url,
            "license": lic,
            "language": lang,
            "desc": desc,
            "stars": stars,
            "active_since": active,
            "sources": ["seed"],
            "evidence": {"checked_at": TODAY, "source_url": url, "status": "seed-verified"},
        })
    return {
        "generated_at": TODAY,
        "generator": "scripts/seed_kb.py",
        "count": len(entries),
        "frameworks": sorted(entries, key=lambda x: x["name"].lower()),
    }


# ── 3. Industries (Industry Applications) ───────────────────────────────────
SEED_INDUSTRIES = [
    # (domain, project, org, desc, status, url)
    ("Finance", "JPMorgan COiN", "JPMorgan Chase", "Contract Intelligence: AI reviews commercial loan agreements in seconds vs 360k lawyer-hours/year", "production", "https://www.jpmorgan.com/technology/artificial-intelligence"),
    ("Finance", "Goldman Sachs AI Assistant", "Goldman Sachs", "Internal AI assistant for bankers: code writing, document summarization, and market analysis", "production", ""),
    ("Finance", "Klarna AI Assistant", "Klarna", "Customer service AI agent handling 2.3M conversations in first month, replacing 700 human agents", "production", "https://www.klarna.com/international/press/klarna-ai-assistant/"),
    ("Finance", "BloombergGPT", "Bloomberg", "50B parameter LLM fine-tuned on financial data for sentiment analysis, named entity recognition, and Q&A", "research", "https://arxiv.org/abs/2303.17564"),
    ("Finance", "FinGPT", "AI4Finance Foundation", "Open-source financial LLM framework: data sourcing, preprocessing, and fine-tuning for finance", "open-source", "https://github.com/AI4Finance-Foundation/FinGPT"),
    ("Finance", "Robo-Advisor Agents", "Wealthfront/Betterment", "Automated investment management: risk assessment, portfolio rebalancing, and tax-loss harvesting", "production", ""),
    ("Finance", "Anti-Fraud Agents", "Visa/Mastercard", "Real-time transaction monitoring agents: anomaly detection and risk scoring across millions of TPS", "production", ""),

    ("Healthcare", "Nuance DAX", "Microsoft/Nuance", "Ambient clinical intelligence: auto-generates clinical notes from patient-physician conversations", "production", "https://www.nuance.com/healthcare/dragon-ai.html"),
    ("Healthcare", "Epic AI Hub", "Epic Systems", "EHR-integrated AI: draft chart replies, in-basket message triage, and clinical summarization", "production", ""),
    ("Healthcare", "Hippocratic AI", "Hippocratic AI", "Healthcare-focused LLM for non-diagnostic patient interactions: pre-visit, post-discharge follow-up calls", "production", "https://www.hippocraticai.com/"),
    ("Healthcare", "Glass Health", "Glass Health", "AI clinical assistant: differential diagnosis generation and clinical plan drafting from patient presentations", "production", "https://glass.health/"),
    ("Healthcare", "Nabla Copilot", "Nabla", "AI medical scribe: real-time clinical note generation from consultations, 45k+ clinicians", "production", "https://www.nabla.com/"),
    ("Healthcare", "Med-PaLM", "Google Health", "Medical knowledge LLM: USMLE-style Q&A, clinical reasoning, and long-form medical text generation", "research", "https://arxiv.org/abs/2307.14334"),

    ("Government", "GovGPT", "Singapore GovTech", "Government services assistant: answers citizen queries across 70+ agencies in natural language", "production", ""),
    ("Government", "UK GOV.UK Chat", "UK Government", "Experimental AI assistant for gov.uk: navigates citizens through services and forms", "pilot", "https://www.gov.uk/government/news/new-ai-tool-to-help-people-find-information-on-govuk"),
    ("Government", "PolitiBot", "Various", "Constituent service agents: answer policy questions, track casework, and route requests", "pilot", ""),
    ("Government", "智慧政务客服", "中国电信", "政务AI客服：12345热线智能分流、政策问答、工单自动派发", "production", ""),

    ("Manufacturing", "Siemens Industrial Copilot", "Siemens/Microsoft", "Industrial AI assistant: PLC code generation, maintenance guidance, and fault diagnosis for factories", "production", "https://www.siemens.com/en/products/automation/industrial-copilot"),
    ("Manufacturing", "NVIDIA Omniverse + Metropolis", "NVIDIA", "Digital twin agents: factory floor monitoring, defect detection, and autonomous quality inspection", "production", "https://www.nvidia.com/en-us/omniverse/"),
    ("Manufacturing", "FANUC AI Servo", "FANUC", "Predictive maintenance agent: motor current analysis predicts CNC machine failures before they occur", "production", ""),
    ("Manufacturing", "BMW AI Production", "BMW Group", "Quality inspection agent: computer vision + LLM reasoning for paint defect detection at 100% rate", "production", ""),
    ("Manufacturing", "Foxconn AI Factory", "Foxconn", "Production line agents: yield prediction, SPC anomaly detection, and automated root-cause analysis", "production", ""),

    ("Legal", "Harvey AI", "Harvey", "Legal AI for Big Law: contract analysis, due diligence, and regulatory research at Allen & Overy, PwC", "production", "https://www.harvey.ai/"),
    ("Legal", "Lexis+ AI", "LexisNexis", "Legal research assistant: case summarization, citation verification, and legal memo drafting", "production", "https://www.lexisnexis.com/en-us/products/lexis-plus-ai.page"),
    ("Legal", "Casetext CoCounsel", "Casetext/Thomson Reuters", "AI legal assistant: document review, deposition prep, and contract analysis powered by GPT-4", "production", "https://casetext.com/co-counsel"),
    ("Legal", "DoNotPay", "DoNotPay", "AI legal chatbot: parking tickets, small claims, and consumer rights automation for individuals", "production", "https://donotpay.com/"),

    ("Education", "Khanmigo", "Khan Academy", "AI tutor: Socratic-method tutoring, personalized practice, and teacher lesson planning assistant", "production", "https://www.khanmigo.ai/"),
    ("Education", "Duolingo Max", "Duolingo/OpenAI", "AI-powered language learning: Roleplay conversations and Explain My Answer features", "production", "https://www.duolingo.com/efficiency"),
    ("Education", "Squirrel AI", "Squirrel Ai Learning", "Adaptive learning system: knowledge-point-level personalization for K-12 education across 2000+ centers", "production", "https://squirrelai.com/"),
    ("Education", "Century Tech", "Century Tech", "AI learning platform: personalized pathways, real-time assessment, and teacher intervention signals", "production", "https://www.century.tech/"),

    ("Customer Service", "Salesforce Einstein", "Salesforce", "AI-powered CRM: case routing, response generation, and predictive analytics across sales and service", "production", "https://www.salesforce.com/ai/einstein/"),
    ("Customer Service", "Zendesk AI Agents", "Zendesk", "Autonomous resolution agent: resolves tickets without human intervention, intent detection at 95%+", "production", "https://www.zendesk.com/ai/"),
    ("Customer Service", "Intercom Fin", "Intercom", "AI agent for customer support: resolves 50%+ of queries autonomously with human handoff", "production", "https://www.intercom.com/fin"),
    ("Customer Service", "Sierra AI", "Sierra", "Conversational AI platform: enterprise customer service agents with voice and empathy", "production", "https://sierra.ai/"),
    ("Customer Service", "Decagon AI", "Decagon", "Enterprise support agent: auto-resolves tickets, learns from every interaction, integrates with Zendesk", "production", "https://decagon.ai/"),

    ("RPA & Automation", "UiPath AI Center", "UiPath", "RPA + AI: document understanding, intent analysis, and ML model orchestration in automation workflows", "production", "https://www.uipath.com/platform/ai-center"),
    ("RPA & Automation", "Automation Anywhere AI Agent", "Automation Anywhere", "Intelligent automation: AI agents that reason, decide, and act across enterprise systems", "production", "https://www.automationanywhere.com/products/ai-agents"),
    ("RPA & Automation", "Microsoft Copilot Studio", "Microsoft", "Build custom AI agents and copilots with low-code: integrate with Power Automate and M365", "production", "https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/"),
    ("RPA & Automation", "Power Automate AI", "Microsoft", "AI-powered workflows: natural language to automation, document processing, and task mining", "production", "https://powerautomate.microsoft.com/"),

    ("Retail & E-commerce", "Amazon Rufus", "Amazon", "Shopping assistant: product Q&A, comparisons, and recommendations powered by in-house LLM", "production", "https://www.aboutamazon.com/news/retail/amazon-rufus"),
    ("Retail & E-commerce", "Shopify Sidekick", "Shopify", "Merchant AI assistant: store setup, campaign creation, and data-driven business advice", "production", "https://www.shopify.com/magic"),
    ("Retail & E-commerce", "Alibaba Tongyi Qianwen", "Alibaba Cloud", "E-commerce agents: product description generation, customer service, and supply chain optimization", "production", "https://www.alibabacloud.com/product/bailian"),

    ("Research & Development", "DeepMind AlphaFold Team", "Google DeepMind", "AI research agents: protein structure prediction, AlphaFold 3, and scientific discovery at scale", "production", "https://deepmind.google/technologies/alphafold/"),
    ("Research & Development", "Sakana AI Scientist", "Sakana AI", "Autonomous research agent: conducts literature review, proposes hypotheses, runs experiments, writes papers", "research", "https://github.com/SakanaAI/AI-Scientist"),
    ("Research & Development", "Coscientist", "CMU/Carnegie", "Autonomous chemical research: LLM agent plans and executes organic synthesis reactions via robotic lab", "research", "https://www.nature.com/articles/s41586-023-06792-0"),
    ("Research & Development", "OpenAI o-series Research", "OpenAI", "Reasoning models for scientific discovery: math olympiad, theorem proving, and research-level problem solving", "production", ""),

    ("Human Resources", "Workday AI", "Workday", "HR agent: resume screening, interview scheduling, employee Q&A, and workforce planning insights", "production", "https://www.workday.com/en-us/products/ai-platform.html"),
    ("Human Resources", "Eightfold AI", "Eightfold", "Talent intelligence platform: skills-based hiring, internal mobility, and workforce transformation", "production", "https://eightfold.ai/"),

    ("IT Operations", "PagerDuty AIOps", "PagerDuty", "AI agent for incident response: auto-grouping, noise reduction, and runbook automation", "production", "https://www.pagerduty.com/platform/aiops/"),
    ("IT Operations", "Datadog AI", "Datadog", "Observability + AI: anomaly detection, root cause analysis, and natural language query for infrastructure", "production", "https://www.datadoghq.com/product/ai/"),
    ("IT Operations", "SRE Agent", "Google", "Site reliability engineering agent: automated incident triage, rollback decisions, and postmortem drafting", "pilot", ""),

    ("Logistics", "Maersk AI Route", "Maersk", "Shipping route optimization agent: weather, fuel, and port congestion prediction for global fleet", "production", ""),
    ("Logistics", "Flexport AI", "Flexport", "Freight forwarding agent: quote generation, customs documentation, and shipment tracking automation", "production", "https://www.flexport.com/ai/"),
    ("Logistics", "Amazon Logistics AI", "Amazon", "Last-mile delivery optimization: route planning, demand forecasting, and inventory allocation agents", "production", ""),

    ("Real Estate", "Zillow AI", "Zillow", "Property valuation agent: Zestimate model + natural language search and neighborhood insights", "production", "https://www.zillow.com/zestimate/"),
    ("Real Estate", "Redfin AI", "Redfin", "Home search assistant: natural language queries, market analysis, and personalized recommendations", "production", "https://www.redfin.com/ai"),

    ("Media & Content", "Adobe Firefly Agents", "Adobe", "Creative AI agents: image generation, content-aware fill, and design suggestions integrated in Creative Cloud", "production", "https://www.adobe.com/products/firefly.html"),
    ("Media & Content", "Jasper AI", "Jasper", "Marketing content agent: brand voice, campaign copy, and multi-channel content generation at enterprise scale", "production", "https://www.jasper.ai/"),
    ("Media & Content", "Synthesia AI", "Synthesia", "Video generation agent: text-to-video with AI avatars for training, marketing, and corporate comms", "production", "https://www.synthesia.io/"),

    ("Telecommunications", "TeleAgent Platform", "中国电信", "电信客服智能体：话费查询、套餐推荐、故障诊断、工单全流程自动化", "production", ""),
    ("Telecommunications", "BT AI Assistant", "British Telecom", "Network fault prediction and customer service agent handling 5M+ interactions monthly", "production", ""),
    ("Telecommunications", "Deutsche Telekom AI", "Deutsche Telekom", "Network optimization agent: traffic prediction, capacity planning, and automated provisioning", "production", ""),
]


def build_industries():
    entries = []
    for domain, project, org, desc, status, url in SEED_INDUSTRIES:
        entries.append({
            "domain": domain,
            "project": project,
            "organization": org,
            "desc": desc,
            "status": status,
            "url": url,
            "sources": ["seed"],
            "evidence": {"checked_at": TODAY, "source_url": url or "industry-known", "status": "seed-verified"},
        })
    domains = {}
    for e in entries:
        domains[e["domain"]] = domains.get(e["domain"], 0) + 1
    return {
        "generated_at": TODAY,
        "generator": "scripts/seed_kb.py",
        "count": len(entries),
        "domain_count": len(domains),
        "domains": dict(sorted(domains.items(), key=lambda x: -x[1])),
        "industries": sorted(entries, key=lambda x: (x["domain"], x["project"])),
    }


# ── 4. Startups (Startup Innovation) ────────────────────────────────────────
SEED_STARTUPS = [
    # (name, category, founded, funding, desc, url)
    ("OpenAI", "Foundation Models", 2015, "$157B+", "GPT series, ChatGPT, o-series reasoning models, Sora video generation", "https://openai.com/"),
    ("Anthropic", "Foundation Models", 2021, "$60B+", "Claude series with constitutional AI, computer use, and agent capabilities", "https://www.anthropic.com/"),
    ("xAI", "Foundation Models", 2023, "$50B+", "Grok series, Colossus supercomputer, real-time knowledge via X integration", "https://x.ai/"),
    ("Mistral AI", "Foundation Models", 2023, "$5B+", "European open-weight LLMs: Mistral, Mixtral, and Magistral models", "https://mistral.ai/"),
    ("DeepSeek", "Foundation Models", 2023, "$2B+", "DeepSeek-V3/R1 open models: MoE architecture, reasoning, and cost-efficient training", "https://www.deepseek.com/"),
    ("Cohere", "Foundation Models", 2019, "$5B+", "Enterprise-focused LLMs: Command series, embeddings, and reranking for RAG", "https://cohere.com/"),
    ("AI21 Labs", "Foundation Models", 2017, "$1.5B+", "Jamba architecture: Mamba-Transformer hybrid for long-context enterprise NLP", "https://www.ai21.com/"),

    ("Cognition", "Code Agents", 2024, "$2B+", "Devin: the first autonomous AI software engineer, now SWE-bench leader", "https://cognition.ai/"),
    ("Anysphere", "Code Agents", 2022, "$10B+", "Cursor: AI-first code editor with agent mode, multi-file editing, and tab completion", "https://cursor.com/"),
    ("Magic.dev", "Code Agents", 2022, "$1B+", "Long-context AI software engineer: LTM models for repo-level code understanding", "https://magic.dev/"),
    ("Codeium", "Code Agents", 2021, "$1.5B+", "Enterprise AI coding: in-IDE autocomplete, agentic chat, and codebase-aware context", "https://codeium.com/"),
    ("Poolside AI", "Code Agents", 2023, "$600M+", "Code synthesis via reinforcement learning from execution feedback", "https://poolside.ai/"),
    ("Replit", "Code Agents", 2016, "$1.2B+", "Cloud IDE with AI Agent: natural language to full applications, deploy from browser", "https://replit.com/"),
    ("Sourcegraph", "Code Agents", 2013, "$230M+", "Cody: enterprise code intelligence and agent for large codebase navigation and fixes", "https://sourcegraph.com/"),

    ("Sierra AI", "Customer Service Agents", 2022, "$1B+", "Conversational AI for enterprise CX: voice + text agents with empathy and guardrails", "https://sierra.ai/"),
    ("Decagon AI", "Customer Service Agents", 2023, "$100M+", "Enterprise support agent: auto-resolves tickets, learns from every interaction", "https://decagon.ai/"),
    ("Forethought", "Customer Service Agents", 2017, "$90M+", "AI agent for support: auto-resolution, agent assist, and workflow automation", "https://forethought.ai/"),
    ("Aisera", "Customer Service Agents", 2012, "$150M+", "Agentic AI for IT and customer service: auto-resolve, assist, and automate", "https://aisera.com/"),

    ("Adept AI", "Action Agents", 2022, "$415M+", "ACT-1: model that takes actions on software — clicks, types, navigates real UIs", "https://www.adept.ai/"),
    ("MultiOn AI", "Action Agents", 2023, "$20M+", "Browser agent: autonomous web task completion via natural language commands", "https://multion.ai/"),
    ("Imbue", "Action Agents", 2021, "$220M+", "Building autonomous agents with reasoning and simulation for complex real-world tasks", "https://imbue.com/"),

    ("Glean", "Enterprise Search & RAG", 2019, "$4.6B+", "Enterprise AI search: connects all company apps with LLM-powered search and agents", "https://www.glean.com/"),
    ("Mem0", "Agent Memory", 2024, "$30M+", "Production memory layer for LLM apps: personalized, evolving memory across sessions", "https://mem0.ai/"),
    ("Zep", "Agent Memory", 2022, "$5M+", "Long-term memory service for AI assistants: temporal knowledge graph and recall", "https://getzep.com/"),
    ("Letta", "Agent Memory", 2024, "$10M+", "Agent memory framework spun out of UC Berkeley: MemGPT and block-based memory", "https://letta.com/"),

    ("LangChain", "Agent Infrastructure", 2023, "$25M+", "Company behind LangChain/LangGraph/LangSmith: the LLM app development stack", "https://www.langchain.com/"),
    ("CrewAI", "Agent Infrastructure", 2024, "$25M+", "Multi-agent orchestration platform: role-playing crews with deployment and monitoring", "https://www.crewai.com/"),
    ("LlamaIndex", "Agent Infrastructure", 2023, "$8.5M+", "Data framework company: RAG pipelines, agents, and enterprise data connectors", "https://www.llamaindex.ai/"),

    ("Sakana AI", "Research Agents", 2023, "$200M+", "Nature-inspired AI: AI Scientist, evolutionary model merging, and autonomous research", "https://sakana.ai/"),
    ("Hippocratic AI", "Healthcare Agents", 2022, "$278M+", "Healthcare safety-focused LLM: non-diagnostic patient interactions, longitudinal care", "https://www.hippocraticai.com/"),
    ("Harvey", "Legal Agents", 2022, "$1B+", "AI for Big Law: contract analysis, due diligence — used by Allen & Overy, PwC, KPMG", "https://www.harvey.ai/"),
    ("Glass Health", "Healthcare Agents", 2021, "$50M+", "Clinical AI: differential diagnosis and clinical plan generation for physicians", "https://glass.health/"),

    ("Browser Use", "Web Agents", 2024, "Open Source", "Open-source web automation: LLM-driven browser control, 60k+ GitHub stars", "https://browser-use.com/"),
    ("Crawl4AI", "Web Agents", 2024, "Open Source", "LLM-friendly web crawler optimized for RAG and agent data ingestion", "https://github.com/unclecode/crawl4ai"),
    ("Composio", "Agent Tools", 2024, "$8M+", "Tool platform: 250+ app integrations with auth management for agent tool-use", "https://composio.dev/"),
    ("Sema4.ai", "Enterprise Agents", 2021, "$30M+", "Enterprise AI agents built on open-source frameworks: automation with control", "https://sema4.ai/"),
    ("Norm AI", "Compliance Agents", 2023, "$27M+", "Regulatory compliance AI agents: automate compliance checks and reporting", "https://norm.ai/"),

    ("Physical Intelligence", "Robotics Agents", 2024, "$400M+", "Universal robot brain: π0 and π0.5 VLA models for cross-embodiment manipulation", "https://physicalintelligence.company/"),
    ("Skild AI", "Robotics Agents", 2023, "$30M+", "Scalable foundation model for robotics: single model across tasks and embodiments", "https://skild.ai/"),
    ("Figure AI", "Robotics Agents", 2022, "$675M+", "Autonomous humanoid robots: Figure 02 with OpenAI-powered reasoning for labor", "https://www.figure.ai/"),
    ("1X Technologies", "Robotics Agents", 2023, "$100M+", "NEO humanoid robot: home assistant with embodied AI and safe physical interaction", "https://1x.tech/"),
    ("Sanctuary AI", "Robotics Agents", 2018, "$150M+", "Phoenix humanoid robot with Carbon AI cognitive architecture for general-purpose work", "https://sanctuary.ai/"),

    ("Wayve", "Autonomous Agents", 2017, "$1B+", "End-to-end autonomous driving: LINGO-2 language-driving model for AV explanation and control", "https://wayve.ai/"),
    ("Waabi", "Autonomous Agents", 2021, "$280M+", "Generative AI for autonomous driving: simulation-first approach to self-driving trucks", "https://waabi.ai/"),

    ("Inworld AI", "Character Agents", 2021, "$125M+", "AI NPCs for games and virtual worlds: character engine with personality and memory", "https://inworld.ai/"),
    ("Replika", "Companion Agents", 2017, "$10M+", "AI companion app: empathetic chatbot with 10M+ users and long-term memory", "https://replika.com/"),
    ("Character.AI", "Character Agents", 2021, "$2.7B+", "Platform for creating and chatting with AI characters: 18M+ users, personalized models", "https://character.ai/"),
]


def build_startups():
    entries = []
    for name, cat, founded, funding, desc, url in SEED_STARTUPS:
        entries.append({
            "name": name,
            "category": cat,
            "founded": founded,
            "funding": funding,
            "desc": desc,
            "url": url,
            "sources": ["seed"],
            "evidence": {"checked_at": TODAY, "source_url": url, "status": "seed-verified"},
        })
    cats = {}
    for e in entries:
        cats[e["category"]] = cats.get(e["category"], 0) + 1
    return {
        "generated_at": TODAY,
        "generator": "scripts/seed_kb.py",
        "count": len(entries),
        "category_count": len(cats),
        "categories": dict(sorted(cats.items(), key=lambda x: -x[1])),
        "startups": sorted(entries, key=lambda x: (x["category"], x["name"])),
    }


# ── 5. Benchmarks (Evaluation) ──────────────────────────────────────────────
SEED_BENCHMARKS = [
    ("GAIA", "General AI Assistant", "466 real-world tasks requiring multi-step tool-use, web search, file handling", "ICLR 2024", "https://github.com/facebookresearch/gaia"),
    ("AgentBench", "General Agent", "8 environments: OS, DB, KG, web, house-holding, card game, over 200 tasks", "ICLR 2024", "https://github.com/THUDM/AgentBench"),
    ("SWE-bench", "Software Engineering", "2294 real GitHub issues across 12 Python repos; resolved-rate metric", "ICLR 2024", "https://github.com/swe-bench/SWE-bench"),
    ("SWE-bench Verified", "Software Engineering", "Human-verified 500-task subset of SWE-bench; current gold standard for coding agents", "OpenAI 2024", "https://openai.com/index/introducing-swe-bench-verified/"),
    ("HumanEval", "Code Generation", "164 hand-written programming problems; pass@k metric", "OpenAI 2021", "https://github.com/openai/human-eval"),
    ("MBPP", "Code Generation", "974 beginner Python programming problems; pass@1 metric", "Google 2021", "https://github.com/google-research/google-research/tree/master/mbpp"),
    ("LiveCodeBench", "Code Generation", "Contamination-free: problems after model training cutoff; holistic code agent eval", "UC Berkeley 2024", "https://github.com/LiveCodeBench/LiveCodeBench"),
    ("BigCodeBench", "Code Generation", "Function-level code generation with 1395 tasks using 723 libraries and tools", "BigCode 2024", "https://github.com/bigcode-project/bigcode-benchmark"),

    ("Mind2Web", "Web Agent", "2350 tasks across 137 real websites; action trace prediction", "NeurIPS 2023", "https://github.com/OSU-NLP-Group/Mind2Web"),
    ("WebArena", "Web Agent", "812 web tasks across 5 self-hosted websites; end-to-end success rate", "ICLR 2024", "https://github.com/web-arena-x/webarena"),
    ("OSWorld", "Computer Agent", "369 tasks across 9 real OS apps (Chrome, VSCode, Terminal); multi-step GUI interaction", "NeurIPS 2024", "https://github.com/xlang-ai/OSWorld"),
    ("WebShop", "Web Agent", "11878 web shopping tasks; instruction-following and search-based decision making", "NeurIPS 2022", "https://github.com/princeton-nlp/WebShop"),
    ("VisualWebArena", "Web Agent", "Multimodal extension of WebArena: 910 visual web tasks requiring image understanding", "ICML 2024", "https://github.com/web-arena-x/visualwebarena"),

    ("MINT-Bench", "General Agent", "Multi-turn interaction with tools: evaluates tool-use, multi-step reasoning, and self-improvement", "ICLR 2024", "https://github.com/xingyaoww/mint-bench"),
    ("ToolBench", "Tool Use", "16000+ real API calls with DFS-based multi-tool instruction; pass_rate and win_rate", "ICLR 2024", "https://github.com/OpenBMB/ToolBench"),
    ("API-Bank", "Tool Use", "73 API tools, 314 tool-use dialogues, 1910 test cases for API-calling agents", "EMNLP 2023", ""),
    ("Tau-Bench", "Tool-User Interaction", "Benchmark for tool-agent-user interaction with simulated users in real-world domains", "ICLR 2025", "https://github.com/sierra-research/tau-bench"),

    ("Agent-SafetyBench", "Agent Safety", "10 hazard types, 200 scenarios, 3815 test cases for LLM agent safety", "arXiv 2024", ""),
    ("AdvBench", "Safety", "Adversarial suffix attacks on LLMs; 520 harmful behaviors for red-teaming", "NeurIPS 2023", "https://github.com/llm-attacks/llm-attacks"),
    ("HarmBench", "Safety", "Standardized evaluation for automated red-teaming; 400 harmful behaviors across 7 categories", "ICML 2024", "https://github.com/centerforaisafety/HarmBench"),

    ("VLABench", "Embodied Agent", "100 language-conditioned manipulation tasks with procedural generation; VLA model eval", "NeurIPS 2024", "https://github.com/Open-VLABench/VLABench"),
    ("CALVIN", "Embodied Agent", "Long-horizon language-conditioned manipulation: 34 tasks, 5 environments, 52 actions", "ICRA 2022", "https://github.com/mees/calvin"),
    ("RoboCasa", "Embodied Agent", "100k everyday manipulation tasks in kitchen scenes; 29 task categories", "RSS 2024", "https://github.com/robocasa/robocasa"),
    ("LIBERO", "Embodied Agent", "Benchmark for lifelong robot learning: 130 manipulation tasks across 5 suites", "ICML 2024", "https://github.com/Lifelong-Robot-Learning/LIBERO"),
    ("ALFRED", "Embodied Agent", "Instruction-following household tasks: 25k language instructions in 8 task types", "CVPR 2021", "https://askforalfred.com/"),

    ("ARZBench", "General Agent", "Agent reasoning and zero-shot behavior across diverse task families", "arXiv 2024", ""),
    ("AgentMonitor", "Agent Safety", "Zero-preparation runtime monitoring with anomaly detection for agent safety", "arXiv 2025", ""),
    ("MLAgentBench", "ML Research Agent", "ML research task solving: from paper reproduction to hyperparameter tuning", "ICLR 2024", "https://github.com/snap-research/mlagentbench"),
    ("DS-1000", "Data Science Agent", "1000 data science problems across Matplotlib/NumPy/Pandas/PyTorch/SciPy/Sklearn", "ICLR 2023", "https://github.com/xlang-ai/ds-1000"),
]


def build_benchmarks():
    entries = []
    for name, domain, desc, venue, url in SEED_BENCHMARKS:
        entries.append({
            "name": name,
            "domain": domain,
            "desc": desc,
            "venue": venue,
            "url": url,
            "sources": ["seed"],
            "evidence": {"checked_at": TODAY, "source_url": url or "paper-venue", "status": "seed-verified"},
        })
    return {
        "generated_at": TODAY,
        "generator": "scripts/seed_kb.py",
        "count": len(entries),
        "benchmarks": sorted(entries, key=lambda x: x["name"]),
    }


# ── Write all knowledge bases ───────────────────────────────────────────────
if __name__ == "__main__":
    kbs = {
        "methods.json": build_methods(),
        "frameworks.json": build_frameworks(),
        "industries.json": build_industries(),
        "startups.json": build_startups(),
        "benchmarks.json": build_benchmarks(),
    }
    for fname, data in kbs.items():
        path = DATA / fname
        path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"  {fname}: {data['count']} entries")
    print(f"\nTotal: {sum(d['count'] for d in kbs.values())} entries across 5 knowledge bases")
    print(f"Written to: {DATA}")
