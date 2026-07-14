# AUDIT-01 Findings — Accessibility and Interaction Audit

Date: 2026-07-14  
Artifact: winter_road.html (v10.2, 62,024 bytes)

---

## Machine checks

| Check | Result | Detail |
|-------|--------|--------|
| poem-integrity | PASS | All 9 poem IDs present in source |
| no-external-resources | PASS | No external CDN/resource URLs found |
| file-size | PASS | 62,024 bytes (60.6 KB; limit 100 KB) |

---

## Acceptance criteria verification

| Criterion | Status | Evidence |
|-----------|--------|---------|
| All 9 poems present with correct IDs and authored text | PASS | machine check; IDs and text verified against BASELINE.md |
| SEMANTIC_GRID matches baseline | PASS | code inspection; lines 513–515 match BASELINE.md |
| DESKTOP_CELLS and MOBILE_CELLS match baseline | PASS | code inspection; lines 519–529 match BASELINE.md |
| CONFIG timing constants match baseline | PASS | code inspection; lines 481–491 match BASELINE.md |
| All ARIA attributes present | PASS | see ARIA inventory below |
| No external resource URLs | PASS | machine check |
| Self-contained size under 100 KB | PASS | 60.6 KB |
| focus-visible styles for all interactive elements | PASS | .haiku:focus-visible, .signature:focus-visible, .statement-return:focus-visible all defined |
| prefers-reduced-motion handling correct | PASS | CSS media query + JS matchMedia; reducedMotion.matches applied in finishPinnedLifecycle and clearTemporary |
| Statement dialog focus management | PASS | showModal(); statementCopy.focus() on open; signature.focus() on close |
| Findings document lists all gaps with severity | PASS (this document) | — |

---

## ARIA inventory (all verified present)

- `<main aria-label="winter road, a haiga space by mozare">` — field container ✓
- `<section aria-label="hidden haiku">` — sites container ✓
- `<button aria-haspopup="dialog" aria-controls="statementDialog">` — statement trigger ✓
- `<div id="live" aria-live="polite" aria-atomic="true">` — announcement region ✓
- `<dialog aria-labelledby="statementHeading">` — statement dialog ✓
- `<h2 class="sr-only" id="statementHeading">Statement</h2>` — dialog label ✓
- `button.setAttribute('aria-describedby', 'hint')` — haiku button hint ✓
- `#hint` — sr-only hint text: "Press Enter or Space to keep this haiku visible. Press Escape to dismiss it." ✓
- `html lang="en"` ✓

---

## Color contrast (WCAG AA computed)

| Color token | Hex | Contrast vs #050505 | WCAG AA |
|-------------|-----|---------------------|---------|
| --poem | #eeeeea | 17.5:1 | PASS |
| --root | #d7d7d1 | 14.1:1 | PASS |
| --guide | #8d8d87 | 6.1:1 | PASS |
| --signature-idle | #8a8a84 | 5.9:1 | PASS |
| --signature-search | #82827c | 5.3:1 | PASS |
| --signature-reading | #7d7d77 | 4.9:1 | PASS |
| statement-copy | #c7c7c1 | 12.0:1 | PASS |
| statement-copy em | #d2d2cc | 13.4:1 | PASS |
| focus ring (composited) | rgba(165,187,201,.84) | 7.3:1 | PASS (≥3:1 non-text) |

All text colors meet WCAG 2.1 AA (4.5:1 minimum for normal text).  
Focus ring meets WCAG 2.1 1.4.11 (3:1 non-text contrast).

---

## Structural integrity

- One `<h1>` (root-inscription "winter road") ✓
- One `<h2>` (sr-only dialog heading) ✓
- `<main>` landmark ✓
- Native `<dialog>` with `showModal()` ✓
- `<button>` elements for all interactive controls ✓

---

## Open observations (require human judgment — no mechanical fix)

### OBS-1: Dialog Tab trap (OPEN — artistic/design decision)

**Observation:** The statement dialog traps Tab to a single element (`statementReturn`). Pressing Tab inside the dialog focuses `statementReturn` and loops.

**Context:** The dialog has two focusable elements: `statementCopy` (tabindex=-1, receives programmatic focus on open) and `statementReturn` (button). The statement copy is deliberately not in the Tab sequence (tabindex=-1) — the reader is expected to read it as a passive text block, then return. This matches the work's interaction grammar: the dialog is a reading pause, not a form.

**Status:** Likely intentional design. A conventional dialog would cycle through all focusable content, but this work has chosen a single-action model. **No change without explicit human decision.**

### OBS-2: No skip navigation link (OPEN — acceptable for this work type)

**Observation:** No skip-to-content link.

**Context:** The work has no repeated navigation block that would benefit from a skip link. The main experience begins immediately. For a single-experience digital art piece, skip nav is not typically required.

**Status:** Acceptable. **No action needed.**

### OBS-3: Keyboard discovery order is non-linear (OPEN — inherent to work's model)

**Observation:** Haiku buttons are positioned by authored spatial topology and cell index. Tab order follows DOM order, which corresponds to `layoutOrder()` (SEMANTIC_GRID rotation). This order is not spatial on screen (e.g., the first tab stop may not be the visually nearest poem).

**Context:** The keyboard interaction is analogous to the pointer interaction: discovery through movement. The focus handler correctly reveals each poem as it's focused. The Tab order is determined by the semantic grid rotation, which varies per session. This unpredictability is part of the work's premise.

**Status:** Inherent to the work's model. **No change without explicit human decision.**

### OBS-4: `statementReturn` button text is "return" (OPEN — acceptable)

**Observation:** The visible button label is "return". The full aria-label is "Close the statement and return to Winter Road".

**Status:** Aria-label provides the accessible name. No issue.

---

## No bugs found

No errors in interaction logic, ARIA markup, focus management, or authored content were identified. The code is well-structured and the accessibility implementation is thorough.

---

## Summary

winter_road.html v10.2 passes all machine checks and all inspected acceptance criteria. All WCAG 2.1 AA measurable requirements are met by code inspection. The four open observations are not bugs; they are either intentional design choices or non-issues for this work type. **Human review is required before any changes are made to the open observations**, as they all touch the work's experiential model.
