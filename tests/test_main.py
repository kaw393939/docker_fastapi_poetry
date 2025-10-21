"""
Test Suite for FastAPI Application

This module contains all test cases for our API endpoints using pytest.

Testing Concepts:
- Unit Tests: Test individual functions/endpoints in isolation
- Integration Tests: Test how components work together
- TestClient: FastAPI's built-in test client (doesn't require running server)
- Assertions: Verify that code behaves as expected

Test Organization:
- Each test function should test ONE specific behavior
- Test names should clearly describe what they test
- Use AAA pattern: Arrange, Act, Assert
"""

# Import TestClient - FastAPI's testing utility
# This allows us to test our API without running an actual server
from fastapi.testclient import TestClient

# Import our FastAPI application instance
from app.main import app

# Create a test client instance
# This client simulates HTTP requests to our API
# It's much faster than running a real server and making HTTP requests
client = TestClient(app)


def test_read_root():
    """
    Test the root endpoint (GET /).

    This test verifies that:
    1. The endpoint responds with HTTP 200 (OK)
    2. The response contains the expected JSON message

    Testing Pattern (AAA):
    - Arrange: Set up test client (done globally above)
    - Act: Make GET request to root endpoint
    - Assert: Verify status code and response data
    """
    # Act: Make a GET request to the root endpoint
    # This simulates: curl http://localhost:8001/
    response = client.get("/")

    # Assert: Verify the HTTP status code is 200 (OK)
    # Status codes: 200=Success, 404=Not Found, 500=Server Error, etc.
    assert response.status_code == 200

    # Assert: Verify the JSON response matches expected structure
    # .json() parses the response body as JSON
    assert response.json() == {"message": "Hello World"}


def test_health_check():
    """
    Test the health check endpoint (GET /health).

    Health checks are critical for:
    - Kubernetes liveness/readiness probes
    - Load balancer health monitoring
    - Alerting systems
    - Service mesh routing decisions

    This test ensures the health endpoint always returns a healthy status.
    """
    # Act: Make a GET request to the health endpoint
    response = client.get("/health")

    # Assert: Verify successful response
    assert response.status_code == 200

    # Assert: Verify health status is "healthy"
    assert response.json() == {"status": "healthy"}


# Additional Test Examples (Commented Out)
# Uncomment and modify these as you add more endpoints

# def test_endpoint_with_path_parameter():
#     """Test endpoint that accepts path parameters."""
#     response = client.get("/items/5")
#     assert response.status_code == 200
#     assert response.json()["item_id"] == 5

# def test_endpoint_with_query_parameter():
#     """Test endpoint that accepts query parameters."""
#     response = client.get("/search?q=fastapi")
#     assert response.status_code == 200
#     assert response.json()["query"] == "fastapi"

# def test_post_endpoint():
#     """Test POST endpoint with request body."""
#     test_data = {"name": "Test Item", "price": 9.99}
#     response = client.post("/items", json=test_data)
#     assert response.status_code == 200
#     assert response.json()["created"] == True

# def test_endpoint_returns_404():
#     """Test that non-existent endpoints return 404."""
#     response = client.get("/nonexistent")
#     assert response.status_code == 404

# def test_endpoint_validation_error():
#     """Test that invalid data returns 422 (Validation Error)."""
#     invalid_data = {"name": "Item"}  # Missing required 'price' field
#     response = client.post("/items", json=invalid_data)
#     assert response.status_code == 422  # Unprocessable Entity


# Advanced Testing Patterns

# import pytest
#
# @pytest.fixture
# def sample_data():
#     """
#     Fixture provides reusable test data.
#     Automatically passed to tests that request it.
#     """
#     return {"name": "Test", "value": 123}
#
# def test_with_fixture(sample_data):
#     """Test using fixture data."""
#     assert sample_data["name"] == "Test"

# @pytest.mark.parametrize("input,expected", [
#     (1, 2),
#     (2, 3),
#     (5, 6),
# ])
# def test_parametrized(input, expected):
#     """
#     Parametrized test runs multiple times with different inputs.
#     Great for testing multiple scenarios efficiently.
#     """
#     assert input + 1 == expected

# @pytest.mark.asyncio
# async def test_async_endpoint():
#     """
#     Test asynchronous endpoints.
#     Requires: poetry add --group dev pytest-asyncio
#     """
#     async with AsyncClient(app=app, base_url="http://test") as ac:
#         response = await ac.get("/")
#     assert response.status_code == 200

