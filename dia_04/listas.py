# Listas são como molhos de chaves

# Uma maneira de definir 
# %%
idades = [28,42,43,35,39,28,38]
print = (idades)
# %%
teo =["teo","calvo",32,True,"casado",2342.98]

# %%
type(teo)

# %%

#idade
print(teo[2])

#renda
print(teo[5])

print(teo[0])

# %%

idades = [28,42,43,35,39,28,38,42,34]

print("soma das idades:",sum (idades))

print("qtde idades:", len(idades))

print("media idades:", sum(idades)/len(idades))

print("menor idade:", min(idades))

print("maior idades:", max(idades))

# %%

teo = ["teo calvo",32,
       True,"casado",
       ["Ana","maria","claudia"]]

print(len(teo))

teo[4][0]

exs = teo[4]
primeira_ex = exs[0]
print(primeira_ex)

# %%
teo = ["teo calvo",32,
       True,"casado",
       ["Ana","maria","claudia"]
       ["estag", "ds jr", "ds pl", "ds sr", "head"]]

tamanho = len(teo)
pos = tamanho -1

exs = teo[pos]

teo[pos][len(exs) - 1]

# %%

teo[-1][-1]
teo[-1][-2]
teo[-1][-3]

# %%

# primeiros 4 elementos
teo[0:4] # indicie +1


# %%
# duas ultimas posiçoes do teo

teo[4][3:5]

# %%

#colocando -2: estamos dizendo que queremos do elemento -2 ate o fim da lista, certo?
# duas ultimas posiçoes do teo
teo[4][-2:]

# %%

# primeiros 4 elementos
teo[:4] # indicie +1
# %%

#teo[start : stop]

# %%
teo = ["teo calvo",32,
       True,"casado",
       ["Ana","maria","claudia"]
       ["estag", "ds jr", "ds pl", "ds sr", "head"]]

salario = teo [5]
#salario = [:: - 1]

#teo[start : stop : step]