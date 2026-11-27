<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: Apache-2.0
-->

# Eiraman site generator

Static generator of the Eiraman website (Italian at the root, English in `/en/`). Python 3, standard
library only. Status: **draft**, prepared for a restricted launch. Nothing here is published.

## Build

```sh
git clone https://github.com/eiraman/role-profiles ../role-profiles   # the build reads profilo.json files
# The registry must be at the commit pinned in profiles.ref, with a clean tree: use a detached worktree, so that
# the work in progress of ../role-profiles is left alone.
git -C ../role-profiles worktree add --detach ../.build/rp-pinned "$(grep -v '^#' profiles.ref | grep -E '^[0-9a-f]{40}$')"
# The same for the Guide (the text of the method that the site renders): the commit in guide.ref.
git clone https://github.com/eiraman/guide ../guide
git -C ../guide worktree add --detach ../.build/guide-pinned "$(grep -v '^#' guide.ref | grep -E '^[0-9a-f]{40}$')"
EIRAMAN_PROFILES=../.build/rp-pinned EIRAMAN_GUIDE=../.build/guide-pinned EIRAMAN_OUT=/tmp/eiraman-site python3 -B generator/build.py
```

The two inputs of the build that live in other repositories are declared once each, in [profiles.ref](profiles.ref)
(the Role Profiles registry) and [guide.ref](guide.ref) (The Eiraman Guide); the CI workflow reads them from
there. The build exits with an error, and a message that says how to get a matching checkout, if
`EIRAMAN_PROFILES` or `EIRAMAN_GUIDE` is not the root of a git checkout whose `HEAD` is that commit with no
uncommitted changes. To update one of them, change its `.ref` file (with the version in its comment) in a
reviewed commit.

The Guide is the reference of the method (decision D-IT-1, CR-029): the English text is canonical
(`EIRAMAN-GUIDE.md` at the root of the guide repository) and the curated Italian translation is
`translations/it/EIRAMAN-GUIDE.it.md` there. The site renders both (`en/guide.html`, `guida.html`), cites the
Guide sections from the component pages and ships the Guide in the kit. The translation is optional: when the
file is absent the Italian page is a placeholder, the build reports `guide-it`, and the Italian pages link the
English Guide. The Guide sections that the site links to (`GUIDE_REF` and `FW_GUIDE` in `generator/content.py`)
are checked in both texts at every build.

| Variable | Meaning | Default |
|---|---|---|
| `EIRAMAN_OUT` | output folder (emptied before the build) | `build/<site version>`, for example `build/0.4.1` |
| `EIRAMAN_PROFILES` | checkout of the `role-profiles` repository, at the commit in `profiles.ref`, clean | `../role-profiles` |
| `EIRAMAN_PROFILES_UNPINNED` | `1` allows a checkout at another commit or with changes; development only, the manifest says `publishable: false` | unset |
| `EIRAMAN_GUIDE` | checkout of the `guide` repository, at the commit in `guide.ref`, clean | `../guide` |
| `EIRAMAN_GUIDE_IT` | the Italian translation of the Guide; a path outside the guide checkout makes the build not publishable | `<guide>/translations/it/EIRAMAN-GUIDE.it.md` (optional) |
| `EIRAMAN_GUIDE_UNPINNED` | as `EIRAMAN_PROFILES_UNPINNED`, for the guide | unset |
| `EIRAMAN_BRAND` | folder holding `eiraman-su-chiaro.png` and `eiraman-su-scuro.png` | `brand/` |
| `EIRAMAN_PHOTO` | author photo for the Author & community page | unset |
| `EIRAMAN_SPEC03` | folder with the historical specification `Eiraman.md` and `Eiraman.en.md` | `generator/spec03/` (absent) |
| `EIRAMAN_OLD` | 0.2 release folder (functional map, sources page) | `releases/0.2.0-candidata` (absent) |

