import requests 


class internal_api:
    def __init__(self, url):
        self.url = url
    
    def get(self, endpoint):
        return requests.get(self.url + endpoint).json()
    
    def post(self, endpoint, data):
        return requests.post(self.url + endpoint, data).json()
    
    def put(self, endpoint, data):
        return requests.put(self.url + endpoint, data).json()
    
    def delete(self, endpoint):
        return requests.delete(self.url + endpoint).json()