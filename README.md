# Agentic Pricing Engine

_(GitHub repo: `agentic_pricing_engine`)_

A single, evolving Pricing Agent, built one course assignment at a time. Each assignment
in the Agentic AI course adds a capability to the same conceptual product instead of
existing as a disconnected script — by the end, this repo should read as one coherent
system whose design history you can explain end to end.

## Status

| Capability | Assignment | Notebook | Ported to `src/` | ADR |
|---|---|---|---|---|
| Prompt-only reasoning | 1 | [`notebooks/assignment_1_baseline_prompting.ipynb`](notebooks/assignment_1_baseline_prompting.ipynb) | not yet | not yet |
| RAG with chunking strategies | 2 | [`notebooks/assignment_2_rag_chunking.ipynb`](notebooks/assignment_2_rag_chunking.ipynb) | not yet | not yet |

## How this repo works

**Two layers, on purpose:**

- `notebooks/` — the lab. This is where you do the actual course exercises yourself,
  exactly as assigned. Nothing here gets touched or "cleaned up" on your behalf — it's
  your learning record and stays messy/exploratory by design.
- `src/pricing_agent/` — the product. Once a notebook's capability is understood and
  working, it gets *deliberately* re-implemented here in a cleaner, tested, reusable
  form and wired into `app.py`. This is the part a stranger (or interviewer) could read
  and understand without having sat through the course.

**Why split them:** notebooks optimize for fast iteration and are allowed to be
throwaway; production-shaped code optimizes for being read, tested, and extended later.
Conflating the two is how notebooks either never get productionized, or `src/` ends up
full of one-off exploration code nobody trusts. Keeping them physically separate keeps
each honest about its job.

## Workflow per assignment

1. **You** work through the assignment notebook yourself in `notebooks/`.
2. **We review** what you built: what pattern you used, why, and what an alternative
   approach would have looked like (including how it'd need to change for real
   production use — cost, latency, failure handling, observability).
3. **We write one ADR** (see `docs/adr/`) capturing the decision and trade-offs, before
   any production code is written.
4. **Only after you approve the design** does the capability get ported into
   `src/pricing_agent/` as clean, tested code.
5. **`app.py` is updated** so the whole system still runs end-to-end with the new
   capability included.
6. `docs/architecture.md` gets a short update reflecting the new shape of the system.

## Running the app

```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

`requirements.txt` starts empty and grows only as a capability is actually ported into
`src/` — we don't pre-install dependencies for code that doesn't exist yet.

## Project layout

```
notebooks/            course exercises, as assigned — never refactored on your behalf
docs/
  architecture.md      living HLD description of the whole system, updated per assignment
  adr/                 one Architecture Decision Record per significant design choice
src/pricing_agent/
  agents/              one module per agent capability (baseline, rag, ...)
  retrieval/           chunking / vector store code shared by retrieval-based agents
  prompts/             prompt templates, kept out of agent logic so they're reviewable on their own
tests/                 one test module per src module
app.py                 thin entrypoint: a CLI menu that composes whatever capabilities exist so far
```
