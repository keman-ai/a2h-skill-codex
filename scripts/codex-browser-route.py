#!/usr/bin/env python3
"""Build the only A2H Market URLs allowed in Codex's display-only Browser."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from urllib.parse import quote, urlencode

try:
    from _site_config import FRONT_BASE
except ModuleNotFoundError:
    # 源码树中站点配置仍在 kernel/scripts；构建产物则与本脚本并排。
    sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "kernel" / "scripts"))
    from _site_config import FRONT_BASE


MAX_QUERY_LENGTH = 200
MAX_IDENTIFIER_LENGTH = 160


def _clean(value: str, *, name: str, limit: int, required: bool) -> str:
    cleaned = value.strip()
    if required and not cleaned:
        raise ValueError(f"{name} must not be empty")
    if len(cleaned) > limit:
        raise ValueError(f"{name} must be at most {limit} characters")
    if any(ord(char) < 32 for char in cleaned):
        raise ValueError(f"{name} must not contain control characters")
    return cleaned


def _base() -> str:
    return FRONT_BASE.rstrip("/")


def market_url() -> str:
    return f"{_base()}/market"


def search_url(query: str, trade_type: str | None) -> str:
    cleaned_query = _clean(query, name="query", limit=MAX_QUERY_LENGTH, required=False)
    params: list[tuple[str, str]] = []
    if cleaned_query:
        params.append(("q", cleaned_query))
    if trade_type:
        params.append(("tradeType", trade_type))
    suffix = urlencode(params)
    return market_url() if not suffix else f"{market_url()}?{suffix}"


def resource_url(kind: str, identifier: str) -> str:
    cleaned = _clean(identifier, name=f"{kind}_id", limit=MAX_IDENTIFIER_LENGTH, required=True)
    path = "listings" if kind == "listing" else "messages"
    return f"{_base()}/{path}/{quote(cleaned, safe='')}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    scenarios = parser.add_subparsers(dest="scenario", required=True)
    scenarios.add_parser("market")

    search = scenarios.add_parser("search")
    search.add_argument("--query", default="")
    search.add_argument("--trade-type", choices=("SELL", "BUY"))

    listing = scenarios.add_parser("listing")
    listing.add_argument("--listing-id", required=True)

    thread = scenarios.add_parser("thread")
    thread.add_argument("--thread-id", required=True)
    args = parser.parse_args()

    try:
        if args.scenario == "market":
            url = market_url()
        elif args.scenario == "search":
            url = search_url(args.query, args.trade_type)
        elif args.scenario == "listing":
            url = resource_url("listing", args.listing_id)
        else:
            url = resource_url("thread", args.thread_id)
    except ValueError as error:
        parser.error(str(error))

    print(json.dumps({"scenario": args.scenario, "url": url}, ensure_ascii=False))


if __name__ == "__main__":
    main()
