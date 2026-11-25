<!--
SPDX-FileCopyrightText: 2026 Paolo Ungari and contributors
SPDX-License-Identifier: Apache-2.0
-->

# Provenance of the Eiraman logo

| File | Use | SHA-256 |
|---|---|---|
| `eiraman-su-chiaro.png` | logo on light backgrounds (site header) | `9725f7178879a801fe9905010582e13ddbc2b6526267f607ace461d8cd16da93` |
| `eiraman-su-scuro.png` | logo on dark backgrounds (site header) | `2770b4c52bc6b113ef49e5361f0ef49b8cdffd029a795d8f8579c3ca631219e1` |
| `eiraman-anteprima.png` | link preview image (Open Graph) | `beeb87792daa3c3e460e5493a840562125f19abf4582916f5a572c3d21d01ab5` |

The favicon (`favicon.svg`, `favicon.ico`, `apple-touch-icon.png`, `icon-512.png`) is drawn in code by
`generator/favicon.py` from the "E" of the logo, and the build regenerates the preview image from
`eiraman-su-chiaro.png`.

## How the logo was made

- The logo was generated with an AI image tool, on commission of the Author (Paolo Ungari).
- The Author compared the proposals and selected "Proposta C" (proposal C) in November 2026. The files
  above are that proposal, adapted for light and dark backgrounds.
- No third-party logo, font file or image was knowingly included.

## Legal status

- **Trademark.** The logo is one of the Eiraman Marks and is protected as a trademark under the
  [Trademark Policy](https://github.com/eiraman/community/blob/main/TRADEMARK.md). The Marks are not
  registered.
- **Copyright: uncertain.** Images generated with AI may not be protected by copyright, or only in part,
  depending on the human contribution and on the applicable law. The project makes no claim about the
  copyright status of the logo and relies on trademark protection.
- **Not covered by the open licences.** The logo files are excluded from CC BY-SA 4.0, CC BY 4.0 and the
  Apache License 2.0 used elsewhere in the project. They are declared in `REUSE.toml` as
  `LicenseRef-Eiraman-Trademark` (see `LICENSES/LicenseRef-Eiraman-Trademark.txt`).
- **Forks.** A fork of this repository must remove or replace the brand files unless the trademark policy
  allows the use. The generator builds without them, with a text wordmark.
