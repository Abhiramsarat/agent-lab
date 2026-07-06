# Build Log

One or two lines per day: what I built, what broke, what I learned.

## 2026-06-28 — Week 0 (Environmental fluency) + side-quest
- Set up the Agent-Lab learning lab; built and ran first tools (headline rewriter, HR assistant).
- Deployed the HR assistant to the internet (Streamlit Cloud); debugged a real deploy error (the cloud app had no secret key — it needs its own copy, separate from the laptop's `.env`).
- Decision: HR is a side-quest, not part of the 100-day plan. Rejoining the plan's spine at Phase 0 (dissect MyCA).

## 2026-06-28 — Phase 0: dissected MyCA
- Read the MyCA architecture brief; drew the pipeline-vs-agent frontier map (one-page diagram = the deliverable).
- Finding: scripted pipeline with 2 owned AI-judgment points (`extract-document`, `signal hunter`); the words are written by Lovable (external).
- Reflection answer — which scripted steps could I now hand to the model? The **Brain** (Dossier), and the **fixed orchestration** itself.
- Closed Phase 0: read Anthropic's tool-use docs + "Building Effective Agents" against the map. Classified MyCA as a **workflow** (prompt chaining + routing + human gates + 2 single-shot augmented-LLM calls), not an agent. The gap = the autonomous agent loop → Phase 1. **Phase 0 COMPLETE.**

## 2026-06-28 (cont.) — Phase 1 started: Positioning Teardown Agent
- Built `projects/teardown-agent/` — first REAL agent: one tool (`fetch_url`), a goal, a manual agentic loop that prints each step so you watch the model choose. First run got cut off by a tool-permission glitch (code is fine; just needs a re-run).

## 2026-06-29 — MyCA v2 processed; agentic Phase-1 target set
- Processed the MyCA v2 architecture + transformation brief. v2 added `audit-brief` (verification loop) and turned `hunt-signal` into the inference engine (runs for every firm).
- Placement: the brief's recommended beachhead — the **compile → audit → repair → recompile loop** — IS a Phase 1 agent loop (the *evaluator-optimizer* pattern we named as MyCA's gap). Converges plan + economics + the brief's own "build this first."
- Constraint reset for MyCA work: **Sonnet not Opus**, bounded loops, human gates, fail-open, log to `agent_log`.
- Next: locate the MyCA codebase, then build loop v0.

## 2026-06-29 (cont.) — Agentic sprint: sandbox up, compile extracted
- MyCA v2 export copied to `sandbox/myca/` (gitignored — proprietary code never touches the public repo).
- Installed Node.js (the JavaScript runner) via nvm.
- **Extracted `compileBrief` verbatim** (BriefPage.jsx lines 28–676 → `sandbox/loop-v0/compile.mjs`) and smoke-tested: 16 sections compile outside the browser. The brief's stated prerequisite for loop v0 is met — an agent can now recompile without a human clicking.
