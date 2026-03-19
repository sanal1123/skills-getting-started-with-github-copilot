from copy import deepcopy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module

_INITIAL_ACTIVITIES = deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Reset global in-memory activities before and after each test."""
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_INITIAL_ACTIVITIES))
    yield
    app_module.activities.clear()
    app_module.activities.update(deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    """Provide a test client for the FastAPI app."""
    with TestClient(app_module.app) as test_client:
        yield test_client
