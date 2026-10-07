#!/usr/bin/env python3
"""whoop.py — read the user's WHOOP data via the connected custom.whoop credential.

Usage:
    whoop.py profile
    whoop.py recovery [--start ISO] [--end ISO] [--limit N]
    whoop.py sleep    [--start ISO] [--end ISO] [--limit N]
    whoop.py workouts [--start ISO] [--end ISO] [--limit N]
    whoop.py cycles   [--start ISO] [--end ISO] [--limit N]

Dates are ISO-8601 (e.g. 2026-10-01T00:00:00Z). Prints JSON to stdout.
Auth goes through authd surrogates; no raw credential is ever handled here.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.parse
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from dynamic_credentials import (  # noqa: E402
    DynamicCredentialError,
    add_surrogate_to_request,
    read_json_response,
)

API_BASE = "https://api.prod.whoop.com"
ALLOWED_HOSTS = ["api.prod.whoop.com"]
CREDENTIAL_NAME = "custom.whoop"

ENDPOINTS = {
    "profile": "/developer/v2/user/profile/basic",
    "recovery": "/developer/v2/recovery",
    "sleep": "/developer/v2/activity/sleep",
    "workouts": "/developer/v2/activity/workout",
    "cycles": "/developer/v2/cycle",
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read WHOOP health data.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("profile", help="Basic user profile.")

    for name in ("recovery", "sleep", "workouts", "cycles"):
        p = sub.add_parser(name, help=f"WHOOP {name} data.")
        p.add_argument("--start", default=None, help="ISO-8601 start, e.g. 2026-10-01T00:00:00Z")
        p.add_argument("--end", default=None, help="ISO-8601 end")
        p.add_argument("--limit", default=None, help="Max records per page")
    return parser


def get(path: str, params: dict | None = None) -> dict:
    url = API_BASE + path
    if params:
        query = {k: v for k, v in params.items() if v is not None}
        if query:
            url += "?" + urllib.parse.urlencode(query)
    request = urllib.request.Request(url, method="GET")
    request.add_header("User-Agent", "Muse-WHOOP-Skill/1.0")
    request.add_header("Accept", "application/json")
    add_surrogate_to_request(
        request, CREDENTIAL_NAME, allowed_hosts=ALLOWED_HOSTS
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as resp:
            return read_json_response(resp)
    except urllib.error.HTTPError as exc:  # type: ignore[attr-defined]
        try:
            body = exc.read().decode("utf-8", errors="replace")[:500]
        except Exception:
            body = ""
        raise DynamicCredentialError(
            f"WHOOP API returned HTTP {exc.code}: {body}"
        ) from exc


def main() -> int:
    args = build_parser().parse_args()
    try:
        if args.command == "profile":
            data = get(ENDPOINTS["profile"])
        else:
            data = get(
                ENDPOINTS[args.command],
                {"start": args.start, "end": args.end, "limit": args.limit},
            )
    except DynamicCredentialError as exc:
        print(f"whoop: error: {exc}", file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
