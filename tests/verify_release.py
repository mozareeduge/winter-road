#!/usr/bin/env python3
"""Release invariant gate for Winter Road.

Checks the repository against the documented release contract.
Uses only Python standard library. Run from repo root:

    python3 tests/verify_release.py

Exits 0 on pass, 1 on any failure.
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ERRORS = []


def err(msg):
    ERRORS.append(msg)
    print(f"  FAIL  {msg}")


def ok(msg):
    print(f"  ok    {msg}")


def read(path):
    full = os.path.join(ROOT, path)
    if not os.path.isfile(full):
        return None
    with open(full, encoding="utf-8") as f:
        return f.read()


# ── Required files ────────────────────────────────────────────────────────────

print("\n[1] Required files")
required = [
    "index.html",
    ".nojekyll",
    "CLAUDE.md",
    "CITATION.cff",
    "CHANGELOG.md",
    "README.md",
    "RIGHTS.md",
    "tests/verify_release.py",
    ".github/workflows/pages.yml",
]
for path in required:
    if os.path.isfile(os.path.join(ROOT, path)):
        ok(path)
    else:
        err(f"missing required file: {path}")


# ── Obsolete files ────────────────────────────────────────────────────────────

print("\n[2] Obsolete files absent")
for name in ["winter_road.html", "CNAME"]:
    if os.path.exists(os.path.join(ROOT, name)):
        err(f"obsolete/forbidden file present: {name}")
    else:
        ok(f"absent: {name}")


# ── index.html — title ────────────────────────────────────────────────────────

print("\n[3] index.html title")
src = read("index.html")
if src is None:
    err("index.html missing — skipping content checks")
else:
    if "v10.2" in src[:500]:
        err("internal version string 'v10.2' found in title area")
    else:
        ok("no 'v10.2' in title area")
    if "<title>winter road — a haiga space by mozare</title>" in src:
        ok("title correct")
    else:
        err("title does not match 'winter road — a haiga space by mozare'")


# ── Poem inventory ────────────────────────────────────────────────────────────

print("\n[4] Poem inventory (nine poems, correct IDs, correct text)")
EXPECTED_POEMS = [
    ("winter-road-absence-wind",    ["winter road", "nobody comes here", "only the wind drives"]),
    ("winter-road-darkness-wind",   ["winter road", "absolute darkness", "only the wind drives"]),
    ("winter-road-only-wind",       ["winter road", "only the wind"]),
    ("winter-darkness-road-driven", ["winter darkness", "wind drives the road"]),
    ("dark-road-only-wind",         ["the dark road", "only the wind"]),
    ("winter-silence-only-wind",    ["absolute winter silence", "only the wind"]),
    ("winter-road-white-absence",   ["winter road", "everything supposed to be white", "nobody comes here"]),
    ("winter-darkness-white",       ["winter darkness", "everywhere supposed to be white"]),
    ("winter-road-absence-white",   ["winter road", "nobody comes here", "everything supposed to be white"]),
]

if src is not None:
    ids_found = re.findall(r"id:\s*'([^']+)'", src)
    ids_set = set(ids_found)
    expected_ids = {p[0] for p in EXPECTED_POEMS}
    if len(ids_found) != len(set(ids_found)):
        err("duplicate poem IDs found")
    else:
        ok("no duplicate poem IDs")
    if ids_set == expected_ids:
        ok("all nine poem IDs present")
    else:
        missing = expected_ids - ids_set
        extra = ids_set - expected_ids
        if missing:
            err(f"missing poem IDs: {missing}")
        if extra:
            err(f"unexpected poem IDs: {extra}")
    for pid, lines in EXPECTED_POEMS:
        for line in lines:
            if line not in src:
                err(f"poem line missing: '{line}' (id: {pid})")
    else:
        ok("all poem lines present")


# ── Semantic grid ─────────────────────────────────────────────────────────────

print("\n[5] Semantic grid IDs")
SEMANTIC_GRID_IDS = [
    "winter-silence-only-wind", "winter-road-only-wind", "winter-road-darkness-wind",
    "winter-road-absence-wind", "winter-darkness-road-driven", "dark-road-only-wind",
    "winter-road-white-absence", "winter-road-absence-white", "winter-darkness-white",
]
if src is not None:
    grid_match = re.search(r"const SEMANTIC_GRID\s*=.*?\]\);", src, re.DOTALL)
    if grid_match:
        grid_src = grid_match.group()
        missing_grid = [gid for gid in SEMANTIC_GRID_IDS if gid not in grid_src]
        if missing_grid:
            err(f"semantic grid missing IDs: {missing_grid}")
        else:
            ok("all nine semantic grid IDs present")
    else:
        err("SEMANTIC_GRID definition not found")


# ── Statement wording ─────────────────────────────────────────────────────────

print("\n[6] Statement wording")
STATEMENT_FRAGMENTS = [
    "I began with two words:",
    "winter road",
    "Through permutation, they opened toward other objects, images, and tensions.",
    "Nine haiku are dispersed across a dark interface, invisible until approached.",
    "The reader’s movement becomes a condition of visibility.",
    "Haiku opens a small interval in language, where an image exceeds the words that hold it.",
    "Haiga gives that interval a surface",
    "I call",
    "Winter Road",
    "a digital haiga space.",
]
if src is not None:
    for frag in STATEMENT_FRAGMENTS:
        if frag in src:
            ok(f"statement fragment present: '{frag[:50]}'")
        else:
            err(f"statement fragment missing: '{frag}'")


# ── Guide strings ─────────────────────────────────────────────────────────────

print("\n[7] Guide strings")
if src is not None:
    for s in ["move slowly · click to keep", "touch and move · tap to keep"]:
        if s in src:
            ok(f"guide string: '{s}'")
        else:
            err(f"guide string missing: '{s}'")


# ── Signature trigger and return control ──────────────────────────────────────

print("\n[8] Signature trigger and return control")
if src is not None:
    if "by mozare" in src and "statement" in src:
        ok("signature trigger content present")
    else:
        err("signature trigger 'by mozare · statement' not found")
    if ">return<" in src:
        ok("return control present")
    else:
        err("return control 'return' not found in statement")
    if "#statement" in src:
        ok("hash #statement referenced in source")
    else:
        err("#statement hash reference missing")


# ── Timing and thresholds ─────────────────────────────────────────────────────

print("\n[9] CONFIG timing and thresholds")
CONFIG_CHECKS = [
    ("READABLE_THRESHOLD: 0.48", "readability threshold 0.48"),
    ("RELATION_THRESHOLD: 0.62", "relational threshold 0.62"),
    ("PIN_SOLO_HOLD_MS: 12000", "solo keep hold 12000ms"),
    ("PIN_RELATION_HOLD_MS: 12000", "relational renewal hold 12000ms"),
    ("PIN_FADE_MS: 6000", "kept fade 6000ms"),
    ("TOUCH_DRAG_PREVIEW_MS: 8000", "touch preview hold 8000ms"),
    ("TOUCH_PREVIEW_FADE_MS: 900", "preview fade 900ms"),
    ("DESKTOP_EXIT_MS: 320", "desktop exit delay 320ms"),
]
if src is not None:
    for pattern, label in CONFIG_CHECKS:
        if pattern in src:
            ok(label)
        else:
            err(f"CONFIG value missing or changed: {label} (expected '{pattern}')")


# ── External dependencies ─────────────────────────────────────────────────────

print("\n[10] No external network dependencies")
if src is not None:
    external_patterns = [
        r'<script[^>]+src=["\']https?://',
        r'<link[^>]+href=["\']https?://',
        r'@import\s+["\']https?://',
        r'url\(["\']https?://',
        r'fonts\.googleapis\.com',
        r'fonts\.gstatic\.com',
        r'cdn\.',
        r'unpkg\.com',
        r'jsdelivr\.net',
        r'gtag\(',
        r'ga\(',
        r'analytics',
        r'plausible',
    ]
    found_external = False
    for pat in external_patterns:
        if re.search(pat, src, re.IGNORECASE):
            err(f"possible external dependency found: {pat}")
            found_external = True
    if not found_external:
        ok("no external scripts, stylesheets, fonts, or analytics detected")


# ── Root-relative runtime paths ───────────────────────────────────────────────

print("\n[11] No root-relative runtime asset paths")
if src is not None:
    root_rel = re.findall(r'(?:src|href|url)\s*[=:(]\s*["\']?(/[^/\s"\'<>])', src)
    filtered = [p for p in root_rel if not p.startswith("/#")]
    if filtered:
        err(f"root-relative paths found (breaks subpath): {filtered[:5]}")
    else:
        ok("no root-relative asset paths")


# ── Citation file ─────────────────────────────────────────────────────────────

print("\n[12] CITATION.cff basics")
cff = read("CITATION.cff")
if cff is None:
    err("CITATION.cff missing")
else:
    for check, label in [
        ("cff-version: 1.2.0", "CFF version 1.2.0"),
        ("Winter Road: A Haiga Space", "title"),
        ("family-names: Zare", "author family name"),
        ("given-names: Mohammad", "author given name"),
        ("1.0.0", "version 1.0.0"),
        ("mozareeduge.github.io/winter-road", "live URL"),
        ("mozareeduge/winter-road", "repository URL"),
    ]:
        if check in cff:
            ok(f"citation: {label}")
        else:
            err(f"citation: {label} missing (expected '{check}')")


# ── Rights file ───────────────────────────────────────────────────────────────

print("\n[13] RIGHTS.md basics")
rights = read("RIGHTS.md")
if rights is None:
    err("RIGHTS.md missing")
else:
    for check, label in [
        ("Mohammad Zare", "author name"),
        ("All rights reserved", "all rights reserved"),
        ("open-source", "open-source disclaimer"),
    ]:
        if check in rights:
            ok(f"rights: {label}")
        else:
            err(f"rights: {label} missing")


# ── Accidental committed Relay/private files ──────────────────────────────────

print("\n[14] No private/Relay files committed (git-tracked check)")
import subprocess
try:
    tracked_result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT, capture_output=True, text=True, check=True
    )
    tracked_files = set(tracked_result.stdout.splitlines())
    forbidden_tracked = [
        ".claude/relay/run",
        "WORK_STATE.md",
        "MISSION.md",
        "TEST_MATRIX.md",
        "relay-execute",
        "relay-release",
        "WORKLOAD.md",
        "PASTE_ONCE",
        ".claude/skills",
    ]
    for pat in forbidden_tracked:
        matching = [f for f in tracked_files if pat in f]
        if matching:
            err(f"private/Relay path tracked by git: {pat} ({matching[:3]})")
        else:
            ok(f"not tracked: {pat}")
    # Also check for committed CNAME
    if "CNAME" in tracked_files:
        err("CNAME committed (not authorized)")
    else:
        ok("CNAME not committed")
except subprocess.CalledProcessError:
    err("could not run git ls-files — run from repo root")


# ── Summary ───────────────────────────────────────────────────────────────────

print()
if ERRORS:
    print(f"RESULT: FAIL — {len(ERRORS)} error(s)")
    for e in ERRORS:
        print(f"  - {e}")
    sys.exit(1)
else:
    print("RESULT: PASS — all release invariants satisfied")
    sys.exit(0)
