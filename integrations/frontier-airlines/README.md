# Frontier Airlines integration

Account access for Frontier Airlines (bookings, FRONTIER Miles), connected 2026-10-04.

## How it is stored

There is no custom connector and no API client here — Frontier offers no
consumer API. The integration is a **saved website login** in the assistant's
Secure Vault (username + password for flyfrontier.com). No credential, token,
or secret is stored in this repo, ever.

## How it is used

When asked to check something on the Frontier account (trips, miles balance),
the assistant signs in at https://www.flyfrontier.com/ through the browser
using the saved login, then reads the needed pages. Nothing is booked,
changed, or cancelled without explicit approval.

## Notes

- Frontier sometimes requires a 6-digit email verification code after the
  password step. The code goes to the account email; the assistant pulls it
  from the connected inbox automatically when possible, otherwise asks for it.
- Browser sessions expire; the saved login persists and is reused for the
  next sign-in.
