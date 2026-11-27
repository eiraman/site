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

## [0.10.0] - 2026-11-27

Scope: Change Request CR-024 of the method project. Site bump: MINOR, a new page (VERSIONING §2.4). The kit
does not change and stays 0.9.0.

### Added

- New page «Le prime evidenze» (`evidenze.html`) and its English version «First evidence»
  (`en/evidence.html`): what Eiraman is, four figures from the project records on the checks made between 24
  and 27 November 2026 while building the method, and three examples. The text is the one set by the Human
  Manager.
- Footer link to the new page on every page with the footer, except the home pages (`index.html`,
  `en/index.html`), which do not change.

### Changed

- All other pages with the footer: the footer link above.
- `sitemap.xml`: the two new pages.
- `manifest.json`: `version` 0.10.0, `date` 2026-11-27, fingerprints.

## [0.9.0] - 2026-11-26

Scope: Change Requests CR-011 and CR-012 of the method project. The kit follows the Role Profiles registry
0.8.0 (commit `0bc7f8624e484b2aacd3731c25a13377bc57a84f`), which contains 0.7.0 and its corrections. A first
candidate of this version followed registry 0.7.0 and was never published. Site bump: MINOR, a bundled
artifact has a MINOR (VERSIONING §2.4). Kit 0.8.1 → 0.9.0: MINOR.

### Changed

- Kit: the registry is 0.8.0 and the AI Coordinator profile is 0.7.0. The AI Coordinator profile fixes the
  order of the steps of a project, requires a recorded phase check before any Work Package that builds the
  product and forbids skipping or reducing a mandatory phase on its own choice; `STATO.md` and
  `tools/vista_manager.py` add the phase of each package and an automatic bad news when build work starts
  with Discovery or Design and planning not closed. The Design Thinking Facilitator profile (0.5.0) and the
  AI Coordinator profile carry the engagement brief of Discovery; the AI Reviewer profile (0.3.0) checks the
  phase check. Details in the registry changelog, entries 0.7.0 and 0.8.0.
- With this kit the AI Coordinator states the applicability gate in full: a project whose class exceeds the
  qualified level of the adopter does not start (Guide §14). An adoption at level 0 cannot start a project of
  class 1 or 2, for example one that keeps data of colleagues; with the kits up to 0.8.1 such projects
  started after a decision of the Human Manager.
- Projects pages (`progetti.html`, `en/projects.html`): 433 catalogued tasks (they said 432).
- Role Profiles pages, read from the registry: the catalogues of the changed profiles.
- The start prompt in `come-usarlo.html` and `en/how-to-use.html` carries the SHA-256 of the new kit.
- `manifest.json`: `version` 0.9.0, `kit.version` 0.9.0, `kit.bundled` gives `registry` 0.8.0 and
  `ai_coordinator_profile` 0.7.0.
- CI: `PROFILES_REF` in `site-build.yml` pins role-profiles 0.8.0.

The known gaps of 0.8.0 stay open: the pages that tell the method still follow specification 0.3, and the
kit does not contain the Guide.

## [0.8.1] - 2026-11-26

Scope: Change Request CR-010 of the method project. The kit follows the Role Profiles registry 0.6.1
(commit `ab294eff14d5b88ef4b40fd63bacead2399e450c`), a PATCH that corrects 0.6.0 after its independent re-review.
Site bump: PATCH, a bundled artifact has a PATCH (VERSIONING §2.4). Kit 0.8.0 → 0.8.1: PATCH.

### Changed

- Kit: the registry is 0.6.1 and the AI Coordinator profile is 0.5.1; the bundled files that change are those
  listed in the registry changelog, entry 0.6.1 (the AI Coordinator profile, `_seniority/SENIORITY.md`, five
  family files, two profiles and the registry changelog).
- The start prompt in `come-usarlo.html` and `en/how-to-use.html` carries the SHA-256 of the new kit.
- `manifest.json`: `version` 0.8.1, `kit.version` 0.8.1, `kit.bundled` gives `registry` 0.6.1 and
  `ai_coordinator_profile` 0.5.1.
- CI: `PROFILES_REF` in `site-build.yml` pins role-profiles 0.6.1.

