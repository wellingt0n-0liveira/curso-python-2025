# %%
import requests
import json

ceps = ["01519000",
        "13329120",
        "21870370",
        "13600110",  
        ]

url = "https://viacep.com.br/ws/{ceps}/json/"
dados = []
for i in tqdm(ceps):
    resposta = requests.get(url.format(cep=i))
    if resposta.status_code == 200:
        dados.append(resposta.json())
dados

# %%

#print(dados)

with open("ceps.json", "w", encoding='utf-8') as open_file:
    json.dump(dados, open_file, ensure_ascii=False, indent=4)


# resposta = requests.get(url)
# dados =resposta.json()
# dados