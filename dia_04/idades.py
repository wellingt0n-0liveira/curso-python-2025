
# %%

idades = []

while True:
    idade = input("entre com idade: ")

    if idade == "":
        break

    idades.append(int(idade))



media = sum(idades) / len (idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print(media)
print(minimo)
print(maximo)
print(qtde)