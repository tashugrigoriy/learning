# Функция дешифровки (шифровки) русского текста,
# с помощью шифра Цезаря, работает с любым регистром символов русского
# алфавита и выводит строку в такой же пунктуации и с такими же символами
# как и введенная строка. Кому нужен файл.py - все мои наработки
# здесь: https://t.me/GrIT_tries_programming
# Функция шифрует русский текст со сдвигом вправо,
# и ДЕШИФРИРУЕТ РУССКИЙ текст, зашифрованный со сдвигом ВЛЕВО.

def decrypt_russian_text_left(step):
    step = int(input('Please, indicate the decryption step: '))
    res = ''

    for char in text:
        if ord(char) not in range(1039, 1104):
            res += char

        elif char == char.lower() and (ord(char.lower()) + step) > 1103:
            res += chr(ord(char.lower()) + step - 32)
        elif char == char.upper() and (ord(char.upper()) + step) > 1071:
            res += chr(ord(char.upper()) + step - 32)

        else:
            res += chr(ord(char) + step)

    print(res)


text = input('Write your text here: ')
decrypt_russian_text_left(text)
