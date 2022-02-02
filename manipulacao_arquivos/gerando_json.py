import json

dicionario = {
    "Fulano": ["Fulano da Silva", "14/10/2021", "AT09"]
}

with open ("bd.json", "a") as json_file:
    json.dump(dicionario, json_file)