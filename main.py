#!/usr/bin/env python3
"""make.fun entry: write the plan to entry.txt.

PLAN (276 characters) is the whole entry: how an AI agent turns $100
into the most money it can in 30 days. This program does nothing but
write it, byte for byte, into the directory named by
MAKEFUN_OUTPUT_DIR (default "/output"), creating that directory first.
"""

import os

PLAN = (
    "Day 1: scrape registries for firms opened this month, code-verify "
    "emails, send 30 agencies a free 20-lead sample. Sell niche lists "
    "at $99, refreshed weekly; $100 covers domain, email tool, API "
    "credits. Edge: new firms need customers now; fresh verified leads "
    "beat stale lists."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(PLAN)


if __name__ == "__main__":
    main()
