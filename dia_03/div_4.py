# %%

# Quais numeros são divisiveis por entre 4 e 100?

count = 4
while count <=100:
    resto = count % 4
    if resto == 0:
        print(count)

    count += 1    
