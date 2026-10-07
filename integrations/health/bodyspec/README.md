# BodySpec integration

BodySpec DEXA scan integration for the personal assistant.

## Layout

- `SKILL.md` + `scripts/` — the assistant skill that reads BodySpec data
  (profile, appointments, scan results, and DEXA detail: body composition,
  bone density, percentiles, visceral fat, RMR) via the BodySpec REST API
  (`https://app.bodyspec.com/api/v1`).
  - `scripts/bodyspec.py` — CLI: `me`, `appts`, `results`, `result`,
    `dexa` (JSON on stdout).
  - `scripts/dynamic_credentials.py` — auth helper. In the assistant
    environment, auth goes through a secure credential exchange; no raw
    key is stored here.

## Notes

- Auth is OAuth 2.0 against BodySpec's identity service
  (auth.bodyspec.com). The OAuth client was self-registered through
  BodySpec's open client-registration endpoint with the assistant's
  callback URL; its credentials live in the assistant's secure credential
  store, not in this repo.
- BodySpec also offers an MCP server (`https://app.bodyspec.com/mcp`);
  this integration uses the REST API instead.
- First scan on file: appointments and results appear through the API as
  scans are booked and completed.
