inventory = []
print(id(inventory))
print(type(inventory))

print(inventory)

inventory.append("палица")
print(inventory)
print(id(inventory))

inventory.append("лук")
inventory.append("щит")
inventory.append("стрелы")
inventory.append("копье")
inventory.append("палица")
print(inventory)
print(id(inventory))

print(len(inventory))

inventory[0] = "конь"
print(inventory)
print(id(inventory))

inventory.pop(2)
print(inventory)
print(id(inventory))

inventory.sort()
print(inventory)
print(id(inventory))