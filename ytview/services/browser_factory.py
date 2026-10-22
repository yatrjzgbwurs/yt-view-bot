from __future__ import annotations

from contextlib import asynccontextmanager
from typing import AsyncIterator

from playwright.async_api import Page, async_playwright

from ytview.models.config import BotConfig


class BrowserFactory:
    def __init__(self, cfg: BotConfig, *, proxy: str | None = None) -> None:
        self.cfg = cfg
        self.proxy = proxy

    @asynccontextmanager
    async def launch(self) -> AsyncIterator[Page]:
        async with async_playwright() as pw:
            launch_kwargs: dict = {"headless": self.cfg.headless}
            if self.proxy:
                launch_kwargs["proxy"] = {"server": self.proxy}
            browser = await pw.chromium.launch(**launch_kwargs)
            ctx = await browser.new_context(
                user_agent=self.cfg.user_agent,
                viewport={"width": 1366, "height": 768},
            )
            page = await ctx.new_page()
            try:
                yield page
            finally:
                await ctx.close()
                await browser.close()