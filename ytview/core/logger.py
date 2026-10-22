from __future__ import annotations

import logging
import sys
from pathlib import Path

_LOG_DIR = Path("logs")


def get_logger(level: str = "INFO") -> logging.Logger:
    logger = logging.getLogger("ytview")
    if logger.handlers:
        return logger

    logger.setLevel(level.upper())
    fmt = logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(fmt)
    logger.addHandler(stream)

    _LOG_DIR.mkdir(exist_ok=True)
    fh = logging.FileHandler(_LOG_DIR / "ytview.log", encoding="utf-8")
    fh.setFormatter(fmt)
    logger.addHandler(fh)
    return logger