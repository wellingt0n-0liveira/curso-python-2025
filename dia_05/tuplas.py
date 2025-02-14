# %%

dados_teo = [32,1,"casado","dev golang"]
dados_teo
# %%
dados_teo = [32,1,"casado","dev golang"]

dados_teo.append("3241.43")
dados_teo
# %%
tupla_teo = 32,1,"casado","dev golang"
tupla_teo =(32,1,"casado","dev golang")

print(type(tupla_teo))
print(tupla_teo)

# %%
#tupla não comporta append, pq é imutavel
tupla_teo[-1].append("ana")