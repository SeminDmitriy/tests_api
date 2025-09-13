import pytest
from pages.base_create_object import CreateObject
from pages.base_get_object import GetObject
from pages.base_put_object import PutObject
from pages.base_delete_object import DeleteObject
from tests.test_data import payloads


def test_get_object(obj_id):
    get_object = GetObject()
    get_object.get_obj(obj_id)
    get_object.status_code_is_200()

@pytest.mark.parametrize('payload', payloads.payload)
def test_post_object(payload):
    create_object = CreateObject()
    create_object.new_object(payload=payload)
    create_object.status_code_is_200()
    create_object.check_name('Apple MacBook Pro 16')
    create_object.check_year(2019)


@pytest.mark.parametrize('payload', payloads.payload_put)
def test_put_object(obj_id, payload):
    put_object = PutObject()
    put_object.put_obj(obj_id, payload_put=payload)
    put_object.status_code_is_200()
    put_object.check_name('Apple MacBook Pro 17')
    put_object.check_year(2021)


def test_delete_object(obj_id):
    delete_object = DeleteObject()
    get_object = GetObject()
    delete_object.delete_obj(obj_id)
    delete_object.status_code_is_200()
    delete_object.response_json['message'] == f'Object with id = {obj_id} has been deleted.'
    get_object.get_obj(obj_id)
    get_object.status_code_is_404()