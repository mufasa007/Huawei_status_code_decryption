import rsa,base64

# 生成密钥
# (pubkey, privkey) = rsa.newkeys(1024)
# with open('public.pem', 'w+') as f:
#     f.write(pubkey.save_pkcs1().decode())
# with open('private.pem', 'w+') as f:
#     f.write(privkey.save_pkcs1().decode())

# 导入密钥
with open('public.pem', 'r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())
# with open('private.pem', 'r') as f:
with open('key.pem', 'r') as f:
    privkey = rsa.PrivateKey.load_pkcs1(f.read().encode())

# with open('clear.txt', 'rb') as f:
#     clear = f.read()

with open('cipher.txt', 'rb') as f:
    cipher = f.read()

# with open('private.pem', 'r') as f:
#     clear = f.read().encode()


# clear = '[{"WORK_PLACE_NAME":"中国/深圳","IV_EXISTS":"1","JOB_TYPE":"0","CURRENT_DEPT":"037956/产品与解决方'.encode()
# crypto_email_text = rsa.encrypt(clear, pubkey)
# crypto_base64 = base64.encodebytes(crypto_email_text)
# print(crypto_base64)  # 什么鬼？看不懂啊！



message1 = rsa.decrypt(base64.decodebytes(cipher), privkey).decode()
print(message1)

