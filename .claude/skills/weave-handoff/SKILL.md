---
name: weave-handoff
description: Write a compact verified continuation handoff before compaction or session rotation
disable-model-invocation: true
---

Note: scripts/weave.py is absent. Do the following manually:

1. Read `harness/STATE.md` and `harness/RUN.json`.
2. Read `harness/TASKS.json` (active task and next ready tasks).
3. Read `harness/DECISIONS.jsonl` (last 5–10 entries).
4. Write `harness/SNAPSHOTS/HANDOFF-<date>.md` containing:
   - Active task and its check status.
   - Git branch, HEAD commit, working tree cleanliness.
   - Next ready tasks.
   - Open decisions or blockers.
   - Minimal continuation instructions.
5. Do not add narrative history. Do not expose session-private material.
