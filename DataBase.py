import pymysql

class DataBase:
    def __init__(self):
        self.db_login = None
        self.cursor_login = None

    def connect_logindb(self): # 与登录数据库连接
        try:
            self.db_login = pymysql.connect(
                host = 'localhost',
                user= 'root',
                password = 'Tsinghua2024',
                database = 'userinfo'
            )
            self.cursor_login = self.db_login.cursor()
            print('正确连接')
            return True
        except:
            print('错误连接')
            return False

    def is_in_logindb(self, username, password): # 检查当前用户是否在数据库中
        sql = f"select * from user_pwd where username = '{username}' and password = '{password}'"
        print(f'sql为{sql}')
        try:
            self.db_login.ping(reconnect = True) # 重新测试连接
            self.cursor_login.execute(sql)
            info = self.cursor_login.fetchall()
            if(info):
                print(f'存在用户{username}')
                return True
            else:
                return False
        except:
            print('出现错误')
            self.db_login.rollback()

# if __name__ == '__main__':
#     db = DataBase()
#     db.connect_logindb()
#     db.is_in_logindb('林林林', 'Tsinghua2024')
