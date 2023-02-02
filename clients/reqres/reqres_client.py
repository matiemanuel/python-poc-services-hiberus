import json

from clients.base_client import BaseClient
from config import REQRES_BASE_URL
from utils.api_request import APIRequest


class ReqresClient(BaseClient):

    def __init__(self):
        super().__init__()
        self.service = APIRequest()
        self.base_url = REQRES_BASE_URL
        self.users_endpoint = self.base_url + '/users'

    def get_users(self, page_numer=1):
        return self.service.get(url=f'{self.users_endpoint}?page={page_numer}', headers=self.headers)

    def get_user(self, user_id):
        return self.service.get(url=f'{self.users_endpoint}/{user_id}', headers=self.headers)

    def create_user(self, name, job):
        return self.service.post(url=self.users_endpoint, payload=json.dumps({"name": name, "job": job}), headers=self.headers)
