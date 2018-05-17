import pymysql


class Pipeline_mysql(object):
    def __init__(self, host, port, db, user, password):
        self.host = host
        self.port = port
        self.db_name = db
        self.user = user
        self.password = password
        self.table = "image"

    @classmethod
    def from_crawler(cls, crawler):
        return cls(host=crawler.settings.get('MYSQL_HOST'),
                   port=crawler.settings.get('MYSQL_PORT'),
                   db=crawler.settings.get('MYSQL_DB'),
                   user=crawler.settings.get('MYSQL_USER'),
                   password=crawler.settings.get("MYSQL_PASSWORD"))

    def open_spider(self, spider):
        print("开启mysql数据库")
        self.DB = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.db_name,
                                  charset="utf8", port=self.port)
        self.cursor = self.DB.cursor()  # mysql都是通过游标来执行sql

    def process_item(self, item, spider):
        # 构造sql的插入语句,比较恶心
        data = dict(item)
        keys = ",".join(data.keys())
        values = ",".join(["'{}'"] * len(data)).format(*data.values())
        insert_sql = "insert into {}({}) values({})".format("image", keys, values)
        # print(insert_sql) #测试sql
        # 提交执行
        self.cursor.execute(insert_sql)
        self.DB.commit()
        return item

    def close_spider(self, spider):
        print("关闭mysql数据库")
        self.DB.close()
