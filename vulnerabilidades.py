from dados import ativos
from enums import Severidade, StatusTratamento
from persistencia import salvar_dados


def cadastrar_vulnerabilidade():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))

            if id_ativo not in ativos:
                print("Ativo não encontrado.")
                continue

            break
        except ValueError:
            print("O ID deve ser um número inteiro.")

    while True:
        descricao = input("Digite a descrição da vulnerabilidade: ")

        if descricao.strip() == "":
            print("A entrada não pode estar vazia!")
            continue
        break

    while True:
        categoria = input("Digite a categoria/tipo da vulnerabilidade: ")

        if categoria.strip() == "":
            print("A entrada não pode estar vazia!")
            continue
        break


    while True:
        try:
            print("\n---Menu Severidade---")
            print("1 - Baixa")
            print("2 - Média")
            print("3 - Alta")
            print("4 - Crítica")

            codigo_severidade = int(input("\nDigite a severidade da vulnerabilidade: "))

            severidade = Severidade(codigo_severidade)

            print(f"Severidade selecionada: {severidade.name}")
            break
        except ValueError:
            print("Severidade inválida!")

    while True:
        try:
            print("\n---Menu Status de Tratamento---")
            print("1 - Aberto")
            print("2 - Em tratamento")
            print("3 - Corrigido")
            print("4 - Aceita como risco")

            codigo_status = int(input("\nDigite o status de tratamento da vulnerabilidade: "))
            status = StatusTratamento(codigo_status)

            print(f"Status de tratamento selecionado: {status.name}")
            break
        except ValueError:
            print("Status de tratamento inválido!")


    vulnerabilidade = {
        "descricao": descricao,
        "categoria": categoria,
        "severidade": severidade,
        "status_tratamento": status
    }

    ativos[id_ativo]["vulnerabilidades"].append(vulnerabilidade)
    salvar_dados()
    print("Vulnerabilidade cadastrada com sucesso!")
    


    if severidade == Severidade.BAIXA:
        print("A vulnerabilidade é de baixa severidade. Nenhuma ação imediata é necessária.")
    elif severidade == Severidade.MEDIA:
        print("A vulnerabilidade é de severidade média. Recomenda-se monitoramento e avaliação de risco.")
    elif severidade == Severidade.ALTA:
        print("A vulnerabilidade é de alta severidade. Ações corretivas devem ser priorizadas.")
    elif severidade == Severidade.CRITICA:
        print("A vulnerabilidade é crítica. Ações corretivas imediatas são necessárias para mitigar o risco.")

def consultar_vulnerabilidade():
    while True:
        try:
            id_ativo = int(input("Digite o ID do ativo: "))

            if id_ativo not in ativos:
                print("Ativo não encontrado")
                continue

            break

        except ValueError:
            print("O ID deve ser um número inteiro!")
    
    vulnerabilidades = ativos[id_ativo]["vulnerabilidades"]

    if not vulnerabilidades:
        print("Esse ativo não possui vulnerabilidades registradas.")

    else:
        print("\n====== VULNERABILIDADES ======")

        for vulnerabilidade in vulnerabilidades:
            print("Descrição:", vulnerabilidade["descricao"])
            print("Categoria:", vulnerabilidade["categoria"])
            print("Severidade:", vulnerabilidade["severidade"].name)
            print("Status:", vulnerabilidade["status_tratamento"].name)
            print("-------------------------------------")
        