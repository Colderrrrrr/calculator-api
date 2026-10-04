from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def calc(a, b, operation):
    return client.post("/calculate", json={"a": a, "b": b, "operation": operation})


def test_health():
    response = client.get("/health")
    assert response.status_code == 200


def test_sum():
    assert calc(2, 3, "+").json()["result"] == 5


def test_subtraction():
    assert calc(5, 3, "-").json()["result"] == 2


def test_multiplication():
    assert calc(4, 2.5, "*").json()["result"] == 10


def test_division():
    assert calc(7, 2, "/").json()["result"] == 3.5


def test_power():
    assert calc(2, 3, "**").json()["result"] == 8


def test_division_by_zero():
    assert calc(1, 0, "/").status_code == 400


def test_unsupported_operation():
    assert calc(1, 2, "%").status_code == 400


# проверки на граничные значения

def test_zero_to_negative_power():
    assert calc(0, -1, "**").status_code == 400


def test_negative_base_fractional_power():
    assert calc(-8, 0.5, "**").status_code == 400


def test_power_overflow():
    assert calc(1e308, 2, "**").status_code == 400


def test_multiplication_overflow():
    assert calc(1e300, 1e300, "*").status_code == 400


def test_infinity_input():
    response = client.post(
        "/calculate",
        content=b'{"a": 1e400, "b": 1, "operation": "+"}',
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 422
