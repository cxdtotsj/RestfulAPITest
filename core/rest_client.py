import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import json as json_parse
import resources.settings


class RestClient:
    """初始化session，并鉴权
    """
    def __init__(self, base_url=None, **kwargs):
        if base_url:
            self.base_url = base_url
        else:
            self.base_url = resources.setting.base_url
            if not self.base_url:
                raise RuntimeError("no url been set.")
        self.session = self.__session(**kwargs)
    
    def __session(self, username=None, password=None, 
            token=None, email=None, mobile=None):
        """session鉴权的三种方式
        """
        # 1. 输入 username, password
        # 2. 输入固定的token
        # 3. 通过 /user/login 接口，获取动态token
        session = requests.session()
        if username and password:
            session.auth = (username, password)
        elif token:
            token = token
        else:
            token = self.__login("/user/login", password, email, mobile)
        session.headers.update({
            "Authorization": token,
            "id-prefix": "ci"
        })
        return session
    
    def __login(self, url, password, email=None, mobile=None):
        """获取动态token
        """
        url = self.__get_url(url)
        data = {
            "email": email,
            "mobile": mobile,
            "password": password
        }
        try:
            res = requests.post(url, data)
            res.raise_for_status()
            return res.json()["token"]
        except:
            print(res.text)
            print("用户登录失败")
    
    def __get_url(self, url_params):
        """拼接URL
        """
        url = "{}{}?debug=1".format(self.base_url, url_params)
        return url
    
    def get(self, url, **kwargs):
        return self.request(url, "get", **kwargs)
    
    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "post", data, json, **kwargs)
    
    def options(self, url, **kwargs):
        return self.request(url, "options", **kwargs)
    
    def head(self, url, **kwargs):
        return self.request(url, "head", **kwargs)
    
    def put(self, url, data=None, **kwargs):
        return self.request(url, "put", data, **kwargs)
    
    def patch(self, url, data=None, json=None, **kwargs): 
        return self.request(url, "patch", data, json, **kwargs)
    
    def delete(self, url, **kwargs):
        return self.request(url, "delete", **kwargs)

    def errInfo(self,res):
        """
        res: http的response对象
        request_id: response对象中的request_id
        """
        if isinstance(res,object):
            try:
                return "\033[31m {} \033[0m".format({"err":res.text,"request_id":res.headers["X-Request-Id"]})
            except KeyError:
                return "\033[31m {} \033[0m".format({"err":res.text, "request_id": "X-Request-Id 获取失败"})

    def assertInfo(self,message):
        """assert错误信息输出
        """
        return "\033[31m {} \033[0m".format(message)
    
    def request(self, url, method_name, data=None, json=None, **kwargs):
        url = self.__get_url(url)
        if method_name == 'get':
            res = self.session.get(url, **kwargs)
        if method_name == 'post':
            res = self.session.post(url, data, json, **kwargs)
        if method_name == 'options':
            res = self.session.options(url, **kwargs)
        if method_name == 'head':
            res = self.session.head(url, **kwargs)
        if method_name == 'put':
            res = self.session.put(url, data, **kwargs)
        if method_name == 'patch':
            if json:
                data = json_parse.dumps(json)
            res = self.session.patch(url, data, **kwargs)
        if method_name == 'delete':
            res = self.session.delete(url, **kwargs)
        return res