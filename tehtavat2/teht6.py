import random
kolme_koodi = ""
for _ in range(3):
 kolme_koodi = str(random.randint(0, 9))

nelja_koodi = ""
for _ in range(4):
 nelja_koodi = str(random.randint(1, 6))

print("Kolmenumeroisen lukon koodi:", kolme_koodi)
print("Nelinumeroisen lukon koodi:", nelja_koodi)

