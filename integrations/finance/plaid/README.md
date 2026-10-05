# Plaid (Finances)

Snapshot of the built-in Plaid skill (reference copy; ask for a refresh to re-sync).

## What it is
Plaid is a built-in connector that links financial institutions (banks,
brokerages) so the assistant can read account data. It is read-only — it
cannot move money, pay bills, or change anything at the institution.
Credentials stay with the institution; the assistant never sees logins.

## Linked (as of 2026-10-05)
- Robinhood — individual brokerage account and crypto, linked through
  Plaid's OAuth flow on 2026-10-05.
- Bank of America — Adv SafeBalance Banking checking, linked through
  Plaid on 2026-10-05.
- Fidelity — linked through Plaid on 2026-10-05: two 401(k) plans
  (EPAM, ServiceNow), individual brokerage TOD, Health Savings Account,
  employee stock purchase plan, and restricted stock units.

## What the assistant can read
- Account metadata and balances
- Transactions and recurring activity
- Investment holdings and buy/sell/dividend activity
- Loans and liabilities
