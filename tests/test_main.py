import pytest
from fastapi.testclient import TestClient 
from unittest.mock import patch
from app.main import app

client = TestClient(app)

@pytest.fixture
def mock_get_latest_price():
    with patch("app.services.get_latest_price") as mock:
        mock.side_effect = lambda db, contract_month: (350.00,) if contract_month == "Z24" else None
        yield mock

def test_calculate_flat_price_contract_not_found(mock_get_latest_price):
    response = client.post("/api/flat_price", json={
        "basis": 10,
        "contract_months": ["INVALID"]
    })
    assert response.status_code == 404
    assert response.json() == {"detail": "Contract month INVALID not found"}

def test_calculate_flat_price_basis_out_of_range():
    response = client.post("/api/flat_price", json={
        "basis": 100,
        "contract_months": ["Z24"]
    })
    
    assert response.status_code == 422
    assert "Basis must be a number between -50 and 50" in str(response.json())
