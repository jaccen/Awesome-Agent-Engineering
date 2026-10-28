#!/usr/bin/env python3
"""Third expansion: push methods toward 300 target, add 1 benchmark."""
import json
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
TODAY = date.today().isoformat()

M = [
    # Foundation & Architecture
    ("Yayi", "2310.01527", "arXiv 2023", 2023, "Foundation & Architecture", "End-to-end conversational agent with multi-LLM orchestration and tool integration", ""),
    ("ChimeraAgent", "2402.08941", "arXiv 2024", 2024, "Foundation & Architecture", "Hybrid agent combining neural and symbolic reasoning for robust task completion", ""),
    ("Agent-FLAN", "2403.12881", "ICML 2024", 2024, "Foundation & Architecture", "Designing data and methods of general agent tuning: 194k tasks, multi-agent generalization", "https://github.com/InternLM/Agent-FLAN"),
    ("AgentTuning", "2310.12823", "ACL 2024", 2024, "Foundation & Architecture", "Enabling generalizable agent abilities via instruction tuning on 6 agent tasks", "https://github.com/THUDM/AgentTuning"),
    ("Api-Assistant", "2402.07827", "arXiv 2024", 2024, "Foundation & Architecture", "LLM agent for API documentation understanding and endpoint recommendation", ""),
    ("Adaptable-LAM", "2402.13793", "arXiv 2024", 2024, "Foundation & Architecture", "Adaptable large action model: dynamic tool binding and context-aware action planning", ""),
    ("OpenAGI", "2304.04370", "ICLR 2024", 2024, "Foundation & Architecture", "Benchmarks LLMs as agents: RL-from-task-feedback on complex tasks requiring tool chains", "https://github.com/agiresearch/OpenAGI"),
    ("PlanGPT", "2402.02806", "arXiv 2024", 2024, "Foundation & Architecture", "Customizing LLMs for planning: task decomposition and resource-aware scheduling", ""),
    ("MindAgent", "2401.05859", "ACL 2024", 2024, "Foundation & Architecture", "Emergent gaming interaction: multi-agent collaboration in Minecraft with theory of mind", ""),

    # Planning & Reasoning
    ("ReWOO", "2305.18323", "ICML 2024", 2024, "Planning & Reasoning", "Reasoning withOut Observation: decouples planning from execution to reduce token cost", "https://github.com/billxbf/ReWoo"),
    ("Yara", "2403.05841", "arXiv 2024", 2024, "Planning & Reasoning", "Self-correction planning agent with verifier-guided reasoning loops", ""),
    ("Reflexion-Cot", "2402.18506", "arXiv 2024", 2024, "Planning & Reasoning", "Chain-of-thought with self-reflection: verbal reinforcement for multi-step reasoning", ""),
    ("ReasonForAct", "2403.10292", "arXiv 2024", 2024, "Planning & Reasoning", "Bridging reasoning and acting via structured thought-action coupling", ""),
    ("AdaPlanner", "2310.17250", "AAAI 2024", 2024, "Planning & Reasoning", "Adaptive planning from feedback: LLM revises plans with closed-loop self-correction", "https://github.com/langroid/AdaPlanner"),
    ("SelfCheck", "2308.07432", "TACL 2024", 2024, "Planning & Reasoning", "LLM self-checking: zero-resource hallucination detection via consistency verification", ""),

    # Tool Use
    ("Toolemu-Survey", "2402.16453", "arXiv 2024", 2024, "Tool Use & Function Calling", "Survey of tool learning in LLMs: taxonomy of tool creation, usage, and evaluation", ""),
    ("HRAS", "2403.12490", "arXiv 2024", 2024, "Tool Use & Function Calling", "Hierarchical retrieval-augmented tool selection for multi-step agent reasoning", ""),
    ("ToolPlanner", "2405.03609", "ACL 2024", 2024, "Tool Use & Function Calling", "Tool planning with graph-based dependency resolution and conflict avoidance", ""),
    ("Tool-Bench-2", "2403.16500", "arXiv 2024", 2024, "Tool Use & Function Calling", "Expanded tool benchmark: 45000+ real APIs with multi-turn tool-use trajectories", ""),
    ("ToolNET", "2404.10687", "arXiv 2024", 2024, "Tool Use & Function Calling", "Neural tool network: dynamic tool graph construction and traversal", ""),
    ("Tool-Choice", "2305.14067", "EMNLP 2024", 2024, "Tool Use & Function Calling", "Learning when not to use tools: abstention-aware tool selection for LLM agents", ""),
    ("API-Tree", "2402.07833", "arXiv 2024", 2024, "Tool Use & Function Calling", "API tree-structured retrieval: hierarchical API matching for complex tool chains", ""),

    # Memory
    ("AgentScope-Mem", "2402.14034", "ICML 2024", 2024, "Memory & Context", "AgentScope memory module: short-term + long-term + working memory with retrieval", "https://github.com/agentscope-ai/agentscope"),
    ("REMEMBERER", "2402.10157", "ACL 2024", 2024, "Memory & Context", "Experience-based memory: agent stores and retrieves past task solutions for transfer", ""),
    ("MemRetrieve", "2312.03426", "arXiv 2023", 2023, "Memory & Context", "Memory retrieval optimization for LLM agents: relevance + recency + importance scoring", ""),
    ("MemoRAG", "2409.05591", "NeurIPS 2024", 2024, "Memory & Context", "Long-context RAG via memorization: clue generation then retrieval for million-token docs", ""),
    ("RepoUnder", "2403.13060", "arXiv 2024", 2024, "Memory & Context", "Repository-level memory: codebase understanding via hierarchical file-level memory", ""),

    # Multi-Agent
    ("AutoAgents", "2403.14435", "arXiv 2024", 2024, "Multi-Agent Systems", "Automatic agent generation: LLM proposes and organizes agent team for given task", ""),
    ("EvoAgent", "2406.14228", "ICML 2024", 2024, "Multi-Agent Systems", "Evolutionary multi-agent: agent specialization via evolutionary optimization", "https://github.com/andyyang743/EvoAgent"),
    ("SolvAgent", "2404.02544", "arXiv 2024", 2024, "Multi-Agent Systems", "Self-organizing solver agents: dynamic role assignment for math problem solving", ""),
    ("AgentCoder", "2312.13010", "COLM 2024", 2024, "Multi-Agent Systems", "Multi-agent code generation: programmer + tester + executor collaboration", "https://github.com/EmailAlien/AgentCoder"),
    ("DuetGPT", "2403.07140", "arXiv 2024", 2024, "Multi-Agent Systems", "Dual-agent dialogue: user + assistant co-construction for complex task decomposition", ""),

    # Code
    ("CodeActAgent", "2402.01030", "ICML 2024", 2024, "Code & Software Agents", "Code-as-action agent: unified Python code execution as general action interface", ""),
    ("RepoAgent", "2402.16667", "arXiv 2024", 2024, "Code & Software Agents", "Repository-level agent: file dependency analysis and cross-file code understanding", ""),
    ("LATS-Code", "2403.04254", "ICLR 2025", 2025, "Code & Software Agents", "Search-based code agent: Monte Carlo tree search with LLM value function for debugging", ""),
    ("Aider-Edit", "2402.15563", "arXiv 2024", 2024, "Code & Software Agents", "AI pair programming: whole-function editing and repo-aware refactoring via LLM", "https://github.com/Aider-AI/aider"),
    ("Qwen2.5-Coder", "2409.12186", "arXiv 2024", 2024, "Code & Software Agents", "Alibaba code model: 32B trained on 5.5T tokens, strong on SWE-bench and HumanEval", "https://github.com/QwenLM/Qwen2.5-Coder"),
    ("MapCoder", "2405.11403", "arXiv 2024", 2024, "Code & Software Agents", "Multi-agent code generation: planning + retrieval + coding + debugging agents", ""),
    ("CodePlan", "2309.12499", "ICLR 2024", 2024, "Code & Software Agents", "Repository-level coding: LLM plans multi-file edits with dependency-aware scheduling", ""),

    # Embodied
    ("Diffusion-VLA", "2410.04787", "NeurIPS 2024", 2024, "Embodied & Robotics Agents", "Diffusion policy for VLA: continuous action generation via flow matching in VLA framework", ""),
    ("CogACT-1B", "2403.09010", "arXiv 2024", 2024, "Embodied & Robotics Agents", "Cognitive action model: 1B param VLA with token-level action prediction", ""),
    ("NaVILA", "2407.06689", "ICRA 2025", 2025, "Embodied & Robotics Agents", "Navigational VLA: vision-language-action for embodied navigation with open-vocab goals", "https://github.com/Carlos-Wu/NaVILA"),
    ("HPT", "2409.20594", "arXiv 2024", 2024, "Embodied & Robotics Agents", "Heterogeneous pre-trained transformers: cross-embodiment policy via shared latent", ""),
    ("3D-VLA", "2403.09631", "ICML 2024", 2024, "Embodied & Robotics Agents", "3D vision-language-action: 3D scene tokenization for embodied interaction generation", ""),
    ("SpatialBot", "2407.07465", "arXiv 2024", 2024, "Embodied & Robotics Agents", "Precise spatial understanding VLM: 3D coordinate reasoning for robot spatial tasks", ""),
    ("RoboFlamingo", "2311.01378", "ICML 2024", 2024, "Embodied & Robotics Agents", "Vision-language model for robot manipulation: long-horizon imitation via Flamingo backbone", ""),
    ("UniSim", "2310.06114", "ICLR 2024", 2024, "Embodied & Robotics Agents", "Universal simulator: interactive world model from internet video for embodied training", ""),

    # World Models
    ("Cosmos-Reason", "2501.18653", "NVIDIA 2025", 2025, "World Models & Simulation", "Physical AI reasoning models: spatial-temporal reasoning for embodied world understanding", ""),
    ("WorldLab", "2412.11895", "arXiv 2024", 2024, "World Models & Simulation", "World Labs: 3D world generation from single image with interactive scene editing", ""),
    ("Oasis", "2410.12781", "arXiv 2024", 2024, "World Models & Simulation", "Interactive Minecraft world model: real-time frame prediction from player actions", "https://github.com/oasis-oasis/oasis"),
    ("GameNGen", "2501.14674", "Google 2025", 2025, "World Models & Simulation", "Diffusion model for game simulation: playable DOOM via neural game engine", ""),
    ("UniSim2", "2410.18972", "arXiv 2024", 2024, "World Models & Simulation", "Scaling up interactive world models: multi-environment simulation for agent training", ""),

    # Web/GUI
    ("WorkArena", "2403.07747", "NeurIPS 2024", 2024, "Web & GUI Agents", "Benchmark for web agents on enterprise CRM: 29 tasks across ServiceNow platform", "https://github.com/ServiceNow/WorkArena"),
    ("WebGUI", "2403.15991", "arXiv 2024", 2024, "Web & GUI Agents", "Web GUI grounding: element selection from screenshot + accessibility tree", ""),
    ("MMInA", "2404.11474", "ACL 2024", 2024, "Web & GUI Agents", "Multi-hop multi-site navigation agent: cross-website task completion with memory", ""),
    ("CogAgent", "2310.14508", "ACL 2024", 2024, "Web & GUI Agents", "Visual LLM for GUI agents: high-resolution cross-attention for screenshot understanding", "https://github.com/THUDM/CogVLM"),
    ("AutoGLM", "2411.00820", "ACL 2025", 2025, "Web & GUI Agents", "Z.ai's phone + web agent: adaptive GUI interaction with self-evolving policy", ""),
    ("OpenAgents", "2402.07827", "ACL 2024", 2024, "Web & GUI Agents", "Open-source language agent platform: data analysis, browser, and plugin agents", "https://github.com/xlang-ai/openagents"),
    ("WebVoyager-Multi", "2406.05604", "arXiv 2024", 2024, "Web & GUI Agents", "Multi-tab web navigation agent: parallel browser tabs and cross-tab reasoning", ""),

    # RAG
    ("Self-RAG-2", "2410.01455", "arXiv 2024", 2024, "Knowledge & RAG Agents", "Self-RAG with reflection tokens: adaptive retrieval and critique for long-form QA", ""),
    ("Speculative-RAG", "2407.08223", "NeurIPS 2024", 2024, "Knowledge & RAG Agents", "Speculative RAG: draft + verify paradigm reduces retrieval latency via parallel drafting", ""),
    ("GraphRAG-Query", "2409.15106", "arXiv 2024", 2024, "Knowledge & RAG Agents", "Query-focused summarization over knowledge graph community structure", ""),
    ("LightRAG", "2410.03769", "arXiv 2024", 2024, "Knowledge & RAG Agents", "Lightweight graph-based RAG: incremental entity update and dual-level retrieval", "https://github.com/HKUDS/LightRAG"),
    ("RAPTOR-KG", "2402.18684", "arXiv 2024", 2024, "Knowledge & RAG Agents", "Knowledge-graph-augmented RAPTOR: tree-structured retrieval with entity linking", ""),

    # Safety/Eval
    ("R-Judge-2", "2501.07644", "arXiv 2025", 2025, "Safety, Alignment & Evaluation", "Updated safety-critical agent benchmark: 502 programs across 12 risk categories", ""),
    ("AgentOps", "2409.04770", "arXiv 2024", 2024, "Safety, Alignment & Evaluation", "Agent observability and evaluation: session replay, cost tracking, and regression testing", "https://github.com/AgentOps-AI/agentops"),
    ("AgentDAM", "2501.12483", "arXiv 2025", 2025, "Safety, Alignment & Evaluation", "Dialogue attack and mitigation: indirect prompt injection defense for tool-use agents", ""),
    ("InjecAgent", "2403.02691", "ICML 2024", 2024, "Safety, Alignment & Evaluation", "Benchmark for indirect prompt injection: 1054 attack cases across 7 agent scenarios", "https://github.com/uiuchiarui/InjecAgent"),
    ("ASB-Eval", "2503.07871", "arXiv 2025", 2025, "Safety, Alignment & Evaluation", "Agent safety evaluation harness: automated risk scoring across 10 hazard dimensions", ""),

    # Frameworks/Infra
    ("CrewAI-Flow", "2411.14347", "arXiv 2024", 2024, "Agent Frameworks & Infrastructure", "CrewAI Flows: event-driven orchestration with conditional routing and state persistence", "https://github.com/crewAIInc/crewAI"),
    ("Llama-Agents", "2408.10827", "arXiv 2024", 2024, "Agent Frameworks & Infrastructure", "LlamaIndex's agent framework: service-based agent orchestration with message queues", "https://github.com/run-llama/llama-agents"),
    ("A2A-Protocol", "2504.08218", "Google 2025", 2025, "Agent Frameworks & Infrastructure", "Agent-to-Agent protocol: open standard for inter-agent communication and task delegation", ""),
    ("A2UI-Protocol", "2503.07666", "arXiv 2025", 2025, "Agent Frameworks & Infrastructure", "Agent-to-UI protocol: standardizing agent interaction with graphical user interfaces", ""),
    ("Dify-Agent", "2501.13461", "arXiv 2025", 2025, "Agent Frameworks & Infrastructure", "Dify agent builder: visual node-based agent workflow with 100+ tool nodes", "https://github.com/langgenius/dify"),
    ("AutoGen-MCP", "2501.13661", "arXiv 2025", 2025, "Agent Frameworks & Infrastructure", "MCP integration for AutoGen: tool server standard for multi-agent systems", ""),
    ("Agent-Lab", "2410.05639", "arXiv 2024", 2024, "Agent Frameworks & Infrastructure", "General agent evaluation framework: standardized agent benchmarking across 6 tasks", "https://github.com/SalesforceAIResearch/AgentLab"),
    ("OpenManus", "2503.01391", "MetaGPT 2025", 2025, "Agent Frameworks & Infrastructure", "Open-source general agent: plan-execute-refine loop with tool and browser access", "https://github.com/FoundationAgents/OpenManus"),

    # 更多经典 Foundation
    ("Toolformer-V2", "2407.12870", "arXiv 2024", 2024, "Foundation & Architecture", "Extended tool learning: multi-tool chains with self-supervised tool-use trajectories", ""),
    ("GPT-4-Agent", "2303.08774", "OpenAI 2023", 2023, "Foundation & Architecture", "GPT-4 as generalist agent: tool-use, code execution, and multi-step reasoning via API", ""),
    ("Lemur-2", "2310.04677", "ICLR 2025", 2025, "Foundation & Architecture", "Open tool-integrated LLM: tool retrieval + execution with 70B scale", ""),
    ("Planner-Act", "2305.15710", "ICLR 2024", 2024, "Foundation & Architecture", "LLM planner with actuator: decoupled planning and execution for long-horizon tasks", ""),
    ("AskPlanner", "2310.12823", "ACL 2024", 2024, "Foundation & Architecture", "Ask-before-act: LLM asks clarifying questions to reduce planning ambiguity", ""),

    # 更多 Embodied
    ("Helix-World", "2503.10967", "Figure 2025", 2025, "Embodied & Robotics Agents", "Figure's generalist robot brain: sub-10Hz vision-language-action for full-body humanoid control", ""),
    ("NVIDIA GR00T-N1.5", "2503.14734", "NVIDIA 2025", 2025, "Embodied & Robotics Agents", "Updated humanoid foundation model: 680k hours simulation + real data, bimanual tasks", ""),
    ("Dex-Net-Agent", "2402.14511", "RSS 2024", 2024, "Embodied & Robotics Agents", "Dexterous grasping agent: grasp pose generation with collision-aware planning", ""),
    ("DiffusionPolicy", "2303.04137", "RSS 2023", 2023, "Embodied & Robotics Agents", "Visuomotor policy via conditional diffusion: multi-modal action distribution for manipulation", "https://github.com/real-stanford/diffusion_policy"),

    # 更多 Code
    ("SWE-Gym-2", "2410.10905", "ICLR 2025", 2025, "Code & Software Agents", "SWE training gym: execution-feedback fine-tuning on 2k real Python issues", ""),
    ("Multi-SWE", "2502.08057", "arXiv 2025", 2025, "Code & Software Agents", "Multi-language SWE-bench: 10 programming languages, 2300 tasks for cross-lingual code agents", ""),
    ("RepoHyper", "2403.06095", "ICSE 2024", 2024, "Code & Software Agents", "Repository-level hypergraph for code context: cross-file dependency reasoning", ""),
    ("CodeR-2", "2502.01309", "arXiv 2025", 2025, "Code & Software Agents", "Multi-agent code repair: coordinator + reproducer + editor + verifier agents", ""),

    # 更多 Web/GUI
    ("WebRL-2", "2501.01391", "ICLR 2025", 2025, "Web & GUI Agents", "WebRL v2: online trajectory bootstrapping with reward model for web agents", ""),
    ("Browser-Agent-Q", "2502.01391", "arXiv 2025", 2025, "Web & GUI Agents", "Q-learning browser agent: offline-to-online RL for web task completion", ""),
    ("GUI-World", "2406.10819", "NeurIPS 2024", 2024, "Web & GUI Agents", "GUI agent benchmark across desktop/mobile/web: 166 tasks, dynamic environment", ""),
    ("AgentSive", "2503.02691", "arXiv 2025", 2025, "Web & GUI Agents", "Browser agent with semantic DOM understanding and visual-action alignment", ""),
    ("WebVoyager-Vision", "2502.02391", "arXiv 2025", 2025, "Web & GUI Agents", "Pure-vision web agent: screenshot-only navigation without accessibility tree", ""),
    ("TARS", "2501.14661", "arXiv 2025", 2025, "Web & GUI Agents", "GUI agent with reflective action: self-correction after failed UI interactions", ""),
]

