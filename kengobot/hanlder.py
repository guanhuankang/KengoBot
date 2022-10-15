import xmltodict
from response import Response

class Hanlder:
    def __init__(self, request):
        data = xmltodict.parse(request.get_data())["xml"]
        self.userName = data["FromUserName"]
        self.hostName = data["ToUserName"]
        self.createTime = data["CreateTime"]
        self.msgId = data["MsgId"]
        self.msgType = data["MsgType"]
        self.content = data["Content"]

        self.response = Response(self)

    def getSimpleResponse(self):
        return self.response.textMsg(text=self.content)