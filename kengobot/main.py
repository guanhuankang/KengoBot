import logging, os
logging.basicConfig(level=logging.INFO)

from auth import auth
from flask import Flask, request
from reciever import Reciever
from response import Response

app = Flask(__name__)
HOME_DIR = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
def root():
    return 'welcome to KengoBot'

@app.route('/wx', methods=["POST", "GET"])
def wx():
    openid = auth(request.args)
    if openid=="": return ""

    data = Reciever(request)
    response = Response(data)
    return response.textMsg(text=data.content if data.isTextMsg() else str(data.msgType))

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port=80)