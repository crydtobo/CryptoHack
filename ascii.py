#ascii 
ascii_list = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67,
              73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]
words = ""

for i in ascii_list:
    words += chr(i)
print(words)

#hex encoded 

hex_string = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d"

flag = bytes.fromhex(hex_string).decode('utf-8')

print(flag)