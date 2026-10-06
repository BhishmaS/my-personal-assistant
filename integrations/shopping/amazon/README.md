# Amazon integration

Account access notes for Amazon, saved 2026-10-05.

## Status: browser sign-in blocked

Amazon explicitly blocks automated AI-agent access. When the assistant's
browser opened the sign-in page on 2026-10-05, Amazon showed: "Continued
access by an unauthorized AI agent violates Amazon's Conditions of Use," with
no sign-in form. The block was not bypassed, and sign-in was never attempted.

## How it is stored

A username + password login is saved in the Secure Vault (the user entered it
via the secure entry card on 2026-10-05). There is no Amazon connector or
public personal-account API — Amazon's official API is for sellers only.

## How it could be used

If Amazon's automated-access block is ever lifted or the user signs in
manually via browser takeover, the assistant could check orders and track
packages through live browser tasks. Until then, this login cannot be used by
the assistant. Sign-in verification was skipped at the user's request.
