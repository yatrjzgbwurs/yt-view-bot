from __future__ import annotations

import asyncio
import random


async def jitter_sleep(low: float, high: float) -> None:
    """Sleep for a random duration to look human-ish."""
    await asyncio.sleep(random.uniform(low, high))


def backoff(attempt: int, base: float = 1.5, cap: float = 30.0) -> float:
    return min(cap, base ** attempt) + random.uniform(0, 0.5)