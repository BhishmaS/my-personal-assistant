---
name: "bodyspec"
description: "Read BodySpec DEXA scan data: body composition, visceral fat, bone density, percentiles, RMR, scan history, and appointments."
---

# Bodyspec

## Purpose
Use Bodyspec with the user-connected `custom.bodyspec` credential.

## Commands
Run `scripts/bodyspec.py`:
- `me` — BodySpec user profile
- `appts` — appointments
- `results` — list scan results
- `result <result_id>` — one result's details
- `dexa <result_id> <section>` — DEXA detail; section is one of
  `scan-info`, `composition`, `bone-density`, `percentiles`,
  `visceral-fat`, `rmr`

All commands print JSON to stdout.

## Tooling
Service-specific CLIs live under `scripts/`.

CLIs must use authd or shared connector helpers for authenticated requests. They must not read OAuth client credentials, browser callback payloads, refresh tokens, access tokens, or Muse auth files directly.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, call `credentials.request_api_access` with `reconnect` to replace it. The connector is stored as `custom.bodyspec`.

## Operating Rules
1. Use this skill when the user asks for Bodyspec or this provider's API.
2. Restrict authenticated requests to: app.bodyspec.com.
3. Do not print, log, or persist raw credentials.
4. If auth is missing or rejected, follow the Auth section rather than asking for a key.
