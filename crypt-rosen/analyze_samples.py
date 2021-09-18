from typing import List
from pwn import *
import sys
import re
import csv

input_file = sys.argv[1]
output = sys.argv[2]

crypt_messages = []
bins = []

print(input_file)

data = open(input_file, 'r')
datalines = []
for line in data:
    datalines.append(line.strip())

data.close()

for line in datalines:
    crypt_messages.append(bytearray.fromhex(line))

full_bin = [0] * 256

for message in crypt_messages:
    message_bin = [0] * 256
    for byte in message:
        # print(str(byte))
        message_bin[byte] = message_bin[byte] + 1
        full_bin[byte] = full_bin[byte] + 1
    
    # for byte in message_bin:
    #     print(str(byte) + ", ", end='')
    # print("")
    bins.append(message_bin)

for byte in full_bin:
    print(str(byte) + ", ", end='')
print("")

out = open(output, 'w')
writer = csv.writer(out)

writer.writerow(full_bin)

for bin in bins:
    writer.writerow(bin)

out.close()

