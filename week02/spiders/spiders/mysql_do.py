import pymysql

def insert_movie(name, time, category):
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        db="scrapydb",
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
    )
    try:
        with conn:
            sql = "insert into `movies` (`title`, `category`, `date`) values (%s, %s, %s)"
            cur = conn.cursor()
            cur.execute(sql, (name, category, time))
            conn.commit()
    except Exception as e:
        print(e)
        conn.rollback()
    conn.close()
#         # 关闭数据库连接
#         conn.close()
# dbInfo = {
#     'host' : 'localhost',
#     'port' : 3306,
#     'user' : 'root',
#     'password' : 'root',
#     'db' : 'scrapydb'
# }

# class ConnDB(object):
#     def __init__(self, dbInfo):
#         self.host = dbInfo['host']
#         self.port = dbInfo['port']
#         self.user = dbInfo['user']
#         self.password = dbInfo['password']
#         self.db = dbInfo['db']

#     def insert_ip(self, ip):
#         conn = pymysql.connect(
#             host = self.host,
#             port = self.port,
#             user = self.user,
#             password = self.password,
#             db = self.db
#         )

#         cusor = conn.cursor()
#         try:
#             cusor.execute('insert into ip values(null, "%s")' % ip)
#             # 关闭游标
#             cusor.close()
#             conn.commit()
#         except Exception as e:
#             print(e)
#             conn.rollback()
#         # 关闭数据库连接
#         conn.close()