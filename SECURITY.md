# Security Policy

## Scope

`yt-view-bot` runs a local Playwright-driven Chromium worker that
simulates watch sessions on YouTube. It does not phone home, upload
telemetry, or store credentials outside the local `sessions/` folder.

## Reporting a vulnerability

Email the maintainer (see GitHub profile) with:
- affected module and version
- reproduction steps
- suggested fix if you have one

Please do **not** open a public issue for anything that could be
weaponized (e.g. session-token leakage, proxy credential exposure).

## Supported versions

Only the latest tagged release on `main` receives security fixes.

## Out of scope

- Getting a channel banned / ToS enforcement outcomes
- Proxy provider quality
- YouTube-side rate limits