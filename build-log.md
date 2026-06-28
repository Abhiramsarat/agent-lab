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
