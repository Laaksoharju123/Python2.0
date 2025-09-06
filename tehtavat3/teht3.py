
sukupuoli = input("kerro sukupuolesi(mies/nainen):")
hemoglobiini = int(input(" kerro hemoglobiini arvosi(g/l)"))

if sukupuoli.lower() == "nainen":
    if hemoglobiini < 117:
        print("hemoglobiini on alhainen")
    elif hemoglobiini <= 175:
        print("hemoglobiini on normaali")
    else:
        print("hemoblobiini on korkea")

if sukupuoli.lower() == "mies":
    if hemoglobiini < 134:
        print("hemoglobiini on alhainen")
    elif hemoglobiini <= 195:
        print("hemoglobiini on normaali")
    else:
        print("hemoblobiini on korkea")