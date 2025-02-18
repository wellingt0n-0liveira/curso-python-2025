# Construa um programa que realiza o sorteio de um número entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute e maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns.

numero_sorteio = 7


for i in range(3):

    while True:
            try:
              numero_usuario = int(input("Entre com o numero: "))

            except ValueError as err:
                  print("valor invalido")
                  continue 
            if not 1 <= numero_usuario <= 15:
                break
            print("Valor deve ser entre u  e 15")

            if numero_sorteio == numero_usuario:
                print("Parabens")
                break

            elif numero_usuario > numero_sorteio:
                print ("numero muito alto. Tente um numero menor")

            else:
                print("Numero muito baixo. tente um maior")    
else:
    print("Suas tentaivas acabaram")