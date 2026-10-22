from __future__ import annotations

import itertools
import threading
from pathlib import Path


class ProxyPool:
    def __init__(self, proxies: list[str]) -> None:
        self._proxies = proxies or []
        self._cycle = itertools.cycle(self._proxies) if self._proxies else None
        self._lock = threading.Lock()

    @classmethod
    def empty(cls) -> "ProxyPool":
        return cls([])

    @classmethod
    def from_file(cls, path: str | Path) -> "ProxyPool":
        p = Path(path)
        if not p.exists():
            return cls.empty()
        lines = [ln.strip() for ln in p.read_text(encoding="utf-8").splitlines()]
        return cls([ln for ln in lines if ln and not ln.startswith("#")])

    def next(self) -> str | None:
        with self._lock:
            if not self._cycle:
                return None
            return next(self._cycle)

    def __len__(self) -> int:
        return len(self._proxies)