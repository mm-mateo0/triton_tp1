
from fastapi.testclient import TestClient

from src.triton_monitor.api import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_receive_telemetry():
    response = client.post(
        "/telemetry",
        json={
            "provider": "aws",
            "service": "api",
            "event": "request_completed",
            "value": 1,
        },
    )
    assert response.status_code == 202
    assert response.json()["accepted"] is True
