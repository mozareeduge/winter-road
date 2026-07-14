---
name: weave-review
description: Independently review one Project Weave task against its contract and evidence
argument-hint: TASK_ID
context: fork
agent: weave-reviewer
disable-model-invocation: true
---

Review `$ARGUMENTS`. Read its task contract from harness/TASKS.json, the complete diff since base commit, surrounding source, check records, and artifacts. Try to refute completion. Return exact findings and a verdict (pass, changes-required, or blocked). Do not modify source files.
