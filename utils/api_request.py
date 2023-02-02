import requests


class APIRequest:

    def get(self, url, headers=None):
        return requests.get(url=url, headers=headers)

    def post(self, url, payload, headers=None):
        return requests.post(url=url, data=payload, headers=headers)

    def delete(self, url, headers=None):
        return requests.delete(url=url, headers=headers)

    def put(self, url, payload, headers=None):
        return requests.post(url=url, data=payload, headers=headers)
