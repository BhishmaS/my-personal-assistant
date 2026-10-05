# Quest Diagnostics (MyQuest)

Notes on the Quest Diagnostics MyQuest patient-portal integration
(no API or connector; credentials stay in the Secure Vault).

## What it is
Quest Diagnostics offers no public API, and does not release records to
health-data aggregators (HealthEx was tried on 2026-10-05 and Quest
declined). Access is through the MyQuest patient portal in the browser.

## How access works
- Saved username + password login in the Secure Vault, used through
  browser sign-in — the credential persists but the browser session
  expires.
- Read-only use: retrieving lab test results. Nothing is ordered,
  changed, shared, or exported through the portal by the assistant.

## Linked (as of 2026-10-05)
- MyQuest patient portal — connected via browser sign-in on 2026-10-05.
