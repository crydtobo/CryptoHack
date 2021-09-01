import codecs
import base64

print("Task -> base64 ")
decode_str = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
decoded_hex = codecs.decode(decode_str, 'hex')
encoded_b64 = codecs.encode(decoded_hex, 'base64').decode()

# solution
print(encoded_b64)

# bytes and big integer

print("Task -> bytes and big integer ")

# base10 integer
dec_hex = 11515195063862318899931685488813747395775516287289682636499965282714637259206269
# first step convert to hex
hex_integer = hex(dec_hex)
m = '63727970746f7b336e633064316e365f346c6c5f3768335f7734795f6430776e7d'
bytes_hex = bytes.fromhex(m)

# solution
print(bytes_hex)

# Encoding challenge

print("Task -> Encoding challenge ")
