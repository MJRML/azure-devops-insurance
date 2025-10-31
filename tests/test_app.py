from fastapi.testclient import TestClient
from src.deployment.app_fastapi import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()
