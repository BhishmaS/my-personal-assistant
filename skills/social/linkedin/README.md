# LinkedIn integration

Account access for LinkedIn, connected 2026-10-05.

## How it is stored

There is no custom connector, API client, or skill for LinkedIn — all work
happens through live browser tasks. A username + password login is saved in
the Secure Vault (the user entered it via the secure entry card on
2026-10-05).

## How it is used

When asked to check the feed, profile, messages, or job-related details, the
assistant opens https://www.linkedin.com/ in the browser (reusing the saved
login) and reads as requested. Nothing is posted, messaged, applied to, or
changed without explicit approval.

## Notes

- Sign-in was verified working on 2026-10-05 with no extra verification step
  (no CAPTCHA or code). LinkedIn may occasionally ask for verification on
  new sessions.
- The browser session persists across tasks, but if it expires the saved
  login is used to sign in again.
