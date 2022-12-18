import pymysql

class MysqlOp(object):
    def __init__(self):
        self.get_connect()
        self.cursor = ""
    def get_connect(self):
        try:
            self.conn = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "Tsinghua2024",
                db = 'userinfo'
            )
            print('userinfo 连接成功')
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

    def get_connect_employ(self):
        try:
            self.conn_employ = pymysql.connect(
                host = "localhost",
                user = "root",
                password = "Tsinghua2024",
                db = 'employ'
            )
            print('employ 连接成功')
        except pymysql.Error as e:
            print(f'Error{e}')