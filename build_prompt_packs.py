#!/usr/bin/env python3
"""Build Prompt Marketplace payloads from packs/ folders."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent
PACKS_DIR = ROOT / "packs"
OUTPUT_FILE = ROOT / "prompt-market-defaults.json"


def load_pack(metadata_path: Path) -> dict[str, Any]:
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    channel = metadata.get("channel")
    modules = metadata.get("modules", [])
    prompt_map: dict[str, str] = {}
    for module in modules:
        key = module["key"]
        path = metadata_path.parent / module["file"]
        prompt_map[key] = path.read_text(encoding="utf-8").rstrip() + "\n"

    item = {
        "id": metadata.get("id"),
        "name": metadata.get("name"),
        "locale": metadata.get("locale"),
        "scenario": metadata.get("scenario"),
        "version": metadata.get("version"),
        "description": metadata.get("description"),
        "tags": metadata.get("tags"),
    }
    if channel == "index":
        item["index_prompts"] = prompt_map
    elif channel == "query":
        item["query_prompts"] = prompt_map
    else:
        raise ValueError(f"Unknown channel '{channel}' in {metadata_path}")
    return item


def main() -> None:
    if not PACKS_DIR.exists():
        raise SystemExit(f"Pack directory {PACKS_DIR} does not exist")
    items = [load_pack(path) for path in sorted(PACKS_DIR.glob("**/metadata.json"))]
    payload = {"items": items}
    OUTPUT_FILE.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(items)} packs to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
