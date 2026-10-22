"""SessionHandler — orchestrates a single simulated watch session."""
from __future__ import annotations

from ytview.handlers.navigation_handler import NavigationHandler
from ytview.handlers.watch_handler import WatchHandler
from ytview.models.config import BotConfig
from ytview.models.session import SessionState
from ytview.services.browser_factory import BrowserFactory


class SessionHandler:
    def __init__(self, cfg: BotConfig, *, worker_id: int, proxy: str | None) -> None:
        self.cfg = cfg
        self.worker_id = worker_id
        self.proxy = proxy
        self.state = SessionState(worker_id=worker_id)

    async def run(self) -> int:
        factory = BrowserFactory(self.cfg, proxy=self.proxy)
        async with factory.launch() as page:
            nav = NavigationHandler(page, self.cfg)
            await nav.open_target()
            self.state.mark("navigated")

            watcher = WatchHandler(page, self.cfg)
            watched = await watcher.simulate_watch()
            self.state.mark("watched", seconds=watched)
            return watched