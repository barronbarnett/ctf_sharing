from pwn import *

r = remote('172.18.10.105', 38483)
print(" ", r.recvuntil(">>").decode('utf8'))

r.sendline("load_file mysupersecretflagfile")
datastring = "E50EA2B8AFDE62B802D41CD7512B4E0572FD9D00"

hashbytes = bytearray.fromhex(datastring)

for i in range(0,255):
    hashbytes[19] = i
    command = "verify_hash " + bytes(hashbytes).hex() + " 0 20"
    print(command)
    r.sendline(command)
    print("", r.recvuntil(">>").decode('utf8'))

#r.interactive()

