class Response:
    def __init__(self, data):
        self.data = data

    def textMsg(self, text):
        return """<xml>
    <ToUserName><![CDATA[{userName}]]></ToUserName>
    <FromUserName><![CDATA[{hostName}]]></FromUserName>
    <CreateTime>{createTime}</CreateTime>
    <MsgType><![CDATA[text]]></MsgType>
    <Content><![CDATA[{text}]]></Content>
</xml>""".format(userName=self.data.userName,
                 hostName=self.data.hostName,
                 createTime=self.data.createTime,
                 text = text)

    def ImageMsg(self):
        pass