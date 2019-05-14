import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import core.setting
from api.users.users import Users
from api.corp.corp import Corp


class InitData:
    def __init__(self, **kwargs):
        self.user = Users(**kwargs)
        self.corp = Corp(**kwargs)

    # 创建用户
    def create_user(self,name,password,email=None,mobile=None):
        data = {
            "email": email,
            "mobile": mobile,
            "name": name,
            "password": password
        }
        try:
            res = self.user.create_user(data=data)
            res.raise_for_status()
            print("用户: {} 创建成功!".format(name))
            return res.json()["id"]
        except:
            print("重置密码失败")
            print(self.user.errInfo(res))

    # 修改密码
    def user_passed_reset(self,password,newpasswd,email=None,mobile=None):
        data = {
            "email": email,
            "mobile": mobile,
            "password": password,
            "newpasswd": newpasswd
        }
        try:
            res = self.user.reset_user_passwd(data=data)
            res.raise_for_status()
        except:
            print("重置密码失败")
            print(self.user.errInfo(res))

    # 创建组织
    def corp_create(self,name):
        data = {
            "name": name
        }
        # sql = '''select name from corp where name = '{}';'''.format(name)
        # corp_name = self.opera_db.get_fetchone(sql)
        # if corp_name is None:
        try:
            res = self.corp.create_corp(data=data)
            res.raise_for_status()
            print("-------------------------------")
            print("组织: {} 创建成功!".format(name))
            return res.json()["id"]
        except:
            print("新增组织失败")
            print(self.corp.errInfo(res))

    # 用户添加到组织
    def user_corp_add(self,user_id,corp_id,role):
        data = {
            "user_id": user_id,
            "corp_id": corp_id,
            "role": role
        }
        try:
            res = self.corp.add_corp_user(data=data)
            res.raise_for_status()
            print("用户添加至组织成功")
        except:
            print("用户添加至组织失败")
            print(self.corp.errInfo(res))


if __name__ == '__main__':
    init = InitData(email="admin@admin", password="abc123")

    # 创建组织
    corp = "测试组织010-3"
    corp_id = init.corp_create(corp)
    # 新增users
    data = [
        ("test001-3@test.com", "测试001-3", "123456", "12345678", 524288),
        ("test002-3@test.com", "测试002-3", "123456", "12345678", 0)
    ]
    for i in data:
        email = i[0]
        user_name = i[1]
        password = i[2]
        newpasswd = i[3]
        role = i[4]
        user_id = init.create_user(name=user_name, password=password, email= email)
        init.user_passed_reset(password=password,newpasswd=newpasswd,email=email)
        init.user_corp_add(user_id=user_id, corp_id=corp_id,role=role)

    other_corp = "测试组织011-3"
    other_corp_id = init.corp_create(other_corp)
    other_user_id = init.create_user(name="测试003-3", password="123456", email= "test003-3@test.com")
    init.user_passed_reset(password="123456",newpasswd="12345678",email="test003-3@test.com")
    init.user_corp_add(user_id=other_user_id, corp_id=other_corp_id,role=524288)