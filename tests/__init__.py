"""
Tests Package Initialization

This __init__.py file makes the 'tests' directory a Python package.

Purpose:
- Allows pytest to properly discover and import test modules
- Enables sharing fixtures across multiple test files
- Provides a place for test configuration

Pytest Discovery:
- pytest automatically finds test_*.py or *_test.py files
- Test functions must start with 'test_'
- Test classes must start with 'Test'

Shared Fixtures Example:
If you have fixtures used across multiple test files, define them here:

    import pytest
    from fastapi.testclient import TestClient
    from app.main import app

    @pytest.fixture(scope="module")
    def client():
        '''Shared test client available to all tests.'''
        return TestClient(app)

Then use in any test file:

    def test_something(client):  # Fixture auto-injected
        response = client.get("/")
        assert response.status_code == 200

This file can remain empty for simple projects.
"""

# This file is intentionally left empty
# It exists to make 'tests' a Python package for pytest

# Conftest.py Alternative:
# For shared test fixtures, pytest convention is to use conftest.py
# instead of __init__.py. conftest.py is automatically discovered by pytest.

