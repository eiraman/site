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
EIRAMAN_OUT=/tmp/eiraman-site python3 -B generator/build.py
```

| Variable | Meaning | Default |
|---|---|---|
| `EIRAMAN_OUT` | output folder (emptied before the build) | `build/<site version>`, for example `build/0.4.0` |
| `EIRAMAN_PROFILES` | checkout of the `role-profiles` repository | `../role-profiles` |
| `EIRAMAN_BRAND` | folder holding `eiraman-su-chiaro.png` and `eiraman-su-scuro.png` | `brand/` |
| `EIRAMAN_PHOTO` | author photo for the Author & community page | unset |
| `EIRAMAN_SPEC03` | folder with the historical specification `Eiraman.md` and `Eiraman.en.md` | `generator/spec03/` (absent) |
| `EIRAMAN_OLD` | 0.2 release folder (functional map, sources page) | `releases/0.2.0-candidata` (absent) |

The build writes `manifest.json` with the SHA-256 of every output file. Two builds from the same commit
must produce the same manifest; CI checks this (`.github/workflows/site-build.yml`).

`manifest.json` also records the site version (`version`) and, under `kit`, the kit version and the
versions of what the kit bundles. The rules are in
[community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md), the history in
[CHANGELOG.md](CHANGELOG.md).

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
| Historical specification 0.3 (`spec03/`) and `make_spec_it.py`, `make_spec_en.py` | The historical specification 0.3 lives in the `guide` repository (`history/`, CC BY-SA 4.0); importing it into the site is not wired yet | Specification page and normative excerpts on component pages show a notice; Markdown downloads are skipped |
| 0.2 release pages (`releases/0.2.0-candidata`) | Not in the repository | Functional map page shows a notice; `framework/Fonti.md` is skipped |

## Known open items

- The historical specification 0.3 (in `guide/history/`) is not yet imported into this build: the kit ships
  without `framework/Eiraman.md` and the specification page shows a notice.
- Some page text is inline in `generator/build.py`. It is covered by Apache-2.0 with the code until it
  moves to `content.py`.
- Code comments and identifiers are in Italian.

## Licence

Code: [Apache License 2.0](LICENSE.md), see also [NOTICE](NOTICE). Website text in `generator/content.py`:
CC BY-SA 4.0, declared in `REUSE.toml`. Brand files: trademark, not licensed (`brand/PROVENANCE.md`).
Contributions need a DCO sign-off on every commit.
