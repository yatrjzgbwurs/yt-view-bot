from __future__ import annotations

from pathlib import Path

import yaml
from pydantic import BaseModel, Field


class BotConfig(BaseModel):
    target_url: str = Field(..., description="YouTube watch URL")
    workers: int = 3
    min_watch_seconds: int = 45
    max_watch_seconds: int = 180
    headless: bool = True
    log_level: str = "INFO"
    proxy_file: str | None = None
    user_agent: str = (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/131.0.0.0 Safari/537.36"
    )


def load_config(path: str | Path) -> BotConfig:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    return BotConfig(**raw)