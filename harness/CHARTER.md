# Project Charter

## Identity

- **Name:** winter-road — a haiga space
- **Repository:** mozareeduge/winter-road
- **Kind:** digital art / computational literature (haiga)
- **Author:** mozare
- **Established:** 2026-07-14
- **Current version:** v10.2 (as declared in winter_road.html title)

## Governance

This project uses Project Weave for structured task execution and evidence-gated completion.

- All aesthetic, conceptual, and publication decisions belong to mozare (human project owner).
- Claude Code executes bounded, evidence-verified tasks.
- Harness authority precedence: see `harness/AUTHORITY.md`.
- Operating policy (autonomy levels, public/private boundary): see `harness/POLICY.md`.

## Scope boundaries

**In scope for Claude Code execution:**
- Technical verification of the HTML/CSS/JS against authored intent.
- Accessibility audit and conformance fixes where fixes are unambiguous corrections (not design changes).
- Identifying bugs or regressions against authored behavior.
- Documentation and harness maintenance.

**Human checkpoint required before proceeding:**
- Any change to poem texts, line breaks, or poem IDs.
- Any change to SEMANTIC_GRID, DESKTOP_CELLS, or MOBILE_CELLS.
- Any change to timing constants (CONFIG object in JS).
- Any change to the artist statement.
- Any change to the color scheme or visual design tokens.
- Any merge to `main`.
- Any publication or upload to an external hosting service.

## Release surface

- `main` branch → `winter_road.html` is the primary public deliverable.
- Feature branches: harness, evidence, and development work.
- Private material (credentials, raw logs): must not appear on any branch.

## Work graph authority

`harness/TASKS.json` is the machine-readable work graph. Tasks are complete only when all required checks pass and (where required) independent review confirms. No task is complete based on prose summary alone.
