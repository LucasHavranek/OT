import json
import os.path

save_path = './manipulacao_arquivos/'
file_name = 'bd.json'
complete_directory = os.path.join(save_path, file_name)

dicionario = {
    "Fulano": ["Fulano da Silva", "14/10/2021", "AT09"]
}

with open (complete_directory, "a") as json_file:
    json.dump(dicionario, json_file)