# Dashboards

Dynamic dashboards for personal analytics. These are living app frontends,
not static snapshots — each dashboard fetches live data (e.g. from the WHOOP
API) when opened, and they are meant to grow into real applications.

## Auth note

The WHOOP API needs OAuth. A dashboard served as a plain static page cannot
hold the client secret, so each dynamic dashboard needs one of:

- a tiny backend that keeps the OAuth credentials server-side and serves
  data to the frontend, or
- a browser-only OAuth flow with PKCE (public client, no secret), with the
  redirect URI registered on the WHOOP app.

## Dashboards

- `whoop-analytics-dashboard.html` — legacy static snapshot of WHOOP data
  (Sep 10 – Oct 4, 2026). Predates the dynamic approach; kept for reference
  until replaced by the dynamic WHOOP dashboard.
