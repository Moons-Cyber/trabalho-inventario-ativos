#Sistema de inventario de Segurança
from enum import Enum

#Definição da classe TipoAtivo que herda de Enum para representar os tipos de ativos disponíveis no sistema de inventário de segurança. Cada tipo de ativo é associado a um valor inteiro único.
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    ESTACAO_TRABALHO = 4

ativos = {}


def cadastrar_ativo():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))
            if id_ativo in ativos:
                print("Esse ID já está cadastrado")
                continue

            break
        except ValueError:
            print("O ID deve ser um número inteiro.")


    while True: 
        nome = input("Digite o nome ou hostname do ativo: ")

        if nome.strip() == "":
            print("A entrada não pode estar vazia!")
            continue
        break

    while True:
        responsavel = input("Digite o responsável pelo ativo: ")

        if responsavel.strip() == "":
            print("A entrada não pode estar vazia!")
            continue
        break


    while True:
        setor = input("Digite o nome do setor/localização do ativo: ")
        if setor.strip() == "":
            print("A entrada não pode estar vazia!")
            continue
        break


    while True:
        try:
            print("\n---Menu Ativos TI---")
            print("1 - Notebook")
            print("2 - Servidor")
            print("3 - Roteador")
            print("4 - Estação de trabalho")

            codigo_tipo = int(input("\nDigite o tipo do ativo: "))

            tipo_ativo = TipoAtivo(codigo_tipo)

            print(f"Tipo selecionado: {tipo_ativo}")
            break
        except ValueError:
            print("Tipo ativo inválido!")

        
    ativos[id_ativo] = {
        "nome": nome,
        "tipo_ativo": tipo_ativo,
        "setor": setor,
        "responsavel": responsavel,
        "vulnerabilidades": []

    }

    print("\nAtivo cadastrado com sucesso!")
    print(ativos)


cadastrar_ativo()