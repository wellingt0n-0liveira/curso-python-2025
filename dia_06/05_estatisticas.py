
# def soma(a:float, b:float)->float:
#     return a + b

# def media(a:float, b:float)->float:
#     return soma(a,b) / 2

# a = float(input("Entre com o valor de a: "))
# b = float(input("Entre com o valor de b: "))

# print("Media:", media(a,b))

# -------------------------------------------------

def soma(a:float, b:float, *args)->float:
    valores = [a,b] + list(args)
    return sum(valores)

def media(a:float, b:float, *args)->float:
    return soma(a,b,*args) / (len(args)+2)

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de b: "))
d = float(input("Entre com o valor de b: "))

print("Media:", media(a,b,c,d))