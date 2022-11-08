import os


def visit_casino(player):
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

        print("1 - Сыграть на 10 монет")
        print("2 - выйти ")
        answer = input("Введите номер варианта и нажмите ENTER ")
        if answer == "1":
            if money >= 10:
                player = random.randint(1, 32) # кидаем кости от 1 до 32
                casino = random.randint(1, 32) # кидаем кости от 1 до 32

                print("Игрок кинул", player) # печатаем кости игрока
                print("казино кинуло", casino) # печатаем кости компа
                if player > casino:
                    print("Игрок победил!")
                elif cpu > player:
                    print("казино победило!")
                else:
                    print("Ничья!")

            else:
                print("Недостаточно денег")
            input("ENTER - дальше")
        elif answer == "2":
            return (name, hp, money, potions)
