from typing import List
from pwn import *
import re

arrayOfCryptText = []
initial_crypt_text = ""
research = "([0-9,a-f]{96})"

index = 0
MAXCNT = 16536
while index < MAXCNT+1:
    print(index)
    r = remote('172.18.10.105', 30303)
    text = r.recvline().decode('utf8')
    result = re.split(research, text)[1]

    if not arrayOfCryptText:
        initial_crypt_text = result
        arrayOfCryptText.append(result)
    else:
        if (initial_crypt_text == result):
            print("We Got One")

        arrayOfCryptText.append(result)
    
    index = index + 1

    r.close()

data = open("output.txt", "w")
print("Here is the full list")
for value in arrayOfCryptText:
    print(value)
    data.write(value + "\n")

data.close()