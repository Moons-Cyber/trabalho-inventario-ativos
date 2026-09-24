from gerenciamento_ativos import (
    cadastrar_ativo,
    consultar_ativo,
    consultar_por_nome,
    atualizar_ativo,
    remover_ativo
)

from vulnerabilidades import (
    cadastrar_vulnerabilidade,
    consultar_vulnerabilidade
)





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
                while True:
                    print("\n---Menu Consulta Ativos---")
                    print("\n1 - Consultar por ID")
                    print("2 - Consultar por nome/hostname")
                    print("3 - Voltar ao menu principal")

                    try:
                        sub_opcao = int(input("\nDigite uma opção: "))

                        if sub_opcao == 1:
                            consultar_ativo()
                        elif sub_opcao == 2:
                            consultar_por_nome()
                        elif sub_opcao == 3:
                            break
                        else:
                            print("Digite uma opção válida")
                    except ValueError:
                        print("Digite uma opção válida: ")

            elif opcao == 3:
                atualizar_ativo()

            elif opcao == 4:
                remover_ativo()

            elif opcao == 5:
                cadastrar_vulnerabilidade()

            elif opcao == 6:
                consultar_vulnerabilidade()  

            elif opcao == 7:
                break
            else:
                print("Digite uma opção válida")
        except ValueError:
            print("Digite uma opção válida: ")