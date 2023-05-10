import math

class Number_System():
    def __init__(self, main_text, main_encoder) -> None:
        self.main_text = main_text
        self.main_encoder = main_encoder
        self.count_bit = 0
        # self.shifr_text = ''
        self.shifr_text_bit = 0


    def decimal_binary(self, main_number):
        'С десятичного сс в двоичное'
        a = []
        while main_number !=1:
            b = main_number%2
            a.insert(0, b)
            main_number = main_number//2
        else:
            a.insert(0, 1)
        print(a)   

    def binary_decimal(self, list_number):
        'С двоичного сс в десятичное'
        result = 0
        list_number.reverse()
        for index, number in enumerate(list_number):
            result += number*(2**index)
        print(result)
    def text_from_bits(self, bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

    def text_to_bits(self, text:str, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        self.shifr_text_bit = bits.zfill(8 * ((len(bits) + 7) // 8))
        return bits.zfill(8 * ((len(bits) + 7) // 8))



class Cryptography(Number_System):
    # def __init__(self) -> None:
    #     self.algoritm_letters = {'у':'y',"о":'o',"а":'a',"с":'c', "р":'p','е':'e','х':'x'} #{рус:англ}
        
    def encryption_letter(self):
        'Шивровка текста через буквы'   
        text = self.main_text
        list_bit = list(self.shifr_text_bit)
        # print(''.join(list_bit))
        list_bit.reverse()
        text = ''.join(text)
        # print(text)
        list_letter = list(text)
        list_letter.reverse()
        c = {'у':'y',"о":'o',"а":'a',"с":'c', "р":'p','е':'e','х':'x'} #{рус:англ}
        index_bit = 0
        for index, i in enumerate(list_letter):
            for r,a in c.items():
                if i == a:
                    list_letter[index] = r

        for index, i in enumerate(list_letter):
            for r, a in c.items(): 
                if i == r:
                    # print(self.shifr_text_bit)
                    # print(reversed(list(self.shifr_text_bit)))
                    try:
                        if list_bit[index_bit] == '1':
                            # print(list_letter[index])
                            list_letter[index] = a
                            # print(list_letter[index])
                        # elif list_bit[index_bit] == '0':
                            # list_letter[index] = '0'
                        index_bit+=1
                    except IndexError:
                        break
                elif i == a:
                    try:
                        if list_bit[index_bit] == '1':
                            list_letter[index] = r
                        # elif list_bit[index_bit] == '0':
                            # list_letter[index] = '0'
                        index_bit+=1
                    except IndexError:
                        break
        list_letter.reverse()
        # print(list_letter)                
        print(''.join(list_letter))
        print('1111')
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(''.join(list_letter))
        


    def decoding_letter(self, main_next):
        'Расшифровка текста через буквы'
        text = main_next
        text = ''.join(text)

        list_text = list(text)
        # list_text.reverse()

        list_bit = []  
        for i in list_text:
            print(i)
            if i in ["у", "о", "а", "с", "р", "е", "х"]: #рус
                list_bit.append('0')
            elif i in ["y", "o", "a", "c", "p", "e", "x"]: #англ
                list_bit.append('1')
        print(''.join(list_bit))
        # while True:
        #     if list_bit[0] == '0':
        #         # print(list(list_bit))
        #         # list_bit = ''.join(list(list_bit).pop(0))
        #         del list_bit[0]
        #     elif list_bit[0] == '1':
        #         break
        # print(''.join(list_bit)) 
        # b = '000000000000000000001110011011000100110010001110011011010100111001101101110'
        # a = list(b)
        # ''.join(list_bit).find('1')
        count = len(list_bit)-(((len(list_bit)-''.join(list_bit).find('1'))//8)+1)*8 
        print(list_bit)
        while count!=0:
            del list_bit[0]
            count-=1 
        print(''.join(list_bit))           
        return ''.join(list_bit)
    

    def encryption_whitespace(self):
        'Шивровка текста через пробелы'
        text = self.main_text
        text = ''.join(text)

        list_text = text.split(' ')
        list_text.reverse()
        print('------ 111')
        print(list_text)
        # bin_text = self.text_to_bits(self.main_encoder)
        list_bin = list(self.shifr_text_bit)
        print(''.join(list_bin))
        list_bin.reverse()
        print('------222')
        print(list_bin)

        for index, i in  enumerate(list_text):
            # if len(list_bin) == index:
            #     list_text[index] = i+'  '
            #     print('wwww')
            #     exit()
            #     break
            try:
                if list_bin[index] == '1':
                    
                    list_text[index] = i+' '
                    # print(i+'1')
                else:
                    # list_text[index] = i+'0'
                    pass
            except IndexError:
                break
            

        print('------333')
        list_text.reverse()
        print(list_text)
        new_text = ' '.join(list_text)
        print(new_text)


        
        print(len(list_text)) 
        
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(new_text)

    def decoding_1(self):
        'Расшифровка текста'
        list_bit = []
        main_text = str(self.main_text)
        print('---1111')
        print(list(main_text))

        for index, i in enumerate(list(main_text)):
            if i == ' ' and list(main_text)[index+1] == ' ':
                list_bit.append('1')
            elif i == ' ' and list(main_text)[index+1] != ' ':
                list_bit.append('0')
            # elif i == ' ' and list(main_text)[index+1] == ' ' and list(main_text)[index+2] == ' ':
                
            #     break
        # list_bit = ''.join(list_bit)
        print(list_bit)
        print(''.join(list_bit))
        print(list_bit[0])
        while True:
            if list_bit[0] == '0':
                # print(list(list_bit))
                # list_bit = ''.join(list(list_bit).pop(0))
                del list_bit[0]
            elif list_bit[0] == '1':
                break
        print(''.join(list_bit))        
        return ''.join(list_bit)


        # main_text = main_text.split(' ')
        # print('----')
        # print(main_text)
    
    def decoding_whitespace(self, main_text):
       
        a = []
        print(list(''.join(main_text)))
        
        for index, i in enumerate(list(''.join(main_text))):
            if index == len(list(''.join(main_text)))-1 and i == ' ':
                a.append('1')
            elif index == len(list(''.join(main_text)))-1 and i != ' ':
                a.append('0')
            try:
                if index == 0:
                    if i == ' ' and list(''.join(main_text))[index+1] != ' ':
                        a.append('0')
                    elif i == ' ' and list(''.join(main_text))[index+1] == ' ':
                        a.append('1')
                        continue
                elif i == ' ' and list(''.join(main_text))[index+1] != ' ' and list(''.join(main_text))[index-1] != ' ':
                    a.append('0') 
                elif i == ' ' and list(''.join(main_text))[index+1] == ' ':
                    a.append('1') 


                    

            except IndexError:
                # a.append('1')
                
                pass
        print(a)
        
        while True:
            if a[0] == '0':
                # print(list(list_bit))
                # list_bit = ''.join(list(list_bit).pop(0))
                del a[0]
            elif a[0] == '1':
                break

        print(''.join(a))
        return''.join(a)





        


     

class Interface():
    def count_bit():
        a = input('Введите текст, в котором хотите узнать обьем в битах: \n')

    def get_main_text():
        a = input("Введите текст в который хоитте вставить зашифровку: ")
    
    def get_main_encoder():
        a = input('Введите текст, который хотите зашифровать: ')

    def output():
        pass
    


# with open("input.txt", "r", encoding="utf-8") as f:
#     main_text = f.readlines()
# print(main_text)

# main_encoder = input('Введите текст, который хотите зашифровать: ')


# User = Cryptography(main_text, main_encoder)


# User.text_to_bits(main_encoder)
# User.encryption()

while True:
    choice = int(input('''
    Допро пожаловать в Шифратор, выберите действие: 

    1) Добаить скрытый шифр в текст.
    2) Расшифровать скрытый шифр.
    3) Узнать количество битов, которые можно зашифровать в тексте.
    4) 

    
    '''))
    if choice == 1:
        with open("input.txt", "r", encoding="utf-8") as f:
            main_text = f.readlines()
        main_encoder = input('Введите текст, который хотите зашифровать: ')

        User = Cryptography(main_text, main_encoder)
        # User = Cryptography()

        User.text_to_bits(main_encoder)
        # User.encryption_whitespace()
        User.encryption_letter()
    elif choice == 2:
            with open("output.txt", "r", encoding="utf-8") as f:
                main_text = f.readlines()
            

            User = Cryptography(main_text, '')

            
            # bin = User.decoding_whitespace(main_text)
            bin = User.decoding_letter(main_text)
            print(User.text_from_bits(bin))

# main_number = int(input('Введите число которое хотите конвертирвать из 10 системы счесления: \n'))
# turn_number = int(input("В какую СС хотите конвертировать ? \n"))


# test(main_number=main_number, turn_number=turn_number)
