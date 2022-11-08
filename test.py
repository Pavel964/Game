import shop
import casino
import os

def start_new_game():
    """
    создать перса:
    имя
    здоровье
    деньги
    зелья
    """
    print("Запустилась новая игра")
    player_name = input("Введите имя игрока и нажмите ENTER ")
    if not player_name:
        player_name = "Святогор"
    player_hp = 999999
    player_money = 1000000
    player_potions = 2
    player = (player_name, player_hp, player_money, player_potions)

    is_game = True
    while is_game:

        os.system("cls")

        print("-- игрок:")
        print(f"имя: {player[0]}")
        print(f"здоровье: {player[1]}")
        print(f"деньги: {player[2]}")
        print(f"зельки: {player[3]}")

        print("-- ситуации")
        print(f"зельки: {player[3]}")
        print(f"")
        print("1 - поехать на битву")
        print("2 - играть в кости")
        print("3 - поехать затариться зельками")
        print("0 - выйти")

        answer = input()
        if answer == "1":
            pass
        elif answer == "2":
            player = casino.visit_casino(player)
        elif answer == "3":
            player = shop.visit_shop(player)
        elif answer == "0":
            is_game = False


start_new_game()