import json

from app.routers.cars import create


def test_create_note(test_app, monkeypatch):
    test_request_payload = {
        "car_number": "A124BC",
        "is_rented": False,
        "model": "Toyota Camry",
        "car_type": "Sedan",
        "fuel_type": "Petrol",
        "car_rating": 4.5,
        "year_to_start": 2020,
        "year_to_work": 2025,
        "rides": 150
    }

    test_response_payload = {"message": "Car added successfully", "car_id": 1}

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(create, "add_car", mock_post)

    response = test_app.post("/cars/add", content=json.dumps(test_request_payload),)
    print(response.text)

    assert response.status_code == 200
    assert response.json() == test_response_payload