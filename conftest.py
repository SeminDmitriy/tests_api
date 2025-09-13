import pytest
import requests
from pages.base_create_object import CreateObject
from tests.test_data import payloads

@pytest.fixture(params=payloads.payload)
def obj_id(request):
    payload = request.param
    create_object = CreateObject()
    create_object.new_object(payload=payload)
    yield create_object.response_json['id']
    requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')