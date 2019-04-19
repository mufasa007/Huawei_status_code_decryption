import rsa,base64
(pub_key, priv_key) = rsa.newkeys(256)

crypto = rsa.encrypt(b'hello', pub_key)
code_ = base64.encodebytes(crypto)

clear = rsa.decrypt(crypto, priv_key)

print(crypto)
print(code_)
print(clear)
