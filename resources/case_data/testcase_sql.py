import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils.operation_db import OperationDB

class User:
    def __init__(self, *args, **kwargs):
        self.opera_db = OperationDB()
    
    def user(self, sql_id):
        sql = '''select * from user where id = '{}';'''.format(sql_id)
        data = self.opera_db.get_fetchone(sql)
        return data
    
if __name__ == '__main__':
    u = User()
    data = u.user("109777231298966563")
    # print(data)
    print({"email": data.get("email")})
