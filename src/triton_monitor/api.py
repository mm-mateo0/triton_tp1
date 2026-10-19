
from datetime import datetime, timezone
from collections import Counter
from typing import Any

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Proyecto Tritón",
    description="Sistema de telemetría y observabilidad asíncrona",
    version="1.0.0",
)

metrics = Counter()


class TelemetryEvent(BaseModel):
    provider: str = "unknown"
    service: str = "api"
    event: str = "unspecified"
    value: Any = 1


@app.get("/health")
async def health():
    return {"status": "ok", "project": "Tritón"}


@app.get("/metrics")
async def get_metrics():
    return dict(metrics)


@app.post("/telemetry", status_code=202)
async def receive_telemetry(event: TelemetryEvent):
    metrics["events_received"] += 1
    metrics[f"provider:{event.provider}"] += 1
    metrics[f"service:{event.service}"] += 1

    return {
        "accepted": True,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "record": event.model_dump(),
    }
