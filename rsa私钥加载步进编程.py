import rsa
with open('key.pem', mode='rb') as privatefile:
    keyfile = privatefile.read()

der = rsa.pem.load_pem(keyfile, b'RSA PRIVATE KEY')
from pyasn1.codec.der import decoder

(priv, _) = decoder.decode(keyfile)

if priv[0] != 0:
    raise ValueError('Unable to read this file, version %s != 0' % priv[0])
as_ints = map(int, priv[1:6])

key = rsa.key._load_pkcs1_der(*as_ints)

exp1, exp2, coef = map(int, priv[6:9])
# if (key.exp1, key.exp2, key.coef) != (exp1, exp2, coef):
#     warnings.warn(
#         'You have provided a malformed keyfile. Either the exponents '
#         'or the coefficient are incorrect. Using the correct values '
#         'instead.',
#         UserWarning,
#     )


