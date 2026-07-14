# Verified Baseline

## Date
2026-07-14

## Repository state at bootstrap

- **Branch:** claude/new-session-6ah8td
- **HEAD:** 997489b0840e78f106608d34651b32be8f195a03
- **Working tree:** clean at bootstrap (before harness installation commits)
- **Remote:** origin → mozareeduge/winter-road

## Files present at bootstrap

| File | Status | Notes |
|------|--------|-------|
| `winter_road.html` | Present — primary artifact | v10.2; 1795 lines; self-contained HTML/CSS/JS |
| `README.md` | Present | "winter-road / A haiga space" |

## Primary artifact: winter_road.html

**Version:** v10.2 (declared in `<title>`)  
**Self-contained:** Yes — no external CDN links, no remote resources  
**Size:** ~1795 lines; estimated < 100 KB  

### Structural inventory (inspected)

**Poems (9 authored haiku):**

| ID | Lines |
|----|-------|
| winter-road-absence-wind | "winter road" / "nobody comes here" / "only the wind drives" |
| winter-road-darkness-wind | "winter road" / "absolute darkness" / "only the wind drives" |
| winter-road-only-wind | "winter road" / "only the wind" |
| winter-darkness-road-driven | "winter darkness" / "wind drives the road" |
| dark-road-only-wind | "the dark road" / "only the wind" |
| winter-silence-only-wind | "absolute winter silence" / "only the wind" |
| winter-road-white-absence | "winter road" / "everything supposed to be white" / "nobody comes here" |
| winter-darkness-white | "winter darkness" / "everywhere supposed to be white" |
| winter-road-absence-white | "winter road" / "nobody comes here" / "everything supposed to be white" |

**Spatial topology (SEMANTIC_GRID — 3×3, authored):**
- Row 0: winter-silence-only-wind, winter-road-only-wind, winter-road-darkness-wind
- Row 1: winter-road-absence-wind, winter-darkness-road-driven, dark-road-only-wind
- Row 2: winter-road-white-absence, winter-road-absence-white, winter-darkness-white

**Interaction constants (CONFIG):**
- PIN_SOLO_HOLD_MS: 12000
- PIN_RELATION_HOLD_MS: 12000
- PIN_FADE_MS: 6000
- READABLE_THRESHOLD: 0.48
- RELATION_THRESHOLD: 0.62
- TOUCH_DRAG_PREVIEW_MS: 8000
- TOUCH_PREVIEW_FADE_MS: 900
- DESKTOP_EXIT_MS: 320
- ENTRY_IDLE_DELAY_MS: 500
- TOUCH_TAP_MOVE_PX: 16
- TOUCH_TAP_MAX_MS: 700
- TOUCH_CLICK_GUARD_MS: 750

**Diagnostics API:** `window.__winterRoadDiagnostics` exposed for state inspection.

**Accessibility features observed:**
- `aria-label` on field (`main`), sites (`section`), each haiku button, statement trigger, dialog, heading, return button
- `aria-haspopup="dialog"` and `aria-controls` on statement trigger
- `aria-live="polite"` region for haiku announcements
- `aria-describedby="hint"` on haiku buttons
- `role` inferred from semantic elements (`<main>`, `<header>`, `<section>`, `<dialog>`, `<button>`, `<h1>`, `<h2>`)
- `.sr-only` class for visually-hidden but screen-reader-accessible text
- Focus management on dialog open/close
- `prefers-reduced-motion` media query handled
- `focus-visible` styles on interactive elements

**Baseline gaps (not yet verified):**
- Actual keyboard navigation sequence not tested in browser
- Screen reader announcement quality not tested
- Mobile touch behavior not verified on real device
- No Lighthouse run yet

## Harness installation

Installed at bootstrap. Files added to repository on branch `claude/new-session-6ah8td`:
- `CLAUDE.md`
- `harness/PROJECT.md`, `AUTHORITY.md`, `POLICY.md`, `CONFIG.json`, `TASKS.json`, `DECISIONS.jsonl`, `RUN.json`, `STATE.md`, `CHARTER.md`, `BASELINE.md`, `PACKS/`, `SNAPSHOTS/`, `private/`
- `.claude/agents/` (weave-scout, weave-worker, weave-reviewer)
- `.claude/skills/` (weave-start, weave-execute, weave-review, weave-handoff)
- `artifacts/BOOTSTRAP-01/`
- `.gitignore`

## Known blocker

`scripts/weave.py` and companion scripts were absent from the Project Weave ZIP. Automated harness commands (`validate`, `status --write`, `next`, `pack`, `begin`, `complete`) are unavailable. Harness is operated manually. See D-002 in DECISIONS.jsonl.
