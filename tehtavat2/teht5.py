#kysytään käyttäjältä kolmea arvoa
leiviskat = float(input("anna leiviskät"))
naulat = float(input("anna naulat"))
luodit = float(input("anna luodit"))
luodit_yhteensa = leiviskat * 20 * 32 + naulat * 32 + luodit
grammat = luodit_yhteensa * 13.3
kilogrammat = int(grammat // 1000)
jaannos_grammat = (grammat % 1000)
print(f"Massa nykymittojen mukaan on {kilogrammat} kilogrammaa ja {jaannos_grammat:.2f} grammaa.")