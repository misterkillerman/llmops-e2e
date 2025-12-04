import requests
import time

BASE_URL = "http://localhost:30080"  # mapped port from k3d

def test_chat():
    """Test whether the service returns a 200 OK."""
    time.sleep(3)  # wait for pods to start
    payload = {"question": "What is AI?", "context": "AI is artificial intelligence."}
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    print(response)
    assert response.status_code == 200
