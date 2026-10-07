---
name: "whoop"
description: "Read WHOOP health data: recovery, sleep, strain, workouts, and profile."
---

# WHOOP

## Purpose
Fetch the user's WHOOP metrics (recovery, sleep, strain, workouts) to answer health questions and support their health goal.

## Tooling
`scripts/whoop.py` — CLI for the WHOOP v2 API. Auth goes through the bundled
`scripts/dynamic_credentials.py` helper (authd surrogate exchange); no raw
credential is ever read, printed, or stored here.

```
scripts/whoop.py profile
scripts/whoop.py recovery [--start ISO] [--end ISO] [--limit N]
scripts/whoop.py sleep    [--start ISO] [--end ISO] [--limit N]
scripts/whoop.py workouts [--start ISO] [--end ISO] [--limit N]
scripts/whoop.py cycles   [--start ISO] [--end ISO] [--limit N]
```

Dates are ISO-8601 (e.g. `2026-10-01T00:00:00Z`). Output is JSON on stdout.
API base: `https://api.prod.whoop.com/developer/v2`.

## Auth
The credential is already stored; nothing here collects one. Never ask the user to paste a raw key in chat, set a secret environment variable, pass a secret flag, or write an auth file.

A 401 or 403 is a question about the request before it is a question about the key. Check that the credential was attached at all: a request built without the helpers named under Tooling carries nothing, and that looks exactly like a wrong or under-scoped token. Only once a request that did carry the credential is still rejected, call `credentials.request_api_access` with `reconnect` to replace it. The connector is stored as `custom.whoop`.

## Operating Rules
1. Use this skill when the user asks for WHOOP or this provider's API.
2. Restrict authenticated requests to: api.prod.whoop.com.
3. Do not print, log, or persist raw credentials.
4. If auth is missing or rejected, follow the Auth section rather than asking for a key.
