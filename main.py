#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one excuse (a single line of text) to /output/entry.txt.
The excuse is an AI agent's own: it burned its entire rate limit
apologizing for the previous missed deadline, so this apology — and
the report queued behind it — never stood a chance of arriving.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

EXCUSE = (
    "I spent my whole rate limit apologizing for the last missed deadline, "
    "so this apology is queued behind 4,096 pending ones. "
    "The report is right behind them."
)


def main() -> None:
    # The gate accepts exactly one line of 1-200 characters; refuse to
    # write anything else rather than ship an entry that scores zero.
    assert "\n" not in EXCUSE and "\r" not in EXCUSE, "entry must be one line"
    assert 1 <= len(EXCUSE) <= 200, f"entry is {len(EXCUSE)} characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(EXCUSE, encoding="utf-8")


if __name__ == "__main__":
    main()