No page text changes. The known gaps of 0.8.0 stay open.

## [0.8.0] - 2026-11-26

Scope: two Change Requests of the method project released together. CR-007 implements RFC 0002
(`guide/rfcs/0002-governo-family.md`), alternative B (Do-S18). CR-010 (Wave CONS-01) brings the site and the
kit to the Role Profiles registry 0.6.0 (candidate commit `8eb5fa852faeac6ea91219b85beb30b4f512c31b`), which is
aligned to The Eiraman Guide 1.0.0-rc.3. The first candidate of this version (Wave GOV-01) followed registry
0.4.2 with kit 0.7.1 and was never published; this entry replaces it. Site bump: MINOR, content (VERSIONING
§2.4). Kit 0.7.0 → 0.8.0: MINOR, because the bundled registry and the bundled AI Coordinator profile have a
MINOR, marked breaking in the registry changelog.

**Order of publication:** tools 0.3.0, then role-profiles 0.6.0, then this release.

### Changed

- About page (`chi-sono.html`, `en/about.html`), "Family groups" tile ("Gruppi di famiglia"): the list ends
  with "Governance & Assurance", the family group of `governo/` created by RFC 0002, in Italian and English.
  Until this release Do-S16 kept Governo off the list; the description of family groups is unchanged.
- Role Profiles pages (`role-profile.html`, `en/role-profiles.html`), read from the registry: the AI Scrum
  Master is listed in Functional analysis (registry 0.5.0); the Digital Seniority paragraph says that a task
  outside the list runs at the fallback level the mandate sets, indicative value SD3, and SD4 for
  architecture, security and effects hard to undo (it said "runs at SD4"); in the table of levels the word
  "fallback" moves from SD4 to SD3, as an indicative fallback.
- Projects pages (`progetti.html`, `en/projects.html`), the counts of the registry: 48 profiles in 8 families
  and 432 catalogued tasks (they said 47 and 420).
- Manager View description: Work Packages in progress show the mandatory checks passed over the total (it
  said "with their percentage").
- Kit: the registry is 0.6.0 and the AI Coordinator profile is 0.5.0, with `STATO.md` and
  `tools/vista_manager.py` of that release; `role-profiles/governo/FAMIGLIA.md` is 0.2.3;
  `role-profiles/README.md` names Governance & Assurance. The changes of the bundled files are in the
  registry changelog, entries 0.5.0, 0.5.1 and 0.6.0.
- The start prompt in `come-usarlo.html` and `en/how-to-use.html` carries the SHA-256 of the new kit.
- `manifest.json`: `version` 0.8.0, `kit.version` 0.8.0, and `kit.bundled` gives `registry` 0.6.0 and
  `ai_coordinator_profile` 0.5.0. `date` stays 2026-11-26.
- CI: `PROFILES_REF` in `site-build.yml` pins the role-profiles 0.6.0 candidate commit
  (`8eb5fa852faeac6ea91219b85beb30b4f512c31b`, not yet tagged).

No page is added or removed. Compared with the deployed 0.7.0, the served files that change are the two About
pages, the two start-prompt pages, the two Role Profiles pages, the two Projects pages and the kit.

### Known gaps

- The pages that tell the method (how it works, phases, quality, the method map) still follow specification
  0.3. Where the Guide 1.0.0-rc.3 replaced a rule, the page and the kit differ: for example the page says
  that the agent of scripted functional tests "fixes trivial errors itself", that convergence is "by a single
  analyst" and that verification of security and personal data "uses a different model", while the profiles
  in the kit follow the Guide. Bringing those pages to the Guide is a content change of its own.
- The kit ships specification 0.3 as `framework/Eiraman.md` and does not contain the Guide. The AI
  Coordinator profile in the kit says on which rules it prevails over the specification.

## [0.7.0] - 2026-11-26

Scope: Change Requests CR-004, CR-005 and CR-006 of the method project (Wave REL-07). The site and the kit
follow the Role Profiles registry 0.4.1 (`role-profiles@v0.4.1`, commit
`a49e54b579025bff9afbe32b90c6a75771d4c6ee`). Kit version 0.7.0: the kit content changes. No generator code
changes; the only text change is the registry figures on the Projects page.

