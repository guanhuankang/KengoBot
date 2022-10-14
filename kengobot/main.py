from certificateToken import certificateToken
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to Flask'

@app.route('/wx', methods=["POST", "GET"])
def wx():
    if request.method=="POST":
        signature = request.form.get("signature")
        timestamp = request.form.get("timestamp")
        nonce = request.form.get("nonce")
        echostr = request.form.get("echostr")
    else:
        signature = request.args.get("signature","")
        timestamp = request.args.get("timestamp","")
        nonce = request.args.get("nonce","")
        echostr = request.args.get("echostr","")
    return certificateToken(signature, timestamp, nonce, echostr)

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0", port=80)