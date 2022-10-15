import requests
import json

class API:
    def __init__(self):
        pass

    def Get(self, url, params):
        return requests.get(url=url, params=params)

    def Post(self, url, params, data):
        return requests.post(url=url, params=params, data=data)

    def isSuccess(self, res):
        if "errcode" not in res:
            return True
        print(res)
        return False

    def getToken(self, appid, appsecret):
        url = "https://api.weixin.qq.com/cgi-bin/token"
        params = {
            "grant_type": "client_credential",
            "appid": appid,
            "secret": appsecret
        }
        res = self.Get(url, params).json()
        if self.isSuccess(res):
            return res["access_token"], res["expires_in"]
        return None, None
