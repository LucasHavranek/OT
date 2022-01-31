from dicionarios.funcoes import *

usuarios = {}

usuarios = {
    "chaves": ["Chaves do 8", "20/12/2021", "REC01"],
    "quico": ["Quico", "20/12/2021", "ENF02"]
}

usuarios["Florinda"] = ["Dona Florinda", "21/12/2021", "AUD01"]
print(usuarios)
print(usuarios.get("quico"))