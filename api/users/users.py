from core.rest_client import RestClient

class Users(RestClient):
    def __init__(self, **kwargs):
        super(Users, self).__init__(**kwargs)

    def user_login(self, **kwargs):
        return self.post("/user/login", **kwargs)
    
    def create_user(self, **kwargs):
        return self.post("/user/create", **kwargs)
    
    def reset_user_passwd(self, **kwargs):
        return self.post("/user/passwd/reset", **kwargs)


# if __name__ == '__main__':
#     u = Users("")