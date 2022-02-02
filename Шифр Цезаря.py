text = input(
    'Введите текст, который необходимо зашифровать/расшифровать с помощью алгоритма Цезаря\n')
destination = input(
    'Укажите направление: ш/s = шифрование или д/d = дешифрование\n').lower()
language = input(
    'Укажите язык алфавита: р/r = русский или а/e = английский\n').lower()
step = int(input('Укажите шаг сдвига(целое число)\n'))

new_text = ''
if destination == 'ш' or destination == 's':
    if language == 'а' or language == 'e':
        for c in text:
            if c.isalpha():
                if c.isupper():
                    new_text += chr((ord(c) - ord('A') + step) %
                                26 + ord('A'))
                else:
                    new_text += chr((ord(c) - ord('a') + step) %
                                26 + ord('a'))
            else:
                new_text += c
    else:
        for c in text:
            if c.isalpha():
                if c.isupper():
                    new_text += chr((ord(c) - ord('А') + step) %
                                32 + ord('А'))
                else:
                    new_text += chr((ord(c) - ord('а') + step) %
                                    32 + ord('а'))
            else:
                new_text += c
    print('Зашифрованный текст:', new_text, sep='\n')
else:
    if language == 'а' or language == 'e':
        for c in text:
            if c.isalpha():
                if c.isupper():
                    new_text += chr((ord(c) - ord('A') - step) %
                                26 + ord('A'))
                else:
                    new_text += chr((ord(c) - ord('a') - step) %
                               26 + ord('a'))
            else:
                new_text += c
    else:
        for c in text:
            if c.isalpha():
                if c.isupper():
                    new_text += chr((ord(c) - ord('А') - step) %
                                32 + ord('А'))
                else:
                    new_text += chr((ord(c) - ord('а') - step) %
                                    32 + ord('а'))
            else:
                new_text += c
    print('Расшифрованный текст:', new_text, sep='\n')