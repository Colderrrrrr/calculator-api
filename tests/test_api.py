from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_sum():
    response = client.post("/calculate", json={"a": 2, "b": 3, "operation": "+"})
    assert response.json()["result"] == 5


def test_power():
    response = client.post("/calculate", json={"a": 2, "b": 3, "operation": "**"})
    assert response.json()["result"] == 8


def test_division_by_zero():
    response = client.post("/calculate", json={"a": 1, "b": 0, "operation": "/"})
    assert response.status_code == 400
