from enum import Enum


class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    ESTACAO_TRABALHO = 4


class Severidade(Enum):
    BAIXA = 1
    MEDIA = 2
    ALTA = 3
    CRITICA = 4


class StatusTratamento(Enum):
    ABERTO = 1
    EM_TRATAMENTO = 2
    CORRIGIDO = 3
    ACEITA_COMO_RISCO = 4