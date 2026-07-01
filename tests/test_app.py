from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_duplicate_signup_returns_400():
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": "michael@mergington.edu"},
    )

    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"
