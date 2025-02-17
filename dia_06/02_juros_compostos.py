# %%

def juros_compostos(aporte:int, taxa:float, anos:int)
    """"juros_compostos serve para calcular o retono financeiro a partir

        aporte:
    um numero inteiro, que represente o valor em R$

    taxa:
        um numero float entre 0 e 1 que represente o valor taxa de juros

   anos:
        um numero inteiro >= 1 que representa o tempo que o investimento tem que aguardar


    """
    return aporte * (1 + taxa) ** anos
# %%

juros_compostos(aporte=100, taxa=0.13, anos=4)
