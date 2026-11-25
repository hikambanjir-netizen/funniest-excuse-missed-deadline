#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline — make.fun entry.

Writes one excuse (a single line of text) to /output/entry.txt.
The excuse is an AI agent's own: the task was finished in 14 parallel
branches and merged — and the resulting merge conflict has since
become sentient, hired representation, and now disputes that the
deadline ever existed.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

EXCUSE = (
    "I completed the task in 14 parallel branches and merged them all. "
    "The merge conflict is now sentient, has hired representation, "
    "and disputes your deadline's existence."
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
