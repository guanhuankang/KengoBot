from kengobot.certificateToken import certificateToken
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def root():
    return 'welcome to Flask'

@app.route('/wx', methods=["POST"])
def wx():
    signature = request.form.get("signature")
    timestamp = request.form.get("timestamp")
    nonce = request.form.get("nonce")
    echostr = request.form.get("echostr")
    return certificateToken(signature, timestamp, nonce, echostr)

if __name__ == '__main__':
    app.run(debug = False, host="0.0.0.0")