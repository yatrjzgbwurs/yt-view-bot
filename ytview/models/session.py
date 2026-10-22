from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class SessionState:
    worker_id: int
    events: list[dict] = field(default_factory=list)

    def mark(self, name: str, **extra) -> None:
        self.events.append(
            {
                "event": name,
                "at": datetime.now(timezone.utc).isoformat(),
                **extra,
            }
        )
        return None