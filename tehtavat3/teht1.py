
kuha_pituus = int(input("kerro kuhan pituus senttimetreinä"))

alamitta = 37

if kuha_pituus < alamitta:
    puuttuu = alamitta - kuha_pituus
    print(f"Kuha on alamittainen. Laske se takaisin järveen! Pituudesta puuttuu {puuttuu} cm.")

else:
    print("kuha sallittu pyyntimitaltaan. Voit pitää sen.")