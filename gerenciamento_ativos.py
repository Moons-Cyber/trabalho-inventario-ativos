from dados import ativos
from enums import TipoAtivo
from persistencia import salvar_dados


def cadastrar_ativo():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))
            # O ID é usado como chave do dicionário, por isso não pode ser duplicado.
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
            
            # Converte o código informado pelo usuário em um membro do Enum.
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

    salvar_dados()

    print("Ativo cadastrado com sucesso!")
        
def consultar_ativo():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))

            if id_ativo in ativos:
                print("\n======ATIVO ENCONTRADO======")
                print("ID:", id_ativo)
                print("Nome:", ativos[id_ativo]["nome"])
                print("Tipo:", ativos[id_ativo]["tipo_ativo"].name)
                print("Setor:", ativos[id_ativo]["setor"])
                print("Responsável:", ativos[id_ativo]["responsavel"])
                print("Vulnerabilidades:", ativos[id_ativo]["vulnerabilidades"])
                break                    
            else:
                print("Ativo não encontrado.")
        except ValueError:
            print("O ID deve ser um número inteiro!")

def consultar_por_nome():
    nome_busca = input("Digite o nome ou hostname do ativo: ")
    encontrado = False 

    for id_ativo, ativo in ativos.items():
        if ativo["nome"].lower() == nome_busca.lower():
            print("\n======ATIVO ENCONTRADO======")
            print("ID:", id_ativo)
            print("Nome:", ativo["nome"])
            print("Tipo:", ativo["tipo_ativo"].name)
            print("Setor:", ativo["setor"])
            print("Responsável:", ativo["responsavel"])
            print("Vulnerabilidades:", ativo["vulnerabilidades"])
            encontrado = True
            break
    if not encontrado:
        print("Ativo não encontrado.")
        
def atualizar_ativo():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo que deseja atualizar: "))

            if id_ativo not in ativos:
                print("Ativo não encontrado.")
                continue

            ativo = ativos[id_ativo]

            while True:
                print("\n====== ATUALIZAR ATIVO ======")
                print("1 - Atualizar nome/hostname")
                print("2 - Atualizar tipo de ativo")
                print("3 - Atualizar setor/localização")
                print("4 - Atualizar responsável")
                print("5 - Voltar ao menu principal")

                try:
                    sub_opcao = int(input("\nDigite uma opção: "))
                except ValueError:
                    print("Digite uma opção válida.")
                    continue

                if sub_opcao == 1:
                    novo_nome = input("Digite o novo nome/hostname do ativo: ")

                    if novo_nome.strip() == "":
                        print("A entrada não pode estar vazia!")
                        continue

                    ativo["nome"] = novo_nome
                    salvar_dados()
                    print("Nome/hostname atualizado com sucesso!")

                elif sub_opcao == 2:
                    while True:
                        try:
                            print("\n--- Menu Ativos TI ---")
                            print("1 - Notebook")
                            print("2 - Servidor")
                            print("3 - Roteador")
                            print("4 - Estação de trabalho")

                            codigo_tipo = int(input("\nDigite o novo tipo do ativo: "))

                            tipo_ativo = TipoAtivo(codigo_tipo)

                            ativo["tipo_ativo"] = tipo_ativo
                            salvar_dados()
                            print("Tipo atualizado com sucesso!")
                            break

                        except ValueError:
                            print("Tipo de ativo inválido!")

                elif sub_opcao == 3:
                    novo_setor = input("Digite o novo setor/localização do ativo: ")

                    if novo_setor.strip() == "":
                        print("A entrada não pode estar vazia!")
                        continue

                    ativo["setor"] = novo_setor
                    salvar_dados()
                    print("Setor/localização atualizado com sucesso!")

                elif sub_opcao == 4:
                    novo_responsavel = input( "Digite o novo responsável pelo ativo: ")

                    if novo_responsavel.strip() == "":
                        print("A entrada não pode estar vazia!")
                        continue

                    ativo["responsavel"] = novo_responsavel
                    salvar_dados()
                    print("Responsável atualizado com sucesso!")

                elif sub_opcao == 5:
                    return  # Voltar ao menu principal

                else:
                    print("Digite uma opção válida.")

        except ValueError:
            print("O ID deve ser um número inteiro.")        

def remover_ativo():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo que deseja remover: "))

            if id_ativo not in ativos:
                print("Ativo não encontrado.")
                continue

            while True:
                confirmacao = input(f"Tem certeza que deseja remover o ativo {ativos[id_ativo]['nome']}? (s/n): ").strip().lower()

                if confirmacao == 's':
                    del ativos[id_ativo]
                    salvar_dados()
                    print("Ativo removido com sucesso!")
                    return  

                elif confirmacao == 'n':
                    print("Remoção cancelada.")
                    return

                else:
                    print("Opção inválida. Digite 's' para sim ou 'n' para não.")


        except ValueError:
            print("O ID deve ser um número inteiro.")  