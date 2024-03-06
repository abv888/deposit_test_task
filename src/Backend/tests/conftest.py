import pytest
from fastapi.testclient import TestClient
from src.Backend.app.settings import settings
from src.Backend.app.app import app

# defult settings
settings.deposits_settings.min_amount = 10000
settings.deposits_settings.max_amount = 1000000
settings.deposits_settings.min_period = 1
settings.deposits_settings.max_period = 60
settings.deposits_settings.min_rate = 1
settings.deposits_settings.max_rate = 8

client = TestClient(app)