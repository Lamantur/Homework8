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
