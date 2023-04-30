from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_ping():
    """
    疎通確認のテスト
    """
    response = client.get("/ping")
    assert response.status_code == 200
