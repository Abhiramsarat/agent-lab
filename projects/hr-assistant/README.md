# HR Assistant 💼

Answers your team's HR questions using **only your company's own policies** —
and points people to a human whenever it isn't sure or the question is sensitive.

## What's in this folder

| File / Folder       | What it is                                                          |
|---------------------|--------------------------------------------------------------------|
| `main.py`           | The assistant itself. The comments explain every step.              |
| `policies/`         | Your policy documents live here. The AI only answers from these.    |
| `README.md`         | This file.                                                          |

## Putting in YOUR real policies

Right now `policies/` holds a **sample** handbook so you can see the tool work.
To use your real ones, just replace the sample — drop your handbook in as a text
file (or several files, one per topic). Tell your assistant *"update the HR
policies"* and it'll help you get your real documents in.

## The safety design (why this is OK to use for HR)

- It answers **only** from the documents in `policies/` — it can't make up policy.
- If your handbook doesn't cover something, it says so and refers to a human.
- For sensitive matters (complaints, pay, performance, health), it always defers
  to a person. The AI informs; **people decide.**

## How to run it

Tell your assistant *"run the HR assistant"*, or by hand:

```
python3 main.py
```
