import logging, os
logging.basicConfig(level=logging.INFO)

from auth import auth
from flask import Flask, request
from reciever import Reciever
from response import Response
from db import DB
from api import API

app = Flask(__name__)
HOME_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def root():
    return 'welcome to KengoBot'

@app.route('/wx', methods=["POST", "GET"])
def wx():
    openid = auth(request.args)
    if openid=="": return ""

    db = DB()
    api = API(db)
    data = Reciever(request)
    response = Response(data)

    if data.isTextMsg():
        if data.content=="openid":
            return response.textMsg(openid)
        else:
            return response.textMsg(text=data.content)
    if data.isImageMsg():
        img = data.content
        filepath = os.path.join(HOME_DIR, "static/{}.png".format(openid))
        logging.info("save to local filepath:{}".format(filepath))
        img.save(filepath)
        media_id = api.uploadImage(filepath)
        logging.log("new media_id:{}, local_filePath:{}".format(media_id, filepath))
        return response.ImageMsg(media_id)
    return response.textMsg("unsupported msg type - {}".format(data.msgType))

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port=80)