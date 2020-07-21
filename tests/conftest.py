import pytest

from app import app as flask_app


@pytest.fixture
def test_app():
    yield flask_app


@pytest.fixture
def client(test_app):
    return test_app.test_client()
