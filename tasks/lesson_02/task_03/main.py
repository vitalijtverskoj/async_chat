"""
Написать скрипт, автоматизирующий сохранение данных в файле YAML-формата.

Для этого:
Подготовить данные для записи в виде словаря, в которомпервому ключу соответствует список, второму — целое 
число, третьему — вложенный словарь, где значение каждого ключа — это целое число с юникод-символом, 
отсутствующим в кодировке ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml. При этом обеспечить 
стилизацию файла с помощью параметра default_flow_style, а также установить возможность работы с юникодом: 
allow_unicode = True; Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

DATA_IN = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
           'items_quantity': 4,
           'items_ptice': {'computer': '200\u20ac-1000\u20ac',
                           'printer': '100\u20ac-300\u20ac',
                           'keyboard': '5\u20ac-50\u20ac',
                           'mouse': '4\u20ac-7\u20ac'}
           }

with open('file.yaml', 'w', encoding='utf-8') as f_in:
    yaml.dump(DATA_IN, f_in, default_flow_style=False, allow_unicode=True, sort_keys=False)

with open("file.yaml", 'r', encoding='utf-8') as f_out:
    DATA_OUT = yaml.load(f_out, Loader=yaml.SafeLoader)

print(DATA_IN == DATA_OUT)
