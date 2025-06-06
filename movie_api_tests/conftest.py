import os
import pytest
from dotenv import load_dotenv
from api.api_client import TMDB_client

load_dotenv()

@pytest.fixture(scope='session')
def api_key():
    return os.getenv('KEY_TO_API_ACCESS')

@pytest.fixture(scope='session')
def base_url():
    return os.getenv('BASE_URL')

@pytest.fixture(scope='session')
def tmdb_client(base_url, api_key):
    return TMDB_client(base_url=base_url, api_key=api_key)
