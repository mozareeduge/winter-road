# Project Weave — Claude Code Instructions

## Runtime

Use `claude-sonnet-4-6` at `medium` effort. Do not escalate model or effort automatically.

## Authority

Use this precedence:

1. explicit current human decision;
2. `harness/AUTHORITY.md` and the sources it names;
3. active entries in `harness/DECISIONS.jsonl`;
4. executable evidence and Git state;
5. `harness/TASKS.json`;
6. summaries and chat history.

Do not flatten product, artistic, research, ethical, experiential, or publication decisions into easier implementation choices.

## Start or resume

1. Verify repository, remote, branch, commit, and working tree.
2. Read `harness/STATE.md`.
3. Read `harness/TASKS.json` (active or next ready task).
4. Generate the selected task pack from `harness/PACKS/`.
5. Read the pack and only the files it names before broad exploration.

Note: `scripts/weave.py` is absent from this installation. Harness state is maintained manually.

## Task loop

For one ready task at a time:

1. verify scope and authority;
2. record task begin in `harness/RUN.json` and `harness/DECISIONS.jsonl`;
3. isolate noisy exploration or review in a subagent;
4. implement the smallest complete contract;
5. store full evidence under `artifacts/<task-id>/`;
6. run or attest every required check;
7. obtain fresh review when required;
8. fix verified findings;
9. mark task `completed` in `harness/TASKS.json`;
10. continue to the next ready task.

Stop only at a recorded human checkpoint or a verified hard blocker.

## Context discipline

- Keep this file under 200 lines.
- Keep the coordinator on state, active pack, and decisions.
- Do not paste full logs into the main context.
- At phase boundaries or high context use, persist evidence, state, and a handoff before compacting or starting fresh.
- Never reconstruct durable truth from chat when Git or evidence can answer.

## Completion and safety

- A prose claim is not evidence.
- Do not bypass failed or missing checks.
- Do not remove tests or weaken acceptance criteria to obtain green status.
- Do not edit outside task scope. Change a task contract only while it is not active, record why, then begin/restart it.
- Do not expose secrets or private operational artifacts.
- Do not force-push, rewrite published history, deploy, publish, or make irreversible external changes without explicit task authority.
- Do not report future work as complete.
