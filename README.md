# Winter Road

A digital haiga space by mozare.

**Live work:** https://mozareeduge.github.io/winter-road/

---

*Winter Road* is a born-digital artwork consisting of nine English haiku dispersed across a dark, near-black field. The poems are invisible until the reader moves near them; a poem may be kept visible through a click or tap. Each page load places the poems in one of four authored spatial profiles derived from a semantic grid. The interaction makes movement a condition of reading, not navigation.

This repository is a public source archive. The source is visible for linking, study, citation, and archival inspection. It is not open-source software; no license to reproduce, adapt, or reuse is granted. See `RIGHTS.md`.

---

## Files

```
index.html          canonical self-contained artwork
tests/
  verify_release.py release invariant check (Python stdlib only)
.github/
  workflows/
    pages.yml       CI and GitHub Pages deployment
CITATION.cff        formal citation record
CHANGELOG.md        release history
RIGHTS.md           rights notice
CLAUDE.md           maintenance rules for future sessions
```

## Opening locally

Open `index.html` directly in a browser (`file://` works) or serve from any HTTP root:

```
python3 -m http.server 8000
# then visit http://localhost:8000/
```

The work also runs correctly from a subpath such as `/winter-road/`.

## Citation

See `CITATION.cff` or cite as:

> Zare, Mohammad. *Winter Road: A Haiga Space*. 2026. https://mozareeduge.github.io/winter-road/

## Rights

Copyright © 2026 Mohammad Zare. See `RIGHTS.md`.
