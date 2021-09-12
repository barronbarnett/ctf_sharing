from pwn import *

r = remote('172.18.10.105', 30677)
print(" ", r.recv().decode('utf-8') )
#r.interactive()

