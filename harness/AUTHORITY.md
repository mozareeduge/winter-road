# Authority Map

## Binding sources (in precedence order)

1. Current explicit human decisions by mozare.
2. `harness/PROJECT.md` — purpose, outcome, invariants, and constraints.
3. `winter_road.html` — the authored source of record for all content, poems, topology, timing, and interaction design. Any proposed change must be justified against its authored logic.
4. `harness/DECISIONS.jsonl` — append-only log of accepted decisions and their rationale.
5. Executable evidence and accepted baselines recorded in `harness/BASELINE.md`.
6. `harness/TASKS.json` — work graph and acceptance contracts.
7. Summaries and chat history.

## Interpretation rules

- A lower source cannot silently overrule a higher source.
- Repetition in an implementation note does not create authority.
- A summary is reported information until evidence verifies it.
- When sources conflict, record the conflict in `harness/DECISIONS.jsonl` and continue only with work that is safe under every plausible interpretation.
- Supersede decisions explicitly; do not erase provenance.
- Aesthetic, artistic, experiential, and publication decisions are human-sensitive. Stop at a checkpoint rather than resolve them as mechanical choices.
