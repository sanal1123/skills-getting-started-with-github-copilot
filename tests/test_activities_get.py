def test_get_activities_returns_seeded_data(client):
    # Arrange
    expected_activity_count = 9

    # Act
    response = client.get("/activities")
    activities = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(activities, dict)
    assert len(activities) == expected_activity_count
    assert "Chess Club" in activities


def test_get_activities_returns_expected_schema(client):
    # Arrange
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    chess_activity = response.json()["Chess Club"]

    # Assert
    assert response.status_code == 200
    assert set(chess_activity.keys()) == expected_fields
    assert isinstance(chess_activity["participants"], list)
    assert isinstance(chess_activity["max_participants"], int)
