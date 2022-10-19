#!/usr/bin/env python3

import itertools
import struct
import string

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

from aes_rtc.aes_rtc import aes_rtc_decrypt, xor_bytes, IV_LEN

orig_ct = bytes.fromhex('7e69c62fc369374fd465c1a0001874a3eb933e45cb5143d53b3a9b224b9eab7c7b3bb9e6f1ddc49d0181b3c750bf67bb0715b2c705881d9bbedc212cb2f2441c79089039f2769e2d8625798dfb4f63fc9286fd0f53087439c5b771ebeb1dad8af95f050cf4981cbf')
flag_len = 100

iv = orig_ct[:IV_LEN]
ct = orig_ct[IV_LEN:]

first_block_ct = ct[:AES.block_size]
last_block_ct = ct[-AES.block_size:]

last_block_counter = len(ct) // AES.block_size - 1
last_block_ks_key = iv + struct.pack('!Q', last_block_counter)

last_block_cipher = AES.new(last_block_ks_key, AES.MODE_ECB)

first_block_ks_key = iv + b'\x00' * 8

first_block_cipher = AES.new(first_block_ks_key, AES.MODE_ECB)

flag_chars = string.ascii_letters + string.digits + '_'

for last_block_pt in itertools.product(flag_chars, flag_chars, flag_chars):
    last_block_pt = ''.join(last_block_pt)
    last_block_pt = last_block_pt + '}'
    last_block_pt = pad(last_block_pt.encode(), AES.block_size)
    last_block_ks = xor_bytes(last_block_ct, last_block_pt)

    key = last_block_cipher.decrypt(last_block_ks)
    first_block_ks = first_block_cipher.encrypt(key)
    
    first_block_pt = xor_bytes(first_block_ks, first_block_ct)
    if first_block_pt.startswith(b'THSCTF{'):
        print(f'{key=}')
        break

print(aes_rtc_decrypt(key, orig_ct))

