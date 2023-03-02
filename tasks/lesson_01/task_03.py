"""
Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''.
"""

WORD_STR_1 = 'attribute'
WORD_STR_2 = 'класс'
WORD_STR_3 = 'функция'
WORD_STR_4 = 'type'

WORD_STR_LIST = [WORD_STR_1, WORD_STR_2, WORD_STR_3, WORD_STR_4]

for i in WORD_STR_LIST:
    try:
        print(bytes(i, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{i}" невозможно записать в виде байтовой строки')