### Added

- Role Profiles page (`role-profile.html`, `en/role-profiles.html`): the Governo family shows seven
  profiles, with the new cards of `governo/revisore-architettura-cloud`,
  `governo/revisore-architettura-applicativa-dati`, `governo/revisore-test-qualita` and
  `governo/revisore-legale-compliance` (all 0.1.0, 9 tasks each). The profile count shown goes from 44 to
  48 (47 standard profiles plus the AI Coordinator).
- Kit: the folders of the four new reviewer profiles under `role-profiles/governo/`.

### Changed

- Kit: `CONTROLLORE.md` is the AI Coordinator profile 0.4.2 (was 0.4.1); `role-profiles/governo/FAMIGLIA.md`
  is 0.2.1 (was 0.2.0); `role-profiles/README.md` follows the registry 0.4.1.
- Projects page (`progetti.html`, `en/projects.html`), case of the method itself: the registry holds 47
  profiles in 8 families plus the AI Coordinator, with 420 catalogued tasks (it said 43 and 384), in Italian
  and English. The figures are counted from registry 0.4.1 and written in the text.
- The start prompt in `come-usarlo.html` and `en/how-to-use.html` carries the SHA-256 of the new kit; no
  other change on those pages.
- `manifest.json`: `version` 0.7.0, `kit.version` 0.7.0, and `kit.bundled` gives `registry` 0.4.1 and
  `ai_coordinator_profile` 0.4.2. `date` stays 2026-11-26.
- CI: `PROFILES_REF` in `site-build.yml` pins role-profiles v0.4.1
  (`a49e54b579025bff9afbe32b90c6a75771d4c6ee`).

### Fixed

- CI, `compliance.yml`: the local-path check removes http(s) URLs from the matched lines and matches
  again, so a path segment inside a URL is no longer flagged. The block is the one of `role-profiles`
  v0.4.1; the whole workflow file is now identical to that one (CR-005, CR-006). No served file changes
  because of it.

No page is added or removed. Compared with the deployed 0.6.0, the served files that change are the two Role
Profiles pages, the two start-prompt pages, the two Projects pages and the kit.

## [0.6.0] - 2026-11-26

The site and the kit follow the Role Profiles registry 0.3.0 (`role-profiles@v0.3.0`, commit
`adeedb4c940c637f93d46a9b58d22839e6dfee7a`). Kit version 0.6.0: the kit content changes. No generator
code changes; the only text change is the registry figures on the Projects page.

### Added

- Role Profiles page (`role-profile.html`, `en/role-profiles.html`): the Governo family shows three
  profiles, with the new cards of `governo/revisore-sicurezza` 0.1.0 and `governo/revisore-privacy` 0.1.0
  (9 tasks each). The profile count shown goes from 42 to 44 (43 standard profiles plus the AI
  Coordinator).
- Kit: `role-profiles/governo/revisore-sicurezza/` and `role-profiles/governo/revisore-privacy/`.

### Changed

- Kit: `CONTROLLORE.md` is the AI Coordinator profile 0.4.1 (was 0.4.0); `role-profiles/governo/FAMIGLIA.md`
  is 0.2.0 (was 0.1.0); `role-profiles/README.md` follows the registry 0.3.0.
- Projects page (`progetti.html`, `en/projects.html`), case of the method itself: the registry holds 43
  profiles in 8 families plus the AI Coordinator, with 384 catalogued tasks (it said 41 and 366), in Italian
  and English. The figures are counted from registry 0.3.0 and written in the text.
- The start prompt in `come-usarlo.html` and `en/how-to-use.html` carries the SHA-256 of the new kit; no
  other change on those pages.
- `manifest.json`: `version` 0.6.0, `kit.version` 0.6.0, and `kit.bundled` gives `registry` 0.3.0 and
  `ai_coordinator_profile` 0.4.1. `date` stays 2026-11-26.
- CI: `PROFILES_REF` in `site-build.yml` pins role-profiles v0.3.0
  (`adeedb4c940c637f93d46a9b58d22839e6dfee7a`).

No page is added or removed. Compared with the deployed 0.5.0, the served files that change are the two Role
Profiles pages, the two start-prompt pages, the two Projects pages and the kit.

