from fastapi.testclient import TestClient

from mini_api.main import app

client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_sum() -> None:
    response = client.get("/api/v1/sum", params={"a": 2, "b": 3})

    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_sum_rejects_invalid_input() -> None:
    response = client.get("/api/v1/sum", params={"a": "invalid", "b": 3})

    assert response.status_code == 422

