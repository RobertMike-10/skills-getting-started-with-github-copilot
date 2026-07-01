from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_duplicate_signup_returns_400():
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.post(
        "/activities/Chess%20Club/signup",
        params={"email": email},
    )

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student is already signed up"


def test_unregister_participant_removes_from_activity():
    # Arrange
    activity_name = "Chess Club"
    participant_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants/{participant_email}"
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {participant_email} from {activity_name}"

    activities_response = client.get("/activities")
    assert participant_email not in activities_response.json()[activity_name]["participants"]
