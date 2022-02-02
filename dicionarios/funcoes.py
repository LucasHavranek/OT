import os.path

save_path = './dicionarios/'
file_name = 'bd.txt'
complete_directory = os.path.join(save_path, file_name)


def perguntar():
    return input("O que deseja realizar?\n" +
                 "<I> - Para inserir um usuário\n" +
                 "<P> - Para pesquisar um usuário\n" +
                 "<E> - Para editar um usuário\n" +
                 "<L> - Para listar um usuário: ").upper()


def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper()]
    salvar(dicionario)


def salvar(dicionario):
    with open(complete_directory, "a") as arquivo:
        for chave, valor in dicionario.items():
            arquivo.write(chave + ":" + str(valor))
