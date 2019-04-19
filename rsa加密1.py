import base64
from rsa import key, common, encrypt
(pub_key, priv_key) = key.newkeys(256)
message = b'[{"WORK_PLACE_NAME":"'

crypto = encrypt(message, pub_key)
print(crypto)

code_ = base64.encodebytes(crypto)
print(code_)

bit_ = base64.decodebytes(code_)
print(bit_)
