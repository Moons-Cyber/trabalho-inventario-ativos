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
def consultar_ativo():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))

            if id_ativo in ativos:
                print(f"Ativo encontrado {ativos[id_ativo]}")
                break
            else:
                print("Ativo não encontrado.")
        except ValueError:
            print("O ID deve ser um número inteiro!")
   

def menu_principal():
    while True:
        print("\n================================")
        print("   INVENTÁRIO DE CIBERSEGURANÇA")
        print("================================")
        print("\n1 - Cadastrar ativo")
        print("2 - Consultar ativo")
        print("3 - Atualizar ativo")
        print("4 - Remover ativo")
        print("5 - Cadastrar vulnerabilidade")
        print("6 - Consultar vulnerabilidades")
        print("7 - Sair")

        try:
            opcao = int(input("\nDigite uma opção: "))

            if opcao == 1:
                cadastrar_ativo()
            elif opcao == 2:
                consultar_ativo()
            elif opcao == 3:
                print("Função ainda não implementada")
            elif opcao == 4:
                print("Função ainda não implementada")
            elif opcao == 5:
                print("Função ainda não implementada")  
            elif opcao == 6:
                print("Função ainda não implementada")  
            elif opcao == 7:
                break
            else:
                print("Digite uma opção válida")
        except ValueError:
            print("Digite uma opção válida: ")
        



menu_principal()