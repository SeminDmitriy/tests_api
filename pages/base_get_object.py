from pages.base_object import BaseObject
import requests

class GetObject(BaseObject):

    def get_obj(self,obj_id):
        self.response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')