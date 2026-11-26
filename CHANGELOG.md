<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: Apache-2.0
-->

# Changelog

All notable changes to the eiraman.tech website, its generator and the kit it serves
(`kit/eiraman-kit.zip`) are documented in this file. The format is based on
[Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow the rules in
[community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md): MINOR for content,
PATCH for fixes. The site version is the `version` field of `manifest.json`; the kit version is
`kit.version` in the same manifest.

The history up to 0.4.0 is reconstructed from the project's activity log, kept by the AI Coordinator
outside this repository. Up to 0.3.0 the site was built from a private repository; this repository was
first published on 25 November 2026. Where the log is not precise, the entry says so.

## [Unreleased]

## [0.4.1] - 2026-11-26

### Fixed

- `manifest.json` gives the site version as a SemVer label of its own (`0.4.1`) instead of `0.3.0`, the
  label under which the 25 November 2026 deployment (0.4.0) was published (see 0.4.0, "Known deviation").

### Added

- `manifest.json` has a `kit` object: path, kit version (`0.4.0`, unchanged because the kit bytes did not
  change) and `bundled`, the versions of what the
  kit contains: `registry` (read from the `CHANGELOG.md` of the `role-profiles` checkout),
  `ai_coordinator_profile` (read from `controllore/CONTROLLORE.md`), `specification` (`0.3` when the
  withheld historical specification is supplied), and `guide` and `tools` as `null`, because the kit
  does not contain the Guide or the tools.
- This changelog, and the CI workflow `changelog.yml`.

### Changed

- The default output folder of the generator is `build/<site version>` instead of `build/0.3.0-candidata`.

No page and no kit byte changes: two builds from this commit differ from a build of `c696503` only in
`manifest.json`.

## [0.4.0] - 2026-11-25

Published as commit `c696503` of this repository; the tag `v0.4.0` will be applied retroactively to that
commit. Deployed on eiraman.tech during the restricted launch of 25 November 2026, built from commit `c696503` of
this repository with the withheld inputs (author photo, historical specification 0.3, 0.2 map pages)
supplied locally. Two builds were identical; 48 changed files and the manifest were uploaded by SFTP;
63 of 63 fingerprints matched over HTTPS; `.htaccess` answers 403. Online manifest SHA-256 `affbcab3…c6eb6a`.
Kit version 0.4.0, the first kit under the open licences.

### Known deviation

- The deployed `manifest.json` says `"version": "0.3.0"`, although the content changed. The correct
  version of that content is 0.4.0. The label is fixed in [0.4.1].

### Changed

- The site is generated from the public `site` repository instead of the private one.
- The "Chi sono" / "About" page became "Autore e comunità" / "Author & community", with the biography and
  the LinkedIn link confirmed by the Human Manager, and links to the community repositories.
- Licence notices: Guide texts CC BY-SA 4.0, Role Profiles CC BY 4.0, code Apache-2.0; the Eiraman name
  and logo are trademarks outside these licences (`brand/PROVENANCE.md`, TRADEMARK.md). Copies
  distributed up to 0.3.x keep CC BY-NC-ND 4.0 (texts) and MIT (scripts).
- Kit: `LICENSE.md` and `LEGGIMI.md` state the new licences; the AI Coordinator profile ships as a draft,
  not qualified.

The log does not list every changed page of this deployment; the list above gives the changes it names.

## [0.3.0] - 2026-11-25

Rebuilt site in four levels, first uploaded on 25 November 2026: 47 files matched their fingerprints over
HTTPS. The orphan 0.2 files `diagramma.html`, `en/diagram.html` and `brand/eiraman.png` were removed; a
copy of the 0.2 site was kept before the upload.

### Added

- 32 pages in Italian and English on four levels, following the Golden Circle (why, how, what), a sober
  palette, the recoloured logo and a "What's new" page; the generator (`generator/`).
- Pages on AI Squads and Scrum, composable architecture and discovery with Design Thinking, and the
  specification 0.3.

### Known deviation: republished under the same label

On 25 November 2026 the site was republished many times with new content and the label stayed 0.3.0.
Under the current rules each of these would have been a MINOR or PATCH version. The log records, in order:

- the opening sentence of the home page restored (47 files);
- a new home page with "The pearl of love" and the page "Frameworks rethought", then the first 0.3 home
  page restored (49 files);
- the tone review of the whole site, with a text home page, the Levels page and costs (49 files);
- the home page drawing "Vision → Mandate → AI Squad → Evidence → Service in production", "AI Squad"
  instead of "squad of agents", and the roles renamed to "Human Manager" and "AI Coordinator" (49 files);
- the page "Come usarlo" / "How to use it" and the updated specification (51 files);
- the animated guide on "How to use it", the "Role Profiles" page, Digital Seniority in the specification
  and the downloadable kit `kit/eiraman-kit.zip`, holding 103 files with texts under CC BY-NC-ND 4.0 and
  scripts under MIT (54 site files);
- "How to use it" in five steps, with "Describe your request" (54 files);
- "Projects" instead of "Data", and the Role Profile families as expandable tiles (56 files);
- low-cost fixes after the critical review: text fixes, the kit SHA-256 in the start prompt, a generated
  `.htaccess` (HTTPS, canonical domain, security headers, no directory listing), `robots.txt` and
  `sitemap.xml` (58 files, manifest `ef1c965e…d9faef`);
- a favicon, then the link preview image;
- the statement on the Deny mechanism and the start from the kit (63 files, manifest `cdca01a6…e8f0f5`);
- the reason for "Bad news first" (63 files, manifest `5f21b3be…33ffc9`);
- the IBM Plex typeface replaced by Barlow and Barlow Condensed, and "complacent" replaced by "flattering"
  in the English translation of the specification (63 files, manifest `3af02f32…0664c7`).

The log does not give every intermediate manifest, so these states cannot all be rebuilt from it.

## [0.2.0] - 2026-11-24

First site online on eiraman.tech: bilingual (Italian at the root, English in `/en/`), 10 pages, desktop
and mobile, light and dark theme. 15 files uploaded by SFTP with a dedicated key and checked against the
manifest over HTTPS. Owner shown: Paolo Ungari, all rights reserved. An independent review asked for
corrections R1–R6: R2–R6 were applied before publication, and R1 (the owner named in the footer) was
closed by the owner's choice: Paolo Ungari, all rights reserved.

## [0.1.0] - 2026-11-24

Static distribution generated from commit `a984dca` of the then-public project repository: eight files,
identical across two builds, with a manifest of fingerprints. The log records the package as prepared and
verified; the external HTTPS check then found the hosting provider's "under construction" page, and it does
not record that 0.1.0 itself went online.

[Unreleased]: https://github.com/eiraman/site/compare/v0.4.1...main
[0.4.1]: https://github.com/eiraman/site/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/eiraman/site/releases/tag/v0.4.0
