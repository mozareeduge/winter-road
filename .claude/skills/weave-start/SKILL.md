---
name: weave-start
description: Refresh state, choose the next ready task, and generate its bounded pack
disable-model-invocation: true
---

Note: scripts/weave.py is absent from this installation. Do the following manually:

1. Read `harness/STATE.md`.
2. Read `harness/TASKS.json` — identify the first task with status "ready" whose depends_on are all "completed".
3. Read `harness/RUN.json` to verify no other task is active.
4. Generate a bounded context pack for that task:
   - Load the task's `authority` files.
   - Load the task's `context` files.
   - Write a pack summary to `harness/PACKS/<task-id>.md`.
5. Return the task, pack path, dependencies, checks, scope, and any missing verified fact. Do not begin broad exploration.
