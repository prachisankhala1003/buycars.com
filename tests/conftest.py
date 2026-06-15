"""
Pytest configuration and shared fixtures for tests
"""
import pytest


@pytest.fixture
def sample_vehicle_data():
    """Sample vehicle data for testing predictor"""
    return {
        "year": 2015,
        "make": "Honda",
        "model": "Civic",
        "mileage": 85000,
        "condition": "good",
        "transmission": "automatic",
    }


@pytest.fixture
def sample_appraisal_data():
    """Sample appraisal data for testing agents"""
    return {
        "vehicle_id": "VH001",
        "predicted_value": 12500,
        "market_range_low": 11800,
        "market_range_high": 13200,
        "days_on_lot": 18,
        "repair_issues": ["transmission_warning"],
    }
