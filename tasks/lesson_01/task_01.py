"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и 
содержание соответствующих переменных. Затем с помощью онлайн-конвертера преобразовать строковые 
представление в формат Unicode и также проверить тип и содержимое переменных.
"""

WORD_STR_1 = "разработка"
WORD_STR_2 = "сокет"
WORD_STR_3 = "декоратор"


WORD_STR_LIST = [WORD_STR_1, WORD_STR_2, WORD_STR_3]

for i in WORD_STR_LIST:
    print(type(i))
    print(i)

WORD_UNI_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
WORD_UNI_2 = '\u0441\u043e\u043a\u0435\u0442'
WORD_UNI_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

WORD_UNI_LIST = [WORD_UNI_1, WORD_UNI_2, WORD_UNI_3]

for i in WORD_UNI_LIST:
    print(type(i))
    print(i)
