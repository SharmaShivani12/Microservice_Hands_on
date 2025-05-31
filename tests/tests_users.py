from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    response = client.post("/users", json={"id": 1, "name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 200
    assert response.json()["name"] == "Alice"

def test_get_user():
    client.post("/users", json={"id": 2, "name": "Bob", "email": "bob@example.com"})
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json()["email"] == "bob@example.com"

def test_delete_user():
    client.post("/users", json={"id": 3, "name": "Charlie", "email": "charlie@example.com"})
    response = client.delete("/users/3")
    assert response.status_code == 200
