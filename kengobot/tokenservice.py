import sqlite3
from api import API
import time

def update():
    conn = sqlite3.connect("db/apptoken.sq3")
    appid, appsecret = conn.execute("select appid, appsecret from token limit 1").fetchone()
    token, expire_in = API().getToken(appid, appsecret)
    if isinstance(token, type(None)):
        conn.close()
        return 10
    conn.execute("UPDATE token set token='{token}', expire='{expire}'".format(
        token = token,
        expire = time.time() + expire_in
    ))
    conn.commit()
    conn.close()
    return expire_in

if __name__=="__main__":
    while True:
        expire_in = update()
        print("update token at {}, expire in {} sec".format(time.time(), expire_in))
        time.sleep(expire_in // 2)
