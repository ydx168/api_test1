import pymysql


class TestMysql:
    def __init__(self):
        self.conn = pymysql.connect(host="localhost",
                                    user='root',
                                    password='111111',
                                    database='test1',
                                    charset='utf8')

        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def check(self, sql):
        try:
            self.cur.execute(sql)
            return self.cur.fetchall()
        except Exception as e:
            self.conn.rollback()
            print('查询错误')

    def change(self, sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print('修改，添加错误')


# aa = TestMysql()
# print(aa.check('select * from sc'))
