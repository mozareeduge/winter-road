# Project Contract

## Identity

- Name: winter-road
- Repository: mozareeduge/winter-road
- Project kind: digital art / computational literature (haiga)
- Primary audience: general public; poetry, haiku, and web-art readers
- Author: mozare

## Purpose

Maintain and develop *Winter Road*, a digital haiga space presenting nine haiku variations on the theme "winter road" through a proximity-based discovery interaction in the browser. The reader's movement across a dark interface reveals poems; reader agency is a structural and aesthetic condition of the work.

## Inspectable outcome

A visitor to the published URL can:
1. Open the page and see a dark field with the "winter road" title inscription and guide text.
2. Move their pointer (desktop) or finger (mobile) across the field to reveal haiku by proximity.
3. Click or tap to pin a revealed haiku; it remains visible for a timed hold then fades.
4. Reach nearby haiku while one is pinned (relation pair).
5. Navigate the interface entirely by keyboard (Tab focus reveals and pins poems; Escape dismisses).
6. Open the artist statement dialog via the "statement" button.
7. Return from the statement via the "return" button or Escape key.
8. Experience correct behavior under `prefers-reduced-motion`.
9. Use the page on mobile touch devices (touch-drag reveal, tap-to-pin).

## Success criteria

- All 9 haiku are discoverable and readable via pointer/touch movement.
- Pin, relation, and dismiss lifecycle timers operate as authored.
- Statement dialog opens, is scrollable, closes, and returns focus correctly.
- Keyboard navigation covers all interactive elements without trapping focus (except inside dialog).
- `prefers-reduced-motion` disables animated transitions without breaking function.
- No JavaScript errors in browser console under normal interaction.
- Lighthouse accessibility score ≥ 90 (or all failures are documented as intentional).
- Page loads under 100 KB (it is self-contained; no external resources).
- The 9 authored poems are present and unmodified.
- `window.__winterRoadDiagnostics` API returns correct structural state.

## Meaning-sensitive invariants

These must not be changed mechanically or without explicit human-authored decision:

- The nine haiku texts: exact wording, line breaks, and poem IDs are authored works.
- `SEMANTIC_GRID`: the 3×3 spatial topology assigning poems to grid positions is an authored spatial argument.
- `DESKTOP_CELLS` and `MOBILE_CELLS`: authored spatial distributions.
- The proximity-based invisibility model: poems are hidden until approached; this is the work's epistemic and experiential premise.
- The "haiga" framing and artist statement text.
- The version label in the `<title>` (currently v10.2).
- The dark color scheme and its specific values.
- No external CDN, analytics, or tracking scripts.
- Authorship attribution ("by mozare").

## Constraints

- Platform: modern browsers (desktop and mobile); no build step; single self-contained HTML file.
- No external dependencies at runtime (all CSS and JS inline).
- Repository is public; no secrets or private material may be committed.
- The `main` branch is the release surface; feature/development work uses a separate branch.
- All aesthetic and artistic decisions require explicit human authority; Claude must not substitute product heuristics for authorial intent.
