def perguntar():
    return input("O que deseja realizar?\n" +
    "<I> - Para inserir um usuário\n" +
    "<P> - Para inserir um usuário\n" +
    "<E> - Para inserir um usuário\n" +
    "<L> - Para inserir um usuário: ").upper()

def inserir(dicionario):
    dicionario[input("Digite o login: ").upper()] = [input("Digite o nome: ").upper(),
                                                    input("Digite a última data de acesso: "),
                                                    input("Qual a última estação acessada: ").upper()]