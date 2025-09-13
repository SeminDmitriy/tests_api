from pages.base_object import BaseObject
import requests


class DeleteObject(BaseObject):
    def delete_obj(self, obj_id):
        self.response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
        self.response_json = self.response.json()