luku = int(input("mikä on kokonaisluku"))
if luku % 3 == 0:
    print("BOOM!")
elif luku % 5 == 0:
    print("BUZZ!")
elif luku % 3 == 0 and luku % 5 == 0:
    print("BOOMBUZZ")
else:
    print("vituiks meni")
#järjestys vituillaan, eli ensin tuo missä kysytään molempia koska ohjelma tekee sen ensin