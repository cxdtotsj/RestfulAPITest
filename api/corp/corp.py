from core.rest_client import RestClient


class Corp(RestClient):
    def __init__(self, **kwargs):
        super(Corp, self).__init__(**kwargs)

    def create_corp(self, **kwargs):
        return self.post("/corp/create", **kwargs)

    def add_corp_user(self, **kwargs):
        return self.post("/corp/user/add", **kwargs)