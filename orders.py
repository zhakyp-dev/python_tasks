orders = [
    {"name": "Пицца", "price": 500},
    {"name": "Бургер", "price": 300},
    {"name": "Кола", "price": 100}
]

def show_orders():
    for order in orders:
        print(order["name"], "-", order["price"], "сом")
        if order["price"] < 200:
            print(order["name"])

print(orders)
show_orders()