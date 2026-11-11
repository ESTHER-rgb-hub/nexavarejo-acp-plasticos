from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "online"

def test_login_sucesso():
    payload = {"email": "operador.fabbri@acpplasticos.com.br", "senha": "12345678"}
    response = client.post("/login", json=payload)
    assert response.status_code == 200
    assert "access_token" in response.json()