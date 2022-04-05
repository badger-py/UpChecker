from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)

website_id: int = 0


# TODO: pytest.fixture() LOOK CHAT
@pytest.mark.run(order=1)
def test_get_all_websites():
    response = client.get("/api/websites/")
    assert response.status_code == 200
    assert type(response.json()) is list


@pytest.mark.run(order=2)
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


@pytest.mark.run(order=3)
def test_get_website():
    global website_id
    response = client.get(f"/api/websites/{website_id}")
    assert response.status_code == 200
    assert type(response.json()) is dict


@pytest.mark.run(order=4)
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


@pytest.mark.run(order=10)
def test_delete_website():
    global website_id
    response = client.delete(
        f"/api/websites/{website_id}"
    )
    assert response.status_code == 200
