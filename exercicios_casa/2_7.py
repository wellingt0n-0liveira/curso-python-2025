#Solicite ao usuário o nome de uma fruta
# e exiba o preço correspondente.


fruta = input("Entre com o nome da fruta: ")

frutas = {
     "Maçã": "R$1,50"
    "Banana":"2.55"
    "Banana": "R$2,75"
    "Uva": "R$1,90"
    "Pera": "R$1,25"
    "Laranja": "R$0,65"
    "Limão": "R$1,25"
}

if fruta in frutas:
    print(frutas[fruta])
else:
    print("Entre com um valor valido!")
