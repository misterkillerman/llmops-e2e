import requests
import time

BASE_URL = "http://localhost:30080"  # mapped port from k3d

def test_service_health():
    """Test whether the service returns a 200 OK."""
    time.sleep(3)  # wait for pods to start
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200
