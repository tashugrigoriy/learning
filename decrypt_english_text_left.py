# Функция дешифровки (шифровки) английского текста
# с помощью шифра Цезаря, работает с любым регистром символов английского
# алфавита и выводит строку в такой же пунктуации и с такими же символами
# как и введенная строка. Кому нужен файл.py - все мои наработки
# здесь: https://t.me/GrIT_tries_programming
# Функция шифрует английский текст со сдвигом вправо,
# и ДЕШИФРИРУЕТ АНГЛИЙСКИЙ текст, зашифрованный со сдвигом ВЛЕВО.

def decrypt_english_text_left(step):
    step = int(input('Please, indicate the decryption step: '))
    res = ''
    for char in text:
        if char == char.lower() and ord(char.lower()) not in range(96, 123):
            res += char
        elif char == char.upper() and ord(char.upper()) not in range(64, 91):
            res += char

        elif char == char.lower() and (ord(char.lower()) + step) > 122:
            res += chr(ord(char.lower()) + step - 26)
        elif char == char.upper() and (ord(char.upper()) + step) > 90:
            res += chr(ord(char.upper()) + step - 26)

        else:
            res += chr(ord(char) + step)

    print(res)


text = input('Write your text here: ')
decrypt_english_text_left(text)
