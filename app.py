"""Composition root for Agentic Pricing Engine.

Menu items map 1:1 to capabilities in src/pricing_agent/agents/. A capability is
added here only after its ADR is written and its notebook logic has been ported —
see README.md for the workflow. Nothing below is implemented yet; this is a
placeholder skeleton, not a working menu.
"""

CAPABILITIES = {
    # "1": ("Baseline prompt-only pricing agent", "pricing_agent.agents.baseline"),
    # "2": ("RAG pricing agent (chunking strategies)", "pricing_agent.agents.rag"),
}


def main():
    if not CAPABILITIES:
        print("No capabilities ported yet. See README.md workflow: notebook -> ADR -> src/ -> app.py.")
        return

    print("Agentic Pricing Engine")
    for key, (label, _) in CAPABILITIES.items():
        print(f"  {key}. {label}")


if __name__ == "__main__":
    main()
