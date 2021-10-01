# Функция дешифровки (шифровки) русского текста,
# с помощью шифра Цезаря, работает с любым регистром символов русского
# алфавита и выводит строку в такой же пунктуации и с такими же символами
# как и введенная строка. Кому нужен файл.py - все мои наработки
# здесь: https://t.me/GrIT_tries_programming
# Функция шифрует русский текст со сдвигом влево,
# и ДЕШИФРИРУЕТ РУССКИЙ текст, зашифрованный со сдвигом ВПРАВО.

def decrypt_russian_text_right(step):
    step = int(input('Please, indicate the decryption step: '))
    res = ''

    for char in text:
        if ord(char) not in range(1039, 1104):
            res += char

        elif char == char.lower() and (ord(char.lower()) - step) < 1072:
            res += chr(ord(char.lower()) - step + 32)
        elif char == char.upper() and (ord(char.upper()) - step) < 1040:
            res += chr(ord(char.upper()) - step + 32)

        else:
            res += chr(ord(char) - step)

    print(res)


text = input('Write your text here: ')
decrypt_russian_text_right(text)
