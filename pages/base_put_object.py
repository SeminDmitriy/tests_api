from pages.base_object import BaseObject
import requests

class PutObject(BaseObject):
    def put_obj(self, obj_id, payload_put):
        self.response = requests.put(f'https://api.restful-api.dev/objects/{obj_id}',json=payload_put)
        self.response_json = self.response.json()