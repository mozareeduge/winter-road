---
name: weave-execute
description: Execute one Project Weave task in an isolated worker context
argument-hint: TASK_ID
context: fork
agent: weave-worker
disable-model-invocation: true
---

Execute `$ARGUMENTS` from its generated pack. Verify branch, base commit, scope, and authority. Begin the task if not active (update harness/RUN.json), implement the full contract, store evidence, run every required check, and return a compact delta. Do not declare completion; the coordinator must record review and pass the deterministic completion gate.
