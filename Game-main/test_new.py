from random import randint


first_names = ("Жран", "Дрын", "Брыст")
last_names = ("Ужасный", "Борзый", "Кровавый")

def make_hero(
        name=None,
        hp_now=None,
        lvl=1,
        xp_now=1,
        xp_next=1000,
        attack=1,
        defence=0,
        luck=1,
        money=None,
        inventory=None,
) -> list:
    """
    Персонаж - это список
    [0] name - имя
    [1] hp_now - текущее здоровье
    [2] hp_max - здоровье максимальное
    [3] lvl - уровень
    [4] xp_now - опыт текущий
    [5] xp_next - опыт до следующего уровня
    [6] attack - сила атаки, применяются в бою
    [7] defence - защита, применяются в бою
    [8] luck
    [9] money
    [10] inventory
    """
    if not name:
        name = choice(first_names) +""+ choice(last_names)


    if not hp_now:
        hp_now = randint(1, 100)
    hp_max = hp_now

    if money is None:
        money = randint(1,100)

    if not inventory:
        inventory = []



    return [
        name,
        hp_now,
        hp_max,
        lvl,
        xp_now,
        xp_next,
        attack,
        defence,
        luck,
        money,
        inventory,
    ]
p1 = make_hero(name="Вася_Бронированный")
p2 = make_hero(name="БОСС")
p3 = make_hero(name="Брыст")
print(p1)
print(p2)
print(p3)

p2[10].append