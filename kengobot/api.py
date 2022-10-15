import io
from PIL import Image
import requests
import logging, json

class API:
    def __init__(self, db):
        self.db = db

    def Get(self, url, params):
        return requests.get(url=url, params=params)

    def Post(self, url, params, **kwargs):
        return requests.post(url=url, params=params, **kwargs)

    def logDown(self, res):
        logging.info("code: {}, msg:{}".format(res.status_code, res.text if len(res.text)<1000 else res.text[0:50] ))

    def getToken(self, appid, appsecret):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": appid,
            "secret": appsecret
        }
        res = self.Get(url, params)
        self.logDown(res)
        res = res.json()
        return res["access_token"], res["expires_in"]

    def downloadMedia(self, mediaId):
        url = "https://api.weixin.qq.com/cgi-bin/media/get"
        params = {
            "access_token": self.db.queryToken(),
            "media_id": mediaId
        }
        res = self.Get(url, params)
        self.logDown(res)
        return res.content

    def downloadImage(self, mediaId):
        return Image.open(io.BytesIO(self.downloadMedia(mediaId)))

    def uploadMedia(self, filepath, mediaType):
        url = "https://api.weixin.qq.com/cgi-bin/media/upload"
        params = {
            "access_token": self.db.queryToken(),
            "type": mediaType
        }
        logging.info("uploading media...")
        res = self.Post(url, params, files={"media": open(filepath, "rb")})
        self.logDown(res)
        res = json.loads(res.text)
        return res["media_id"]

    def uploadImage(self, filepath):
        return self.uploadMedia(filepath,"image")

if __name__=="__main__":
    from db import DB
    import time
    api = API(DB())
    img = api.downloadImage("BY71Chc36zgy9f9HyhuVZjPb3cZVDIQaW6Mh_Tj7ZRBDvUwbDbq6e3eW3ivZH_M_")

    filepath = "static/{}.jpg".format(time.time())
    img.save(filepath)
    print(api.uploadImage(filepath))