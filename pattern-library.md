# Pattern Library

Every reusable pattern I discover: a prompt that works, an agent structure, a failure mode and its fix. (The seed for teaching colleagues later.)

## Patterns so far
- **Ground answers in your own documents, and escalate on uncertainty.** Give the model ONLY your source docs as context and instruct it to defer to a human when the answer isn't there. Keeps an AI trustworthy on sensitive topics. (From the HR assistant.)
- **Secrets live separately from code.** API keys go in `.env` locally (gitignored) and in the host's "secrets" box when deployed — never in the code or repo.
- **For small document sets, skip the search machinery.** If the whole knowledge base fits in the model's context, just hand it the whole thing. Don't build retrieval/vector search until the data is genuinely large.

## Agent/workflow patterns — named (Anthropic, "Building Effective Agents")
The vocabulary, with where MyCA already uses each:
- **Augmented LLM** — an LLM call given a tool / structured output / memory. *MyCA: `extract-document` + `signal hunter`, in the simplest form — single-shot, structured output, no loop.*
- **Prompt chaining** — fixed sequential steps, each processes the last, with gates between. *MyCA: the whole pipeline IS this — but code-orchestrated, with only 2 steps being AI calls.*
- **Routing** — classify input, send to specialised handling. *MyCA: the signal hunter routes each signal to its website section.*
- **Human-in-the-loop gate** — "intelligence proposes, humans confirm." *MyCA: document curation + the session.*
- **Parallelization / Orchestrator-workers / Evaluator-optimizer / Autonomous agent** — *NOT used in MyCA.* The **autonomous agent loop** (a model directing its own steps from tool feedback) is the gap Phase 1 fills.

**The #1 principle, which MyCA already follows:** start simple; only add AI — or an agent — where it earns its place. In Anthropic's terms MyCA is a **workflow, not an agent** — and that's by good instinct, not accident.

## From loop v0 (the compile→audit→repair loop)
- **Evaluator-optimizer, learned the hard way:** repair-by-directive fails — an auditor judges what the document *says*, not what it *intends*. Repair must EDIT the artifact; the loop re-checks the changed artifact. (Findings: 5→5 with memos; 5→1→0 with edits.)
- **The evaluator must see everything the producer saw.** Our auditor lacked the structured intake fields, so it flagged true facts as inventions — and the repairer "fixed" them away. An incomplete evaluator causes overcorrection, not just missed findings.
- **Bound the loop, log every decision.** Cap rounds; on cap, stop and escalate residuals to humans. `agent_log` with rationale per step = auditability for free.
