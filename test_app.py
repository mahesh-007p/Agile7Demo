from app import app

def test_home_page():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Bill Calculation Implementation." in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_calculate_bill():
    client = app.test_client()
    response = client.post("/calculate", json={"price": 10.5, "quantity": 3})
    assert response.status_code == 200
    assert response.json["total"] == 31.5
