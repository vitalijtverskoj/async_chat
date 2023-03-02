"""
Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

"""

WORD_STR_1 = 'разработка'
WORD_STR_2 = 'администрирование'
WORD_STR_3 = 'protocol'
WORD_STR_4 = 'standard'

WORD_STR_LIST = [WORD_STR_1, WORD_STR_2, WORD_STR_3, WORD_STR_4]

WORD_BYTE_LIST = []

for i in WORD_STR_LIST:
    print(i)
    k = i.encode('utf-8')
    print(k)
    WORD_BYTE_LIST.append(k)

for i in WORD_BYTE_LIST:
    print(i)
    k = i.decode('utf-8')
    print(k)
