import random as r


first_names = ("Жран", "Дрын", "Брыст")
last_names = ("Ужасный", "Борзый", "Кровавый")


def make_hero(
    name="Безымянный",
    hp=1,
    xp=0,
    attack=1,
    defence=0,
    money=1000,
    potions=0
) -> tuple:
    if not name:
        name = f"{r.choice(first_names)} {r.choice(last_names)}"
    if not hp:
        hp = r.randint(1, 100)
    if not xp:
        xp = r.randint(1, 100)
    if not attack:
        attack = r.randint(1, 100)
    if not defence:
        defence = r.randint(1, 100)
    if not money:
        money = r.randint(1, 100)
    if not potions:
        potions = r.randint(1, 100)
    return (name, hp, xp, attack, defence, money, potions)


def show_hero(hero: tuple):
    

print(hero_1)
print(hero_1)
print(hero_1)