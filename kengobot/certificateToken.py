import hashlib

def certificateToken(signature, timestamp, nonce, echostr):
    token = "KengoBotToKennnn"
    lst = [token.encode(), str(timestamp).encode(), str(nonce).encode()]
    lst.sort()
    sha1 = hashlib.sha1()
    for x in lst:
        sha1.update(x)
    hashcode = sha1.hexdigest()
    print("handle/GET func: hashcode, signature: ", hashcode, signature)
    if hashcode == signature:
        return echostr
    else:
        return "unmatched"