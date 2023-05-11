# 'www'
# # import unicide 
import requests
# A = 'привет'
# print(repr(A))
# print(type(repr(A)))
# import unicodedata 
# print(unicodedata.normalize('NFC', A))

# import ftfy
# print(ftfy.fix_text(A))
# print(''.join([str(i) for i in A]))

# data = "Привет".encode("utf-8")
# print(data)


# url = 'https://allcalc.ru/node/1977'
# x = requests.post('https://allcalc.ru/node/1977')

# # print(x)
# # print(x.text)
# with open('text.txt', 'w') as f:
#     for i in x.text:

#         f.write(i)

# print(bin(25))
# print(ascii("My name is Ståle"))
# print(repr('b'))


def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))


# print(text_to_bits('привет'))
# print(text_to_bits('привет как дела ?'))
# print(text_from_bits('110100001011111111010001100000001101000010111000110100001011001011010000101101011101000110000010001000001101000010111010110100001011000011010000101110100010000011010000101101001101000010110101110100001011101111010000101100000010000000111111'))
import time
# import pyautogui
# print(pyautogui.position())
# while True:
#     pyautogui.click(x=1005, y=909)
#     time.sleep(1)
# import pyrogram

# import asyncio
# from pyrogram import Client

# api_id = 14460056
# api_hash = "37a84ab4c73a4c1b3addb04da7a83df0"


# def main():
#     with Client("my_account", api_id, api_hash) as app:
#         while True:
#             app.send_message('mine_evo_bot', "⛏ Копать")
#             time.sleep(1)

# main()


# a = '123'
# print(bool('asdа'=='asda'))

# a =                                            '110100001001111111010001100000001101000010111000110100001011001011010000101101011101000110000010'
# b = '1010010000010001010101010101001000010100000000101001000001001010100001010010000010000101000100101001000001001010010010101001000010100000010'
# # print(len(a))
# with open('input.txt', 'r', encoding='utf-8') as f:
#     a = f.read()
#     # print(a)
# print(list(''.join(a)))
# count = 0
# for i in list(''.join(a)):
#     if i == 'у' or i == "о" or i == "а" or i == "с" or i == "р" or i == 'е' or i == 'х':
#         print(i)
#         count+=1
# print(len(list(''.join(a)))) 
# print(count)

# a = {'1':'2',"о":'o',"а":'a',"с":'c', "р":'p','е':'e','х':'x'}
110100001001111110100001100000001101000010111000110100001011001011010000101101011101000110000101
110100001001111111010001100000001101000010111000110100001011001011010000101101011101000110000010
# for k,i in a.items():
#     print(i)
#     print(k)

b = '000000000000000000001110011011000100110010001110011011010100111001101101110'
a = list(b)
count = len(a)-(((len(a)-b.find('1'))//8)+1)*8 

while count!=0:
    del a[0]
    count-=1

print(''.join(a))





