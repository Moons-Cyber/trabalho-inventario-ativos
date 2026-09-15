#Sistema de inventario de Segurança
from enum import Enum

class TipoAtivo(Enum):
    NOTEBOOK = 1
    SERVIDOR = 2
    ROTEADOR = 3
    ESTACAO_TRABALHO = 4


print(TipoAtivo.NOTEBOOK.value)