import os
import sqlite3
HOME_DIR = os.path.abspath(os.path.dirname(__file__))

import config

class DB:
    def __init__(self):
        self.dbPath = os.path.join(HOME_DIR, config.dbPath)

    def getDB(self):
        return sqlite3.connect(self.dbPath)

    def execute(self, *sqls):
        db = self.getDB()
        for sql in sqls:
            db.execute(sql)
            db.commit()
        db.close()

    def queryOne(self, sql):
        db = self.getDB()
        record = db.execute(sql).fetchone()
        db.close()
        return record

    def queryAll(self, sql):
        db = self.getDB()
        record = db.execute(sql).fetchall()
        db.close()
        return record

    def queryToken(self):
        sql = "select token from token limit 1"
        token = self.queryOne(sql)[0]
        return token

if __name__=="__main__":
    db = DB()
    print(db.queryToken())