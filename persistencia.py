import json

from dados import ativos
from enums import TipoAtivo, Severidade, StatusTratamento

def preparar_dados():
    dados = {}

    for id_ativo, ativo in ativos.items():
        vulnerabilidades = []


        for vulnerabilidade in ativo["vulnerabilidades"]:
            vulnerabilidades.append({
                "descricao": vulnerabilidade["descricao"],
                "categoria": vulnerabilidade["categoria"],
                "severidade": vulnerabilidade["severidade"].value,
                "status_tratamento": vulnerabilidade["status_tratamento"].value

            })

        dados[id_ativo] = {
            "nome": ativo["nome"],
            "tipo_ativo": ativo["tipo_ativo"].value,
            "setor": ativo["setor"],
            "responsavel": ativo["responsavel"],
            "vulnerabilidades": vulnerabilidades
        }

    return dados

def salvar_dados():
    dados = preparar_dados()
    with open("ativos.json", "w", encoding="utf-8") as arquivos:
        json.dump(dados, arquivos, indent=4)

def carregar_dados():
    try:
        with open("ativos.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)

    except FileNotFoundError:
        return

    for id_ativo, ativo in dados.items():
        vulnerabilidades = []

        for vulnerabilidade in ativo["vulnerabilidades"]:
            vulnerabilidades.append({
                "descricao": vulnerabilidade["descricao"],
                "categoria": vulnerabilidade["categoria"],
                "severidade": Severidade(vulnerabilidade["severidade"]),
                "status_tratamento": StatusTratamento(vulnerabilidade["status_tratamento"])
            })

        ativos[int(id_ativo)] = {
            "nome": ativo["nome"],
            "tipo_ativo": TipoAtivo(ativo["tipo_ativo"]),
            "setor": ativo["setor"],
            "responsavel": ativo["responsavel"],
            "vulnerabilidades": vulnerabilidades
        }