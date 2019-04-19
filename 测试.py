import base64
import 状态码解密

# with open('clear.txt', 'rb') as f:
with open('clear.txt', 'rb') as f:
    clear = f.read()
# print(clear)
# print(len(clear))

# line = []
# for i in clear:
#     line.append(i)
# print(line)

with open('key.txt', 'rb') as f:
    key = f.read()
print(key)

d1 = 状态码解密.rsa_encrypt(clear,key)
print(d1)


# d0 = 'abc='
# d1 = '万雨'

# b0_str = base64.b64decode(d0)
# b1_str = base64.b64decode(d1)