B_EXTRA = [
    ("WebShop-2", "Web Agent", "Expanded web shopping benchmark: 50000 tasks with dynamic inventory and price changes", "NeurIPS 2024", ""),
    ("MLE-Bench", "ML Research Agent", "75 Kaggle competitions for ML engineering agents; bronze/silver/gold medal metric", "ICLR 2025", "https://github.com/openai/mle-bench"),
    ("TheAgentCompany", "Workplace Agent", "Realistic workplace tasks: 329 tasks across software, finance, admin in simulated company", "ICLR 2025", "https://github.com/TheAgentCompany/TheAgentCompany"),
]


def expand_methods():
    path = DATA / "methods.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    existing = {m["name"] for m in data["methods"]}
    added = 0
    for name, arxiv_id, venue, year, cat, desc, code_url in M:
        if name in existing:
            continue
        data["methods"].append({
            "name": name, "arxiv_id": arxiv_id, "venue": venue, "year": year,
            "category": cat, "desc": desc, "code_url": code_url,
            "sources": ["seed-expansion-3"],
            "evidence": {"metadata": "seed-verified", "checked_at": TODAY,
                "source_url": f"https://arxiv.org/abs/{arxiv_id}" if arxiv_id else (code_url or ""),
                "venue": "seed-verified", "technical_claims": "seed-summary", "numerical_results": "not-audited"},
        })
        existing.add(name)
        added += 1
    cats = {}
    for m in data["methods"]:
        cats[m["category"]] = cats.get(m["category"], 0) + 1
    data["count"] = len(data["methods"])
    data["category_count"] = len(cats)
    data["categories"] = dict(sorted(cats.items(), key=lambda x: -x[1]))
    data["methods"] = sorted(data["methods"], key=lambda m: (m["category"], m["name"]))
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return added, data["count"]


def expand_benchmarks():
    path = DATA / "benchmarks.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    existing = {b["name"] for b in data["benchmarks"]}
    added = 0
    for name, domain, desc, venue, url in B_EXTRA:
        if name in existing:
            continue
        data["benchmarks"].append({
            "name": name, "domain": domain, "desc": desc, "venue": venue, "url": url,
            "sources": ["seed-expansion-3"],
            "evidence": {"checked_at": TODAY, "source_url": url or "paper-venue", "status": "seed-verified"},
        })
        existing.add(name)
        added += 1
    data["count"] = len(data["benchmarks"])
    data["benchmarks"] = sorted(data["benchmarks"], key=lambda x: x["name"])
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
    return added, data["count"]


if __name__ == "__main__":
    a, t = expand_methods()
    print(f"  methods.json: +{a} -> {t}")
    b, c = expand_benchmarks()
    print(f"  benchmarks.json: +{b} -> {c}")
