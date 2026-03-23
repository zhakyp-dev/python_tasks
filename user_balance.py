users_balance = [
    {"name": "James", "balance": 10000},
    {"name": "Alex", "balance": 20000},
    {"name": "Jonh", "balance": 50000}
]

def show_balance():
    for balance in users_balance:
        print("Balance: ", balance["name"], "-", balance["balance"], "сом")

show_balance()

def deposit(name, amount):
    for user in users_balance:
        if user["name"] == name:
            user["balance"] += amount
            print("Пополнение для", name, "на", amount)
            return
        print("Пользователь не найден")

deposit("James", 400)

def withdraw(name, amount):
    for user in users_balance:
        if user["name"] == name:
            if user["balance"] >= amount:
                user["balance"] -= amount
                print("Снятие", amount)
            else:
                print("Недостаточно денег")
            return

withdraw("Alex", 500)