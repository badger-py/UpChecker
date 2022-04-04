from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)

categoriy_id: int = 0

@pytest.mark.run(order=5)
def test_get_all_categories():
    response = client.get("/api/categories/?website_id=1")
    assert response.status_code == 200
    assert type(response.json()) is list

@pytest.mark.run(order=6)
def test_create_category():
    global categoriy_id
    response = client.post("/api/categories/",
                           json={
                               "name": "Gmail of google.com",
                               "url": "http://mail.google.com/",
                               "contact": "123456789",
                               "check_type_id": 1,
                               "check_required_value": "200",
                               "website_id": 1,
                               "message_type_id": 1
                           }
                           )
    assert response.status_code == 201
    assert type(response.json()) is dict

    categoriy_id = response.json()["id"]

@pytest.mark.run(order=7)
def test_get_category():
    global categoriy_id
    response = client.get(f"/api/categories/{categoriy_id}")
    assert response.status_code == 200
    assert type(response.json()) is dict

@pytest.mark.run(order=8)
def test_update_categoriy():
    global categoriy_id
    response = client.put(
        f"/api/categories/{categoriy_id}",
        json={
            "url": "https://mail.google.com/"
        }
    )
    assert response.status_code == 200
    assert response.json()["url"] == "https://mail.google.com/"

@pytest.mark.run(order=9)
def test_delete_categoriy():
    global categoriy_id
    response = client.delete(
        f"/api/categories/{categoriy_id}"
    )
    assert response.status_code == 200
