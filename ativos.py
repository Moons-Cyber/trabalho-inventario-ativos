#Sistema de inventario de Segurança
from enum import Enum

#Definição da classe TipoAtivo que herda de Enum para representar os tipos de ativos disponíveis no sistema de inventário de segurança. Cada tipo de ativo é associado a um valor inteiro único.
class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    ESTACAO_TRABALHO = 4

ativos = {}

ativos[101] = {
    "nome": "Notebook Dell XPS 13",
    "tipo": TipoAtivo.NOTEBOOK,
    "setor": "TI",
    "responsavel": "João Silva",
    "vulnerabilidades":[]
}

while True:
    try:
        id_ativo = int(input("Digite o ID do ativo: "))
        if id_ativo in ativos:
            print("Esse ID já está cadastrado")
            continue

        break
    except ValueError:
        print("O ID deve ser um número inteiro.")