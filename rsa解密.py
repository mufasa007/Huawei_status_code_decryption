#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
# rsa
from rsa import PublicKey, common, transform, core


def f(cipher, PUBLIC_KEY):
    public_key = PublicKey.load_pkcs1(PUBLIC_KEY)
    encrypted = transform.bytes2int(cipher)
    decrypted = core.decrypt_int(encrypted, public_key.e, public_key.n)
    text = transform.int2bytes(decrypted)

    if len(text) > 0 and text[0] == '\x01':
        pos = text.find('\x00')
        if pos > 0:
            return text[pos + 1:]
        else:
            return None


clearPath = sys.stdin.readline()[:-1]
keyPath = sys.stdin.readline()[:-1]
cipherPath = sys.stdin.readline()[:-1]

clear = open(clearPath, 'rb').read()
key = open(keyPath, 'rb').read()
cipher = open(cipherPath, 'rb').read()

# print(clear)
# print(key)
# print(cipher)

str_out = f(cipher, key)
print(str_out)

"""
clear.txt
key.pem
cipher.txt
"""