import time
from api import API
from db import DB

def update():
    db = DB()
    api = API(db)

    appid, appsecret = db.queryOne("select appid, appsecret from token limit 1")
    token, expire_in = api.getToken(appid, appsecret)
    print(token, expire_in)
    if isinstance(token, type(None)): return 10

    db.execute("UPDATE token set token='{token}', expire='{expire}'".format(
        token = token,
        expire = time.time() + expire_in
    ))
    return expire_in

if __name__=="__main__":
    while True:
        expire_in = update()
        print("update token at {}, expire in {} sec".format(time.time(), expire_in))
        time.sleep(expire_in // 2)
