# Operating Policy

## Autonomy levels

**Mechanical:** act without asking when the task contract authorizes it and verification is available. Examples: correcting broken attribute syntax, fixing a deterministic naming error, updating a comment that is provably wrong.

**Interpretive:** proceed only when authority and acceptance criteria make the intended meaning unambiguous. Record the interpretation in `harness/DECISIONS.jsonl`.

**Human-sensitive:** stop at a checkpoint. Examples: changing poem text, altering spatial topology, adjusting timing constants, revising the artist statement, changing visual design tokens, adding new poems or removing existing ones, altering authorship attribution.

**Irreversible or external:** require explicit authority before acting. Examples: merging to `main`, publishing to a hosting service, uploading to any external platform, deleting authored content, force-pushing.

## Public/private boundary

Classify every output as one of:

- `public`: safe for release or merge to `main`;
- `project-internal`: safe on a feature branch or private context;
- `session-private`: credentials, raw session logs, local paths, hidden reasoning, temporary workmaps.

Do not commit `session-private` material to any branch. Do not assume a file is public merely because it is inside the repository; audit the intended release surface separately.

## Evidence hierarchy

1. executable end-to-end result (browser interaction, Lighthouse run);
2. deterministic command output;
3. inspectable artifact with recorded criteria;
4. independent review with exact references;
5. agent report.

Use the strongest feasible evidence. State what remains untested.

## Artistic and experiential authority

The work's interaction model, spatial topology, poem texts, visual design, and timing behavior are authored decisions. Conventional software heuristics (e.g., "users expect X") do not override authorial intent. When evaluating these dimensions, use the project's own aesthetic logic as the benchmark.
