import os


def visit_shop(player):
    name = player[0]
    hp = player[1]
    money = player[2]
    potions = player[3]

    while True:
        os.system("cls")
        print(f"имя: {name}")
        print(f"здоровье: {hp}")
        print(f"деньги: {money}")
        print(f"зельки: {potions}")

        print("1 - Купить зелье, цена 10 рублей")
        print("2 - выйти ")
        answer = input("Введите номер варианта и нажмите ENTER ")
        if answer == "1":
            if money >= 10:
                potions += 1
                money -= 10
                print("Купил зелье")
            else:
                print("Недостаточно денег")
            input("ENTER - дальше")
        elif answer == "2":
            return (name, hp, money, potions)
