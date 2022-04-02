from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

website_id: int = 0


def test_get_all_websites():
    response = client.get("/api/websites/")
    assert response.status_code == 200
    assert type(response.json()) is list


def test_get_website():
    response = client.get("/api/websites/1")
    assert response.status_code == 200
    assert type(response.json()) is dict


def test_create_website():
    global website_id
    response = client.post("/api/websites/",
                           json={
                               "name": "Example",
                               "url": "http://example.com/"
                           }
                           )
    assert response.status_code == 201
    assert type(response.json()) is dict

    website_id = response.json()["id"]


def test_update_website():
    global website_id
    response = client.put(
        f"/api/websites/{website_id}",
        json={
            "is_paused": True
        }
    )
    assert response.status_code == 200
    assert response.json()["is_paused"] == True


def test_delete_website():
    global website_id
    response = client.delete(
        f"/api/websites/{website_id}"
    )
    assert response.status_code == 200
