from typing import List
from pwn import *
import sys
import re
import csv

input_file = sys.argv[1]
output = sys.argv[2]

bins = []

KNOWNTEXT = "RTXFLAG{"
bytes = bytearray().fromhex("0000000000000000")

def get_data():    
    print(input_file)
    data = open(input_file, 'r')
    datalines = []
    for line in data:
        datalines.append(line.strip())
    data.close()
    return datalines

def build_crypt_message_list(datalines):
    crypt_messages = []
    for line in datalines:
        crypt_messages.append(bytearray.fromhex(line))
    return crypt_messages

def build_stats(messages):
    bins = []
    for message in messages:
        message_bin = [0] * 257
        for byte in message:
            # print(str(byte))
            message_bin[byte] = message_bin[byte] + 1
        
        greater_than_1 = 0
        for byte in message_bin:
            if byte > 1:
                greater_than_1 = greater_than_1 + 1
        
        message_bin[256] = greater_than_1

        bins.append(message_bin)
    return bins

def analyze_message(bin):
    for message in bin:
        print(str(message[256]))
    

def write_output(bins):
    out = open(output, 'w')
    writer = csv.writer(out)

    for bin in bins:
        writer.writerow(bin)
    out.close()

def GetXORKey(message):
    kt_bytes = bytearray(KNOWNTEXT.encode())
    key = bytearray().fromhex("0000 0000 0000 0000")
    for i in range(len(kt_bytes)):
        key[i] = message[i] ^ kt_bytes[i]

    return key

def DecryptMessage(message, key):
    plaintext = bytearray(len(message))
    for i in range(len(message)):
        plaintext[i] = key[i%len(key)] ^ message[i]

    #print(plaintext.decode('ascii'))
    return plaintext

def BreakMessages(messages):
    plaintext_messages = []

    for message in messages:
        key = GetXORKey(message)
        pt_message = DecryptMessage(message, key)
        plaintext_messages.append(pt_message)

data = get_data()
messages = build_crypt_message_list(data)
stat_bin = build_stats(messages)
pt_messages = BreakMessages(messages)
analyze_message(stat_bin)




