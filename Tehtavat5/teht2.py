lista = []
#kysytään käyttäjältä lukuja
lukuja = (input("anna lukuja:"))

while lukuja != "":
    lista.append(lukuja)
    lukuja = (input("anna lukuja:"))

lista.sort(reverse=True)
print(lista [0:5])