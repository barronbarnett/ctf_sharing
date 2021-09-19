#!/usr/bin/env python
from pwn import *
import sys

#context.log_level = 'debug'
#p = process(['obj-x86_64-linux-gnu/simduino.elf', 'bldr.hex'])
p = remote('172.18.10.105',32557)
p.recvuntil("What's the length of your payload?")

payload = open(sys.argv[1], 'rb').read()

p.writeline(str(len(payload)))
p.write(payload)

p.interactive()
