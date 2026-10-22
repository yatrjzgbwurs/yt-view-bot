"""WatchEngine — spawns N async workers, each running a WatchSession."""
from __future__ import annotations

import asyncio
from dataclasses import dataclass

from ytview.core.logger import get_logger
from ytview.handlers.session_handler import SessionHandler
from ytview.models.config import BotConfig
from ytview.services.proxy_pool import ProxyPool


@dataclass
class WorkerResult:
    worker_id: int
    watched_seconds: int
    success: bool
    reason: str = ""


class WatchEngine:
    def __init__(self, cfg: BotConfig, *, dry_run: bool = False) -> None:
        self.cfg = cfg
        self.dry_run = dry_run
        self.log = get_logger(cfg.log_level)
        self.pool = ProxyPool.from_file(cfg.proxy_file) if cfg.proxy_file else ProxyPool.empty()

    async def _worker(self, wid: int) -> WorkerResult:
        proxy = self.pool.next()
        handler = SessionHandler(self.cfg, worker_id=wid, proxy=proxy)
        try:
            watched = await handler.run()
            return WorkerResult(wid, watched, True)
        except Exception as exc:  # noqa: BLE001
            self.log.exception("worker %d failed: %s", wid, exc)
            return WorkerResult(wid, 0, False, str(exc))

    async def _run_all(self) -> list[WorkerResult]:
        tasks = [self._worker(i) for i in range(self.cfg.workers)]
        return await asyncio.gather(*tasks)

    def run(self) -> list[WorkerResult]:
        if self.dry_run:
            self.log.info("dry-run: skipping browser launch")
            return []
        return asyncio.run(self._run_all())