<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: Apache-2.0
-->

# Changelog of the Eiraman kit

All notable changes to the Eiraman kit (`kit/eiraman-kit.zip`, served at eiraman.tech) are documented in this
file. The format is based on [Keep a Changelog 1.1](https://keepachangelog.com/en/1.1.0/), and versions follow
the rules in [community/VERSIONING.md](https://github.com/eiraman/community/blob/main/VERSIONING.md). The kit
version is `KIT_VERSION` in `generator/build.py` and `kit.version` in `manifest.json`.

The kit is built by the generator of this repository, and its history up to now is told in the changelog of
the repository, [CHANGELOG.md](../CHANGELOG.md): for the earlier and the joint history of the kit and the
site, read that file. This file starts with the entries below, which are extracted from it (Change Request
CR-025, decision D-VER-2). A kit change that is released together with a site change appears in both files.

The kit has its own line, which continues the 0.3.x copies named in the licence notice (`LICENSE.md` in the
kit): up to 0.3.x the kit was distributed under CC BY-NC-ND 4.0 and MIT, and those copies are not described
here. The entries record what the repository changelog states about the kit; where it does not say, the entry
says so.

## [Unreleased]

## [0.9.0] - 2026-11-26

The registry is 0.8.0 and the AI Coordinator profile is 0.7.0. A first candidate of this version followed
registry 0.7.0 and was never published. MINOR. Source: [CHANGELOG.md](../CHANGELOG.md), 0.9.0.

### Changed

- The AI Coordinator profile fixes the order of the steps of a project, requires a recorded phase check before
  any Work Package that builds the product and forbids skipping or reducing a mandatory phase on its own
  choice; `STATO.md` and `tools/vista_manager.py` add the phase of each package and an automatic bad news when
  build work starts with Discovery or Design and planning not closed.
- The Design Thinking Facilitator profile (0.5.0) and the AI Coordinator profile carry the engagement brief of
  Discovery; the AI Reviewer profile (0.3.0) checks the phase check. Details in the registry changelog,
  entries 0.7.0 and 0.8.0.
- The AI Coordinator states the applicability gate in full: a project whose class exceeds the qualified level
  of the adopter does not start (Guide §14). An adoption at level 0 cannot start a project of class 1 or 2;
  with the kits up to 0.8.1 such projects started after a decision of the Human Manager.

## [0.8.1] - 2026-11-26

The registry is 0.6.1 and the AI Coordinator profile is 0.5.1 (CR-010). PATCH. Source:
[CHANGELOG.md](../CHANGELOG.md), 0.8.1.

### Changed

- The bundled files that change are those listed in the registry changelog, entry 0.6.1: the AI Coordinator
  profile, `_seniority/SENIORITY.md`, five family files, two profiles and the registry changelog.

## [0.8.0] - 2026-11-26

The registry is 0.6.0 and the AI Coordinator profile is 0.5.0, aligned to The Eiraman Guide 1.0.0-rc.3
(CR-007, CR-010). MINOR, because the bundled registry and the bundled AI Coordinator profile have a MINOR,
marked breaking in the registry changelog. A candidate that followed registry 0.4.2 with kit 0.7.1 (Wave
GOV-01) was never published; this entry replaces it. Source: [CHANGELOG.md](../CHANGELOG.md), 0.8.0.

### Changed

- `STATO.md` and `tools/vista_manager.py` are those of the AI Coordinator profile 0.5.0;
  `role-profiles/governo/FAMIGLIA.md` is 0.2.3; `role-profiles/README.md` names Governance & Assurance. The
  changes of the bundled files are in the registry changelog, entries 0.5.0, 0.5.1 and 0.6.0.

### Known gaps

- The kit ships specification 0.3 as `framework/Eiraman.md` and does not contain the Guide. The AI
  Coordinator profile in the kit says on which rules it prevails over the specification.

## [0.7.0] - 2026-11-26

The registry is 0.4.1 (CR-004, CR-005, CR-006). MINOR. Source: [CHANGELOG.md](../CHANGELOG.md), 0.7.0.

### Added

- The folders of the four new reviewer profiles under `role-profiles/governo/`:
  `revisore-architettura-cloud`, `revisore-architettura-applicativa-dati`, `revisore-test-qualita` and
  `revisore-legale-compliance`.

### Changed

- `CONTROLLORE.md` is the AI Coordinator profile 0.4.2 (was 0.4.1); `role-profiles/governo/FAMIGLIA.md` is
  0.2.1 (was 0.2.0); `role-profiles/README.md` follows the registry 0.4.1.

## [0.6.0] - 2026-11-26

The registry is 0.3.0. MINOR. Source: [CHANGELOG.md](../CHANGELOG.md), 0.6.0.

### Added

- `role-profiles/governo/revisore-sicurezza/` and `role-profiles/governo/revisore-privacy/`.

### Changed

- `CONTROLLORE.md` is the AI Coordinator profile 0.4.1 (was 0.4.0); `role-profiles/governo/FAMIGLIA.md` is
  0.2.0 (was 0.1.0); `role-profiles/README.md` follows the registry 0.3.0.

## [0.5.0] - 2026-11-26

The registry is 0.2.0. The kit still contains no validator or activation tools (those of the tools repository). MINOR. Source: [CHANGELOG.md](../CHANGELOG.md), 0.5.0.

### Added

- `role-profiles/governo/FAMIGLIA.md` and `role-profiles/governo/revisore-ai/` (the AI Reviewer profile), and
  the templates `role-profiles/_modello/business-analyst/` and `role-profiles/_modello/user-persona/`.

### Changed

- `CONTROLLORE.md` is the AI Coordinator profile 0.4.0 (was 0.3.0); `AVVIO.md` adds the paragraph on setting
  up the AI Reviewer.
- `role-profiles/README.md` and the files of the family `analisi-funzionale` (`FAMIGLIA.md`,
  `analista-funzionale`, `facilitatore-design-thinking`, `utente-simulato`) follow the registry 0.2.0.

## [0.4.0] - 2026-11-25

The first kit under the open licences, deployed during the restricted launch of 25 November 2026. The version
label of the kit was recorded in the generator on 26 November 2026 (repository changelog, 0.4.1); the kit
bytes did not change between that deployment and 0.4.1. Source: [CHANGELOG.md](../CHANGELOG.md), 0.4.0 and 0.4.1.

### Changed

- `LICENSE.md` and `LEGGIMI.md` state the new licences: Guide texts CC BY-SA 4.0, Role Profiles and AI
  Coordinator profile texts CC BY 4.0, code Apache-2.0; name and logo are trademarks outside these licences.
- The AI Coordinator profile ships as a draft, not qualified.

The repository changelog does not list the other files of this kit, nor its file count; the entry gives only
what it names. The manifest `kit` object (path, version, `bundled`) was added with the site 0.4.1.
