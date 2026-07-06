# Positioning Teardown Agent 🔍

Your first **agent** — it decides its own steps instead of following a fixed script.

Give it a brand or competitor's website. It reads the site (fetching extra pages
if *it* decides to), then returns:
1. **Positioning teardown** — their messaging, audience, strengths, gaps.
2. **Pitch angle** — one sharp way your agency could win them.

## Why this one is different
Your earlier tools made **one** AI call. This runs a **loop**: the AI is given a
goal and a tool (`fetch_url`), and on each turn it chooses — fetch another page,
or stop and conclude. You watch it choose in real time as it runs.

## How to run it
Tell your assistant *"run the teardown agent on [url]"*, or by hand:

```
python3 main.py https://example.com
```
