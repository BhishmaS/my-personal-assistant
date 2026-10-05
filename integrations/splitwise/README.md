# Splitwise integration

Account access for Splitwise (shared expenses), connected 2026-10-04.

## How it is stored

There is no custom connector, API client, or skill for Splitwise — all work
happens through live browser tasks. The account signs in with Google, so
there is no Splitwise password and nothing is stored in the Secure Vault.
Access depends on the Google session in the assistant's browser.

## How it is used

When asked to check balances or add expenses, the assistant opens
https://secure.splitwise.com/ in the browser (reusing the existing Google
session) and reads or edits as requested. Nothing is created, edited, or
deleted without explicit approval.

## Notes

- The Google sign-in was completed once by the user via browser takeover.
  The session persists across tasks, but if it expires the user needs to
  sign in again via takeover — the assistant tries the existing session
  first and only asks when it is actually gone.
- On 2026-10-04 the account's default currency was switched INR→USD and
  timezone Chennai→Pacific Time, so dashboard totals now display in dollars.
