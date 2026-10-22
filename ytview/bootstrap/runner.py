"""Bootstrap entry point — wires config, logging, and the watch engine."""
from __future__ import annotations

import argparse
import sys

from ytview.core.engine import WatchEngine
from ytview.core.logger import get_logger
from ytview.models.config import load_config
from ytview.utils.cli import render_banner


def _build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="ytview", description="YouTube viewer bot")
    p.add_argument("--config", default="config/default.yaml")
    p.add_argument("--target", help="override target video URL")
    p.add_argument("--workers", type=int, help="override worker count")
    p.add_argument("--dry-run", action="store_true")
    return p


def main(argv: list[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    render_banner()

    cfg = load_config(args.config)
    if args.target:
        cfg.target_url = args.target
    if args.workers:
        cfg.workers = args.workers

    log = get_logger(cfg.log_level)
    log.info("loaded config: target=%s workers=%d", cfg.target_url, cfg.workers)

    engine = WatchEngine(cfg, dry_run=args.dry_run)
    try:
        engine.run()
    except KeyboardInterrupt:
        log.warning("interrupted by user")
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())