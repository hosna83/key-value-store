from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_set_and_get_key():
    # POST /set
    response = client.post("/set", json={"key": "name", "value": "Hosna"})
    assert response.status_code == 200
    assert response.json() == {"message": "Key name set successfully."}

    # GET /get/{key}
    response = client.get("/get/name")
    assert response.status_code == 200
    assert response.json() == {"key": "name", "value": "Hosna"}

def test_get_nonexistent_key():
    response = client.get("/get/nonexistent")
    assert response.status_code == 404

def test_empty_key_fails():
    response = client.post("/set", json={"key": "", "value": "something"})
    assert response.status_code == 422  # validation error

def test_overwrite_existing_key():
    client.post("/set", json={"key": "name", "value": "Hosna"})
    client.post("/set", json={"key": "name", "value": "Hana"})
    response = client.get("/get/name")
    assert response.json()["value"] == "Hana"
