from pwn import *

r = remote('172.18.10.105', 30677)

print(" ", r.recvline().decode('utf8'))
print(" ", r.recvline().decode('utf8'))

r.sendline("rescue")

print(" ", r.recvall().decode('utf8'))