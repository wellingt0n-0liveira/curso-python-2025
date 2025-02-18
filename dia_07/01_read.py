# %%

nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()

print(conteudo)

# abre arquivo em formato de leituta
open_file = open(nome_arquivo)

# le os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# fecha o arquivo
open_file.close()
