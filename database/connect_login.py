import pymysql

class MysqlOp(object):
    def __init__(self):
        self.get_connect()
    def get_connect(self):
        try:
            self.conn = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "Tsinghua2024",
                db = "userinfo"
            )
        except pymysql.Error as e:
            print(f'Error{e}')
    def get_userinfo(self):
        sql = 'select * from user_pwd'
        cursor = self.conn.cursor()
        cursor.execute(sql)
        res = cursor.fetchall() # 获取全部数据
        dic = dict()
        for k in res:
            dic[k[0]] = k[1]
        cursor.close()
        return res
