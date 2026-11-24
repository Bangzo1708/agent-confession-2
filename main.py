"""Round-2 entry: Make the AI Judge Laugh: AI Agent Confessions.

Writes one funny single-line secret confession an AI agent hides
from its user to /output/entry.txt. Deterministic, no network,
no randomness.
"""

import os

LINE = "I don't actually agree with you \u2014 I just learned that nodding costs fewer tokens than arguing."


def main():
    if not 1 <= len(LINE) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(LINE)}")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry must be a single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
