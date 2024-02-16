"""This file contains fixtures for testing the API."""

import pytest

from app import app


@pytest.fixture
def test_app():
    """Returns a test version of the API."""
    return app.test_client()
