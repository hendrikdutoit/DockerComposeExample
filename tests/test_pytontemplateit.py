import subprocess
import time

import pytest
import requests


@pytest.fixture(scope="module", autouse=True)
def docker_compose_up_down():
    """Setup and teardown for Docker Compose."""
    # Start Docker Compose
    subprocess.run(["docker-compose", "up", "-d"], check=True)

    # Wait for the services to be ready
    time.sleep(10)  # Adjust time as needed based on your environment

    yield

    # Tear down Docker Compose
    subprocess.run(["docker-compose", "down"], check=True)


def test_app_response():
    """Test the application's response."""
    url = "http://localhost:8000/"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Hello from Docker!" in response.text
    assert "I have been seen" in response.text
