"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": []
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""

import json


def write_order_to_json(item: str, quantity: int, price: int, buyer: str, date: str):
    new_orders = {'item': item, 'quantity': quantity,
                  'price': price, 'buyer': buyer, 'date': date}

    with open('orders.json') as f_n:
        objs = json.load(f_n)
    objs.get('orders').append(new_orders)
    print(objs)
    with open('orders.json', 'w') as f_n:
        json.dump(objs, f_n, sort_keys=True, indent=2, ensure_ascii=False)


write_order_to_json("Computer", 5, 500, "Nobody", "24.02.2023")
