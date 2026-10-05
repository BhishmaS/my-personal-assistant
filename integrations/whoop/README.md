# WHOOP integration

WHOOP fitness tracker integration for the personal assistant.

## Layout

- `SKILL.md` + `scripts/` — the assistant skill that reads WHOOP data (recovery,
  sleep, strain, workouts, profile) via the WHOOP v2 API
  (`https://api.prod.whoop.com/developer/v2`).
  - `scripts/whoop.py` — CLI: `profile`, `recovery`, `sleep`, `workouts`, `cycles`
    (JSON on stdout).
  - `scripts/dynamic_credentials.py` — auth helper. In the assistant environment,
    auth goes through a secure credential exchange; no raw key is stored here.
- `privacy-policy.md` — privacy policy for the WHOOP OAuth app registration.

## Notes

- The WHOOP OAuth app itself is registered in the WHOOP Developer Dashboard;
  its credentials live in the assistant's secure credential store, not in this repo.
- Dashboard snapshots live in the top-level `dashboards/` folder, not here.
