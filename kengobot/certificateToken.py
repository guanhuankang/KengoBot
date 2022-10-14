import hashlib

def certificateToken(signature, timestamp, nonce, echostr):
    token = "KengoBotToKennnn"
    list = [token, timestamp, nonce]
    list.sort()
    sha1 = hashlib.sha1()
    map(sha1.update, list)
    hashcode = sha1.hexdigest()
    print("handle/GET func: hashcode, signature: ", hashcode, signature)
    if hashcode == signature:
        return echostr
    else:
        return "unmatched"