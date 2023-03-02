"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в 
последовательность кодов (не используя методы encode и decode) и определить тип, содержимое и длину 
соответствующих переменных.
"""

WORD_BYTE_1 = b'class'
WORD_BYTE_2 = b'function'
WORD_BYTE_3 = b'method'

WORD_BYTE_LIST = [WORD_BYTE_1, WORD_BYTE_2, WORD_BYTE_3]

for i in WORD_BYTE_LIST:
    print(i)
    print(type(i))
    print(len(i))
