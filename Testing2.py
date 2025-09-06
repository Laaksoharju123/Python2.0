nimi = input("kerro nimesi:")
if nimi == "Matti":
    try:
        maara = int(input("Montako keittoannosta? "))
        hinta = 5.90
        kokonaishinta = maara * hinta
        print(f"Kokonaishinta on {kokonaishinta:.2f}")
    except ValueError:
        print("Virheellinen syöte. Anna annosten määrä numerona.")
    else:
        print("seuraava, kiitos!")



