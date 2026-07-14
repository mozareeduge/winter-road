# Winter Road — maintenance rules

## What this is

Static, self-contained born-digital artwork. No framework, build step, bundler,
package manager, server, or runtime dependency. `index.html` is the canonical
artifact and must remain a single file that works from `file://` and any HTTP root.

## Canonical source

`index.html` is the canonical artwork. `winter_road.html` is obsolete and must
not be re-added.

## Invariants — do not change without explicit authority

**Poem text:** Nine haiku, exact wording, spelling, and capitalization. Defined
in the `POEMS` array in `index.html`. Do not alter, reorder, punctuate, or add poems.

**Statement text:** Three paragraphs beginning "I began with two words: *winter road*."
Exact wording. Defined in `.statement-copy` in `index.html`.

**Timing and thresholds:** `READABLE_THRESHOLD: 0.48`, `RELATION_THRESHOLD: 0.62`,
`PIN_SOLO_HOLD_MS: 12000`, `PIN_FADE_MS: 6000`, `TOUCH_DRAG_PREVIEW_MS: 8000`,
`TOUCH_PREVIEW_FADE_MS: 900`, `DESKTOP_EXIT_MS: 320`. Do not adjust timing or
spatial topology, colors, guide logic, or statement behavior without explicit request.

**No redesign:** Do not add visual polish, splash screens, navigation, cards, headers,
footers, modals, frameworks, analytics, service workers, external fonts, or audio.

## Rights

Source-visible archive. Not open-source. Do not add a `LICENSE` file or change
`RIGHTS.md` without explicit authority.

## Verification

Run before any release commit:

```
python3 tests/verify_release.py
```

## Pages and portability

The site deploys to `https://mozareeduge.github.io/winter-road/`. All paths in
`index.html` must be relative. No root-relative paths beginning with `/`. No
hardcoded host. `#statement` must work under a subpath. No `CNAME` in this
repository without explicit authority.

## No custom domain yet

Do not add `CNAME` or redirect to `theblackbirdfield.com` until explicitly authorized.