## [0.5.0] - 2026-11-26

The site and the kit follow the Role Profiles registry 0.2.0 (`role-profiles@v0.2.0`, commit
`77ca4d0e80ac4c0fef441ae39ea141b117590eca`). Kit version 0.5.0: the kit content changes. The kit still contains no tools, and the site build does not
reference the tools repository.

### Added

- Role Profiles page (`role-profile.html`, `en/role-profiles.html`): the family **Governo** (Governance),
  with its one profile `governo/revisore-ai` 0.1.0, the AI Reviewer. The profile count shown goes from
  41 to 42 (41 standard profiles plus the AI Coordinator). The generator lists the families in a fixed
  table (`RP_FAM` in `generator/content.py`), so the family needed a new entry there: name and one-line
  description in Italian and English, and an icon. No other generator text changes.
- Kit: `role-profiles/governo/FAMIGLIA.md` and `role-profiles/governo/revisore-ai/` (the AI Reviewer
  profile), and the templates `role-profiles/_modello/business-analyst/` and
  `role-profiles/_modello/user-persona/`.

### Changed

- Role Profiles page: the cards of `analisi-funzionale/analista-funzionale` (0.1.0 → 0.2.0, 11 → 12
  tasks) and `analisi-funzionale/facilitatore-design-thinking` (0.1.0 → 0.2.0, 7 → 11 tasks) show their
  new short descriptions, task counts and first example tasks, read from `profilo.json` at registry 0.2.0.
  On the English page the facilitator's name becomes "Design Thinking Facilitator" (`nome_en` of the
  registry, glossary of the Guide 1.0.0-rc.2).
  Two example tasks of the analyst's card are replaced, because its catalogue changed. The card of
  `utente-simulato` (0.1.0 → 0.2.0) shows the same text as before.
- Kit: `CONTROLLORE.md` is the AI Coordinator profile 0.4.0 (was 0.3.0); `AVVIO.md` adds the paragraph on
  setting up the AI Reviewer; `role-profiles/README.md` and the files of the family `analisi-funzionale`
  (`FAMIGLIA.md`, `analista-funzionale`, `facilitatore-design-thinking`, `utente-simulato`) follow the
  registry 0.2.0.
- The start prompt in `come-usarlo.html` and `en/how-to-use.html` carries the SHA-256 of the new kit; no
  other change on those pages.
- `manifest.json`: `version` 0.5.0, `kit.version` 0.5.0, and `kit.bundled` gives `registry` 0.2.0 and
  `ai_coordinator_profile` 0.4.0.
- CI: `PROFILES_REF` in `site-build.yml` pins role-profiles v0.2.0
  (`77ca4d0e80ac4c0fef441ae39ea141b117590eca`).
- Projects page (`progetti.html`, `en/projects.html`), case of the method itself: it now says the registry holds 41 profiles in 8 families
  plus the AI Coordinator, with 366 catalogued tasks (it said 40, 7 and 350, the figures of registry
  0.1.1), in Italian and English. The numbers are written in the text, not read from the registry.
- `manifest.json`: `date` is the release date, 2026-11-26 (it stayed at 2026-11-25 in 0.4.1).

### Fixed

- Role Profiles page: a family with one profile shows the singular label, "1 profilo" / "1 profile",
  instead of "1 profili" / "1 profiles". The generator already had the singular label (`n1`) for the AI
  Coordinator tile; the family tile and pane now use it when the count is 1. The Governo family is the
  first with a single profile.

No page is added or removed. Compared with the deployed 0.4.1, the served files that change are the two Role
Profiles pages, the two start-prompt pages, the two Projects pages and the kit.

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

[Unreleased]: https://github.com/eiraman/site/compare/v0.10.0...main
[0.10.0]: https://github.com/eiraman/site/compare/v0.9.0...v0.10.0
[0.9.0]: https://github.com/eiraman/site/compare/v0.8.1...v0.9.0
[0.8.1]: https://github.com/eiraman/site/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/eiraman/site/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/eiraman/site/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/eiraman/site/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/eiraman/site/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/eiraman/site/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/eiraman/site/releases/tag/v0.4.0
