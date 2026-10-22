from __future__ import annotations

import random

from playwright.async_api import Page

from ytview.models.config import BotConfig
from ytview.utils.delays import jitter_sleep


class WatchHandler:
    def __init__(self, page: Page, cfg: BotConfig) -> None:
        self.page = page
        self.cfg = cfg

    async def simulate_watch(self) -> int:
        target = random.randint(self.cfg.min_watch_seconds, self.cfg.max_watch_seconds)
        elapsed = 0
        while elapsed < target:
            step = random.randint(20, 45)
            await jitter_sleep(step, step + 10)
            elapsed += step
            if random.random() < 0.15:
                await self._nudge_player()
        return elapsed

    async def _nudge_player(self) -> None:
        try:
            await self.page.mouse.move(
                random.randint(200, 800), random.randint(200, 600)
            )
        except Exception:
            pass