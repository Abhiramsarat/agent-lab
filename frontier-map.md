# Frontier Map

Honest running list: what I can do solo vs. what I still need help with. This is my real measure of progress and my Day-100 deliverable.

## ✅ What I can do solo (as of 2026-06-28, end of Week 0)
- Direct Claude Code to build and run a small tool from plain English.
- Read a project's structure (repo, `.env`, `requirements.txt`, virtual environment) and know what each part is for.
- Make savepoints (git commits) and back up to GitHub.
- Deploy a simple app to the internet, and reason about *why* a deployment error happens.

## 🧗 What I still need help with (the climb ahead)
- Build an agent that decides its **own** steps — tool use, a goal, a loop. *(Phase 1 — next)*
- Connect an agent to my real data via MCP. *(Phase 2)*
- Automate a full process end-to-end (client reporting). *(Phase 3)*
- Orchestrate multiple agents handing off. *(Phase 4)*

## 🗺️ MyCA frontier (Phase 0 finding, 2026-06-28)
MyCA is a **scripted pipeline** (Intake → Dossier → Session → Design → Brief). It exercises *model* judgment at only **two** owned points — `extract-document` and the `signal hunter` — and the actual words are written by **Lovable** (external). The biggest "hand it to the model" opportunities: the **Brain** (rules today) and the **fixed orchestration itself** (the plan's "give up the control flow").

## 💰 Economic-impact watchlist (from the MyCA dissection)
- **Signal hunter** — *highest* payoff. The moat: turns generic → bespoke in one cheap AI call that self-skips. **Keep & strengthen.**
- **Document extraction** — *high* payoff. Kills manual data entry, captures signal no form could; human-curated, so safe. **Keep.**
- **The Brain (Dossier)** — scripted rules today; the best **candidate to hand to the model** (the Phase-0 reflection answer). Weigh cost vs. control.
- **Content writing** — outsourced to Lovable. Strategic question: how much to pull in-house via the four-trigger enrichment.
