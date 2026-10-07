# DoorDash integration

Account access for DoorDash (food delivery), connected 2026-10-05.

## How it is stored

There is no custom connector, API client, or skill for DoorDash — all work
happens through live browser tasks. The account signs in with email plus an
SMS verification code, so there is no DoorDash password and nothing is stored
in the Secure Vault.

## How it is used

When asked to check orders or account details, the assistant opens
https://www.doordash.com/ in the browser and signs in as requested. Nothing
is ordered, changed, or cancelled without explicit approval.

## Notes

- Sign-in requires two steps: the email address on the account, then the full
  phone number on the account (DoorDash shows it masked) before it sends the
  SMS verification code. Both were completed once by the user via browser
  tasks on 2026-10-05.
- The browser session persists across tasks, but if it expires the sign-in
  (email + phone + fresh SMS code) has to be done again.
