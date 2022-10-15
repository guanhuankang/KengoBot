from certificateToken import certificateToken
from flask import Flask, request

'''
    AppSecret: 849ae7804e7facd47e9c2d4e4fc861c9
    AppId: wxb19f49d8dfe1ceb1
'''

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to Flask'

@app.route('/wx', methods=["POST", "GET"])
def wx():
    ## authurtification
    signature = request.args.get("signature", "")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    openid = request.args.get("openid", "")

    if not certificateToken(signature, timestamp, nonce):
        return "auth_fail"

    print(request.get_data())
    return "success"

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port=80)