The build writes `manifest.json` with the SHA-256 of every output file. Two builds from the same commit
must produce the same manifest; CI checks this (`.github/workflows/site-build.yml`).

`manifest.json` also records the registry commit read by the build (`registry_commit`), the Guide commit and version
(`guide_commit`, `guide_version`), `publishable` (`false` when `EIRAMAN_PROFILES_UNPINNED` or `EIRAMAN_GUIDE_UNPINNED`
was used: such a build must never be published), the site version (`version`) and, under `kit`, the kit version and the
versions of what the kit bundles. The rules are in
[community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), the history in
[CHANGELOG.md](CHANGELOG.md). The changelog of the kit alone is [kit/CHANGELOG.md](kit/CHANGELOG.md)
(decision D-VER-2); it is a source of the repository and is not put in `kit/eiraman-kit.zip`. The kit does contain the changelogs of the artifacts it bundles from the registry (D-VER-2): the
`CHANGELOG.md` of each profile and of the registry (`role-profiles/`) and the one of the AI Coordinator profile
(`controllore/CHANGELOG.md`), because the profiles cite them. The build takes the Guide in English and Italian from
the pinned guide commit and the registry from the pinned role-profiles commit; the versions it records under
`kit.bundled` are read from those sources.

## Brand files

`brand/` holds the Eiraman logo (`eiraman-su-chiaro.png`, `eiraman-su-scuro.png`, `eiraman-anteprima.png`),
and `generator/favicon.py` draws the favicon from it. The logo is a **trademark**: it is not covered by the
CC or Apache licences of this repository (`REUSE.toml`: `LicenseRef-Eiraman-Trademark`). Provenance and
legal status: [brand/PROVENANCE.md](brand/PROVENANCE.md). A fork must remove or replace these files
unless the [trademark policy](https://github.com/eiraman/community/blob/main/TRADEMARK.md) allows the use;
without them the build renders a text wordmark and lists `brand` under `"placeholders"`.

## Withheld inputs and placeholders

Some inputs of the private build are not part of this repository. When one is missing, the build does not
fail: it renders a visible placeholder (an element with a `data-placeholder` attribute) and lists the
missing input in `manifest.json` under `"placeholders"`.

| Input | Why it is withheld | Placeholder |
|---|---|---|
| `recolor_logo.py` | Private helper that processed the logo; not needed by the build | Not needed by the build |
| Author photo | Personal data, excluded | Empty circle on the Author & community page |
| `chi-sono-bozza.md` | Draft of the former About page, not for publication | Not needed by the build |
| Historical specification 0.3 (`spec03/`) and `make_spec_it.py`, `make_spec_en.py` | Private working copies (both languages). The Italian text also lives in the `guide` repository (`history/`, CC BY-SA 4.0), but the site is built from the two private files, which also give the English text and the anchors of the page; reading `history/` instead is not wired | The historical specification page shows a notice; the Markdown downloads are skipped, and the component pages omit their secondary link to the historical text |
| 0.2 release pages (`releases/0.2.0-candidata`) | Not in the repository | Functional map page shows a notice; `framework/Fonti.md` is skipped |

## Known open items

- The historical specification 0.3 is still read from the private `EIRAMAN_SPEC03` folder: a public build shows a
  placeholder on `specifica.html` and `en/specification.html`. The kit no longer ships it (kit 0.10.0).
- The pinned Guide commit is `2635a69` (1.0.0-rc.5), which has no Italian translation: until `guide.ref` moves to
  the commit that contains it, `guida.html` is a placeholder.
- Some page text is inline in `generator/build.py`. It is covered by Apache-2.0 with the code until it
  moves to `content.py`.
- Code comments and identifiers are in Italian.

## Licence

Code: [Apache License 2.0](LICENSE.md), see also [NOTICE](NOTICE). Website text in `generator/content.py`:
CC BY-SA 4.0, declared in `REUSE.toml`. Brand files: trademark, not licensed (`brand/PROVENANCE.md`).
Contributions need a DCO sign-off on every commit.
