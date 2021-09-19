import base64
import hashlib
import math
from Cryptodome.Cipher import AES as domeAES


test_message = "1f5b51fd8d66671c4fd74b131f29dfdfefb373882e167250444c7cb6f0a8b34bd92afb5702bbdbd21b6970e9bd0f70a7"

#All arugments are expected in bytearraay form
def decryptECB(key_data, message_data):
    key = key_data
    message = message_data

    cipher = domeAES.new(key,domeAES.MODE_ECB)

    message_len = len(message)
    block_size = 16
    block_count = math.ceil(message_len/block_size)
    plaintext=bytearray()

    for i in range(0,block_count):
        message_block = message[(i*block_size):block_size]
        block = cipher.decrypt(message_block)
        plaintext.extend(block)
        
    return plaintext

def decryptCBC(key_data, message_data, iv_data):
    key = key_data
    message = message_data
    iv = iv_data

    cipher = domeAES.new(key,domeAES.MODE_CBC, iv)

    message_len = len(message)
    block_size = 16
    block_count = math.ceil(message_len/block_size)
    plaintext=bytearray()

    for i in range(0,block_count):
        message_block = message[(i*block_size):block_size]
        block = cipher.decrypt(message_block)
        plaintext.extend(block)
    plaintext = cipher.decrypt(message)
    return plaintext

def decryptGCM(key_data, iv_data, message_data):
    key = key_data
    iv = iv_data
    message = message_data

    cipher = domeAES.new(key,domeAES.MODE_ECB,iv)

    plaintext = cipher.decrypt(message)
    return plaintext

def splitupMessageWithIV(message):
    message_bytes = bytearray.fromhex(message)
    return [message_bytes[0:16], message_bytes[16:32], message_bytes[32:48]]

def splitupMessageNoIV128(message):
    message_bytes = bytearray.fromhex(message)
    return [message_bytes[0:16], message_bytes[16:48]]

def splitupMessageNoIV256(message):
    message_bytes = bytearray.fromhex(message)
    return [message_bytes[0:32], message_bytes[32:48]]

message_info_iv = splitupMessageWithIV(test_message)
message_info_noiv128 = splitupMessageNoIV128(test_message)
message_info_noiv256 = splitupMessageNoIV256(test_message)

plaintext_ecb128 = decryptECB(message_info_noiv128[0], message_info_noiv128[1])
print("128 ECB: " + plaintext_ecb128.hex())

plaintext_ecb256 = decryptECB(message_info_noiv256[0], message_info_noiv256[1])
print("256 ECB: " + plaintext_ecb256.hex())

plaintext_cbc128 = decryptCBC(message_info_iv[0], message_info_iv[1], message_info_iv[2])
print("128 CBC: " + plaintext_cbc128.hex())