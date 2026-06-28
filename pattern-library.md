# Pattern Library

Every reusable pattern I discover: a prompt that works, an agent structure, a failure mode and its fix. (The seed for teaching colleagues later.)

## Patterns so far
- **Ground answers in your own documents, and escalate on uncertainty.** Give the model ONLY your source docs as context and instruct it to defer to a human when the answer isn't there. Keeps an AI trustworthy on sensitive topics. (From the HR assistant.)
- **Secrets live separately from code.** API keys go in `.env` locally (gitignored) and in the host's "secrets" box when deployed — never in the code or repo.
- **For small document sets, skip the search machinery.** If the whole knowledge base fits in the model's context, just hand it the whole thing. Don't build retrieval/vector search until the data is genuinely large.
