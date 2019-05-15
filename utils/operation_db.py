import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pymysql
from resources.settings import CASE_DATABASE


class OperationDB:
    def __init__(self, db_name=None, *args, **kwargs):
        if db_name is None:
            self.db_info = CASE_DATABASE.get("dev")
        else: 
            self.db_info = CASE_DATABASE.get(db_name)
        self.mycursor = self._get_db()

    def _get_db(self):
        db_session = pymysql.connect(host=self.db_info.get("HOST"),
                             port=int(self.db_info.get("PORT")),
                             db=self.db_info.get("NAME"),
                             user=self.db_info.get("USER"),
                             password=self.db_info.get("PASSWORD"),
                             charset=self.db_info.get("CHARSET"),
                             autocommit=True,
                             cursorclass=pymysql.cursors.DictCursor)
        mycursor = db_session.cursor()
        return mycursor

    def get_fetchall(self, sql, paramers=None):
        """返回全部查询结果"""
        self.mycursor.execute(sql)
        row_all = self.mycursor.fetchall()
        return row_all

    def get_effect_row(self, sql):
        """
        获取查询结果的行数
        """
        effect_row = self.mycursor.execute(sql)
        self.close_db()
        return effect_row

    def get_fetchone(self, sql):
        """
        获取第一个返回结果
        返回查询结果的json
        """
        self.mycursor.execute(sql)
        row_one = self.mycursor.fetchone()
        self.close_db()
        return row_one

    def get_fetchmany(self, sql, n, paramers=None):
        """返回指定查询行数的结果"""
        if paramers is None:
            self.mycursor.execute(sql)
        else:
            self.mycursor.execute(sql % paramers)
        row_num = self.mycursor.fetchmany(n)
        self.close_db()
        return row_num

    def update_data(self, sql):
        """更新数据库"""
        try:
            self.mycursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("更新数据失败", e)
        self.close_db()

    def insert_data(self, sql):
        """插入数据，并返回自增id"""
        try:
            self.mycursor.execute(sql)
            self.db.commit()
            last_id = self.mycursor.lastrowid
            return last_id
        except Exception as e:
            self.db.rollback()
            print("插入数据失败", e)
        self.close_db()

    def delete_data(self, sql):
        """删除数据"""
        try:
            self.mycursor.execute(sql)
            self.db.commit()
        except Exception as e:
            self.db.rollback()
            print("删除数据失败", e)
        self.close_db()

    def close_db(self):
        """关闭数据库连接"""
        self.mycursor.close()


if __name__ == '__main__':
    dbdata = OperationDB("testcase")
    sql = '''SELECT * FROM `auth_group_permissions` where id = 1;'''
    a = dbdata.get_fetchone(sql)
    print(a)