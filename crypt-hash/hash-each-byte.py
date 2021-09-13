from pwn import *

r = remote('172.18.10.105', 38483)
print("", r.recvuntil('>>').decode('utf8'))

r.sendline("load_file mysupersecretflagfile")
print("", r.recvuntil('>>').decode('utf8'))

for i in range(0,20):
    command = "hash " + str(i) + " " + str(1)
    print(command)
    r.sendline(command)
    print("", r.recvuntil('>>').decode('utf8'))


command = "hash " + str(8) + " " + str(10)
print(command)
r.sendline(command)
print("", r.recvuntil('>>').decode('utf8'))
#r.interactive()

