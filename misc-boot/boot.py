from typing import List
from pwn import *
import re

index = 0
MAXCNT = 16536
while index < MAXCNT+1:
    print(index)
    r = remote('172.18.10.105', 30677)
    bytes = bytearray().fromhex("0304")
    r.send_raw(bytes)
    print(r.recvall(10).decode('utf-8'))
    #r.interactive()

    r.close()

data = open("output.txt", "w")
print("Here is the full list")
for value in arrayOfCryptText:
    print(value)
    data.write(value + "\n")

data.close()