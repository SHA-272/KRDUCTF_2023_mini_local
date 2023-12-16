from Crypto.Cipher import AES
from Crypto.Util.Padding import *
import random
from base64 import *

sample = b'krdu{**********************************************}' 
flag = b'krdu{Th1s_1s_n0T_a_fl@g_546831735f31735f6e30545f615f666c4067}'

KEY_LEN = 16
BS = 16

key = bytes([random.randint(0, 255) for _ in range(KEY_LEN)])
    
key_out = AES.new(key, AES.MODE_ECB)
cipher = key_out.encrypt(pad(sample,BS))
kb64 = b64encode(b'key_out')
cb64 = b64encode(cipher)

print(f'cipher = {cb64.hex()}')
print(f'key = NOT ALLOWED') 

