import xmltodict
from response import Response

class Reciever:
    def __init__(self, request):
        data = xmltodict.parse(request.get_data())["xml"]
        self.data = data
        self.userName = data["FromUserName"]
        self.hostName = data["ToUserName"]
        self.createTime = data["CreateTime"]
        self.msgId = data["MsgId"]
        self.msgType = data["MsgType"]
        self.loadMsg()

    def loadMsg(self):
        self.loadTextMsg()
        self.loadImageMsg()
        self.loadVoiceMsg()
        self.loadVideoMsg()
        self.loadLocationMsg()
        self.loadLinkMsg()

    def isTextMsg(self):
        return self.msgType=="text"

    def loadTextMsg(self):
        if self.isTextMsg():
            self.content = self.data["Content"]

    def isImageMsg(self):
        return self.msgType == "image"

    def loadImageMsg(self):
        if self.isImageMsg():
            self.mediaId = self.data["MediaId"]
            self.picUrl = self.data["PicUrl"]

    def isVoiceMsg(self):
        return self.msgType=="voice"

    def loadVoiceMsg(self):
        if self.isVoiceMsg():
            self.mediaId = self.data["MediaId"]
            self.format = self.data["Format"]
            self.recognition = self.data["Recognition"] if "Recognition" in self.data else ""

    def isVideoMsg(self):
        return self.msgType=="video" or self.msgType=="shortvideo"

    def loadVideoMsg(self):
        if self.isVideoMsg():
            self.mediaId = self.data["MediaId"]
            self.thumbMediaId = self.data["ThumbMediaId"]

    def isLocationMsg(self):
        return self.msgType=="location"

    def loadLocationMsg(self):
        if self.isLocationMsg():
            self.lat = self.data["Location_X"]
            self.lon = self.data["Location_Y"]
            self.scale = self.data["Scale"]
            self.lable = self.data["Label"]

    def isLinkMsg(self):
        return self.msgType=="link"

    def loadLinkMsg(self):
        if self.isLocationMsg():
            self.title = self.data["Title"]
            self.desc = self.data["Description"]
            self.url = self.data["Url"]