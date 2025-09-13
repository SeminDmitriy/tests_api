class BaseObject:
    response = None
    response_json = None

    def status_code_is_200(self):
        assert self.response.status_code == 200

    def status_code_is_404(self):
        assert self.response.status_code == 404

    def check_name(self, name):
        assert self.response.json()['name'] == name

    def check_year(self, year):
        assert self.response.json()['data']['year'] == year