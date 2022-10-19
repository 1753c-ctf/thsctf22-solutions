#!/usr/bin/env python3

from Crypto.Util.number import long_to_bytes, bytes_to_long
import re
import requests
import random
from functools import reduce
from operator import mul
from base64 import b64encode, b64decode
from string import ascii_letters

from secret_cookie import SECRET_COOKIE

# > factor(bytes_to_long(b'Admin'))
# 2 * 3 * 13 * 113 * 31864961
# > long_to_bytes(31864961*2*3).decode()
# '\x0beS\x06'
# > long_to_bytes(13).decode()
# '\r'
# > long_to_bytes(113).decode()
# 'q'
# sign each part, multiply results, got signature for Admin

def test_local():
    from respectable_signature_algorithm.rsa_sign import rsa_keygen, rsa_sign, rsa_verify
    text = b'text1234'
    pubkey, privkey = rsa_keygen(1024)

    signature = rsa_sign(privkey, text)

    assert(rsa_verify(pubkey, text, signature) == True)
    assert(rsa_verify(pubkey, text + b'\x00', signature) == False)
    assert(rsa_verify(pubkey, text, signature + b'\x00') == False)

    e, n = pubkey
    text0 = bytes_to_long(text) % n
    textm1 = pow(text0, -1, n)
    text1 = bytes_to_long(b'Admin')
    textsig = (text1 * textm1) % n
    signature1 = bytes_to_long(rsa_sign(privkey, long_to_bytes(textsig)))

    assert(long_to_bytes((textsig * text0) % n) == b'Admin')
    signature_forged = long_to_bytes((signature1 * bytes_to_long(signature)) % n)
    assert(rsa_verify(pubkey, b'Admin', signature_forged))

# url_base = 'http://172.17.0.2:3000'
url_base = 'https://respectable-signature-algorithm-6a751faa43.thsctf.site'

def get_user_signature(username):
    resp = requests.post(url_base + '/login', data={'username': username}, cookies=SECRET_COOKIE)
    print(f'{username=}: {resp.status_code=} {resp.cookies["user_token"]=}')
    token = b64decode(resp.cookies["user_token"])
    signature = token[token.find(b':')+1:]
    return signature

def main():
    test_local()

    resp = requests.get(url_base + '/verify_user.js', cookies=SECRET_COOKIE)
    print(resp.text)
    match = re.search('n=(\d+)', resp.text)
    print(match[1])
    n = int(match[1])

    print(f'{n=}')

    users = [13, 113, 2*3*31864961]
    assert(long_to_bytes(reduce(mul, users, 1)) == b'Admin')

    signatures = []
    for user in users:
        user = long_to_bytes(user).decode()
        signatures.append(bytes_to_long(get_user_signature(user)))

    admin_signature = reduce(mul, signatures, 1) % n
    admin_signature = long_to_bytes(admin_signature)

    admin_cookie = b64encode(b'Admin:' + admin_signature).decode()
    print(f'{admin_cookie=}')

    resp = requests.get(url_base + '/get_flag', cookies={'user_token': admin_cookie} | SECRET_COOKIE)
    print(resp.text)

if __name__ == '__main__':
    main()

