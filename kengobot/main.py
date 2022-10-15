from auth import auth
from flask import Flask, request
from hanlder import Hanlder

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to KengoBot'

@app.route('/wx', methods=["POST", "GET"])
def wx():
    openid = auth(request.args)
    if openid=="": return ""

    handler = Hanlder(request)
    return handler.getSimpleResponse()

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port=80)