import hashlib

def certificateToken(signature, timestamp, nonce):
    token = "KengoBotToKennnn"
    lst = [token.encode(), str(timestamp).encode(), str(nonce).encode()]
    lst.sort()
    sha1 = hashlib.sha1()
    for x in lst:
        sha1.update(x)
    hashcode = sha1.hexdigest()
    print("certificateToken/GET func: hashcode, signature: ", hashcode, signature)
    return hashcode == signature

def auth(args):
    signature = args.get("signature", "")
    timestamp = args.get("timestamp", "")
    nonce = args.get("nonce", "")
    openid = args.get("openid", "")
    if certificateToken(signature, timestamp, nonce):
        return openid
    else:
        return ""