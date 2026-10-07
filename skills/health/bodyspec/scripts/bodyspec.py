#!/usr/bin/env python3
"""bodyspec.py — read the user's BodySpec DEXA data via the connected
custom.bodyspec credential.

Usage:
    bodyspec.py me
    bodyspec.py appts
    bodyspec.py results
    bodyspec.py result <result_id>
    bodyspec.py dexa <result_id> <section>
        section: scan-info | composition | bone-density | percentiles |
                 visceral-fat | rmr

Prints JSON to stdout. Auth goes through authd surrogates; no raw
credential is ever handled here.
"""

from __future__ import annotations

import argparse
import json
import sys
import urllib.request

sys.path.insert(0, __file__.rsplit("/", 1)[0])

from dynamic_credentials import (  # noqa: E402
    DynamicCredentialError,
    add_surrogate_to_request,
    read_json_response,
)

API_BASE = "https://app.bodyspec.com"
ALLOWED_HOSTS = ["app.bodyspec.com"]
CREDENTIAL_NAME = "custom.bodyspec"

DEXA_SECTIONS = (
    "scan-info",
    "composition",
    "bone-density",
    "percentiles",
    "visceral-fat",
    "rmr",
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Read BodySpec DEXA data.")
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("me", help="BodySpec user profile.")
    sub.add_parser("appts", help="User appointments.")
    sub.add_parser("results", help="List scan results.")

    p = sub.add_parser("result", help="One result's details.")
    p.add_argument("result_id")

    p = sub.add_parser("dexa", help="One result's DEXA section.")
    p.add_argument("result_id")
    p.add_argument("section", choices=DEXA_SECTIONS)
    return parser


def get(path: str) -> dict:
    url = API_BASE + path
    request = urllib.request.Request(url, method="GET")
    request.add_header("User-Agent", "Muse-BodySpec-Skill/1.0")
    request.add_header("Accept", "application/json")
    add_surrogate_to_request(
        request, CREDENTIAL_NAME, allowed_hosts=ALLOWED_HOSTS
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as resp:
            return read_json_response(resp)
    except urllib.error.HTTPError as exc:  # type: ignore[attr-defined]
        try:
            body = exc.read().decode("utf-8", errors="replace")[:500]
        except Exception:
            body = ""
        raise DynamicCredentialError(
            f"BodySpec API returned HTTP {exc.code}: {body}"
        ) from exc


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "me":
            data = get("/api/v1/users/me")
        elif args.command == "appts":
            data = get("/api/v1/users/me/appts")
        elif args.command == "results":
            data = get("/api/v1/users/me/results/")
        elif args.command == "result":
            data = get(f"/api/v1/users/me/results/{args.result_id}")
        elif args.command == "dexa":
            data = get(
                f"/api/v1/users/me/results/{args.result_id}"
                f"/dexa/{args.section}"
            )
        else:  # pragma: no cover - argparse enforces the choices
            raise AssertionError(args.command)
    except DynamicCredentialError as exc:
        print(json.dumps({"error": str(exc)}), file=sys.stderr)
        return 1
    print(json.dumps(data, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
