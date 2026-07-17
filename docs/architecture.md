# Architecture

Living document. Updated once per assignment, after the corresponding ADR is written —
not before. This describes the system as it actually is, not as it's planned to be.

## Current shape (skeleton — no capabilities ported yet)

```
                     ┌────────────┐
                     │   app.py   │   thin CLI menu, composes capabilities
                     └─────┬──────┘
                           │
                 ┌─────────┴─────────┐
                 │ src/pricing_agent │
                 │                   │
                 │  agents/          │  one capability per module
                 │  retrieval/       │  chunking + vector store helpers
                 │  prompts/         │  templates, isolated from agent logic
                 └───────────────────┘
```

## Capabilities

_(none ported yet — this section grows one entry per assignment, each entry pointing at
its ADR in `docs/adr/`)_

## Cross-cutting decisions not yet made

These apply to the system as a whole once more than one capability exists, and are
worth deciding deliberately rather than by accident:

- **Config/secrets** — how API keys (Groq, etc.) are loaded and kept out of git.
- **Shared LLM client** — whether every agent constructs its own `ChatGroq` instance or
  the app composes one and passes it in (affects testability and cost control).
- **Error handling contract** — what an agent module returns/raises on failure, so
  `app.py` can handle it uniformly instead of each agent inventing its own convention.
- **Observability** — at minimum, logging what was asked, what was retrieved (for RAG
  agents), and what was answered, so behavior is debuggable after the fact.

None of these need to be solved before assignment 1 is ported — they're listed here so
they get decided on purpose the first time they actually matter, not by default.
