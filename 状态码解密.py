# coding=utf-8
import base64
import rsa

__all__ = ['rsa_encrypt']


def _str2key(s):
    # 对字符串解码
    b_str = base64.b64decode(s)

    if len(b_str) < 162:
        return False

    hex_str = ''

    # 按位转换成16进制
    for x in b_str:
        h = hex(x)[2:]
        h = h.rjust(2, '0')
        hex_str += h

    # 找到模数和指数的开头结束位置
    m_start = 29 * 2
    e_start = 159 * 2
    m_len = 128 * 2
    e_len = 3 * 2

    modulus = hex_str[m_start:m_start + m_len]
    exponent = hex_str[e_start:e_start + e_len]

    return modulus, exponent

# *** rsa加密 *** #
def rsa_encrypt(s, pubkey_str):
    '''
    :param s:原始数据输入
    :param pubkey_str:公钥
    :return:
    '''
    key = _str2key(pubkey_str)

    modulus = int(key[0], 16)
    exponent = int(key[1], 16)

    pubkey = rsa.PublicKey(modulus, exponent)
    # d1 = s.decode()
    # print(d1)
    d2 = rsa.encrypt(s, pubkey)
    d3 = base64.b64encode(d2)
    d4 = d3.decode()

    return d4

