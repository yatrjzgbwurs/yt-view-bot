from __future__ import annotations

from playwright.async_api import Page

from ytview.models.config import BotConfig
from ytview.utils.delays import jitter_sleep


class NavigationHandler:
    def __init__(self, page: Page, cfg: BotConfig) -> None:
        self.page = page
        self.cfg = cfg

    async def open_target(self) -> None:
        await self.page.goto(self.cfg.target_url, wait_until="domcontentloaded")
        await jitter_sleep(1.2, 2.8)
        # dismiss cookie / consent overlays if present
        for sel in ("button[aria-label*='Accept']", "tp-yt-paper-button#button"):
            try:
                await self.page.click(sel, timeout=1500)
                break
            except Exception:
                continue