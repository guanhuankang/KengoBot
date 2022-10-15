import time

class Response:
    def __init__(self, reqData):
        self.reqData = reqData

    def textMsg(self, text):
        return """<xml>
    <ToUserName><![CDATA[{userName}]]></ToUserName>
    <FromUserName><![CDATA[{hostName}]]></FromUserName>
    <CreateTime>{createTime}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{text}]]></Content>
</xml>""".format(userName=self.reqData.userName,
                  hostName=self.reqData.hostName,
                  createTime=self.reqData.createTime,
                  text = text)

    def ImageMsg(self):
        pass