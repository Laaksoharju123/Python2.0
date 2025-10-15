#kysytään käyttäjältä

luku = int(input("kerro kokonaisluku:"))

if luku <= 1:
    print(f"{luku} ei ole alkuluku")
else:
    on_alkuluku=True

for i in range(2,luku):
    if luku % i ==0:
     on_alkuluku = False
     break

if on_alkuluku and luku >1:
    print(f"{luku} on alkuluku!")
else:
    print(f"{luku} ei ole alkuluku!")

