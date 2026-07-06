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

## ⚡ MyCA v2 + agentic target (updated 2026-06-29)
Fable rewired MyCA to v2 — the frontier moved:
- **4 AI call sites now:** `extract-document`, **`hunt-signal` (now the inference engine** — thesis / hero / headings / hierarchy, runs for EVERY firm), **`audit-brief` (NEW** — verification loop flagging MISSING / CONFLICT / UNVERIFIED), `scrape-website`.
- **Agentic target:** an *orchestrator agent* owns each firm's journey to a goal state ("a brief that passes the audit + expresses the firm's distinguishing signal"), decides next steps, calls the existing functions as tools, and pauses at human gates. `stage` becomes derived status, not the control flow.
- **THE FIRST AGENTIC BUILD (beachhead): the `compile → audit → repair → recompile` loop** (cap 2–3). This is the **evaluator-optimizer** pattern — the exact one Phase 0 flagged as MyCA's *missing* pattern. Machine-side (no UX change), bounded, fail-open, crisp success (audit clean). Proof demo: a firm with a planted conflict repairs itself, each step logged to a new `agent_log` column.
- **Invariants (never break):** ICAI compliance is law; authority hierarchy holds (compliance > firm directives > firm-confirmed > inference > defaults); never invent facts; human gates stay (doc curation, session, final send); cost discipline (**Sonnet, not Opus**; bounded loops); determinism via seed = firmName|city|practices; fail-open; `firms` table is the single source of truth.
