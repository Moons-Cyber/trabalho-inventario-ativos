# Inventário de Cibersegurança

Sistema de inventário de ativos de tecnologia desenvolvido em Python para a disciplina de Cibersegurança da UFU. O sistema permite cadastrar, consultar, atualizar e remover ativos, além de registrar e consultar vulnerabilidades associadas a cada ativo.

## Funcionalidades

- Cadastro de ativos de tecnologia com:
  - ID único
  - Nome ou hostname
  - Responsável
  - Setor ou localização
  - Tipo do ativo

- Consulta de ativos por:
  - ID
  - Nome ou hostname
 
- Atualização dos dados dos ativos.

- Remoção de ativos com confirmação.

- Cadastro de vulnerabilidades associadas aos ativos, contendo:
  - Descrição
  - Categoria/tipo
  - Severidade
  - Status de tratamento

- Consulta das vulnerabilidades associadas a cada ativo.

- Validação das entradas fornecidas pelo usuário.

- Persistência dos dados em arquivo JSON.

- Uso de `Enum` para representar tipos de ativos, níveis de severidade e status de tratamento.

## Tecnologias utilizadas 

- **Pyhton** — Linguagem utilizada no desenvolvimento do sistema.
- **JSON** — Formato utilizado para persistência de dados.
- **Git** — Controle de versão do projeto.
- **GitHub** — Hospedagem do repositório e gerenciamento das branches.

## Estrutura do projeto

```text
.
├── ativos.py
├── dados.py
├── enums.py
├── gerenciamento_ativos.py
├── menu.py
├── persistencia.py
├── vulnerabilidades.py
├── ativos.json
└── .gitignore
```

## Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/Moons-Cyber/trabalho-inventario-ativos.git
```
### 2. Acesse a pasta do projeto

```bash
cd trabalho-inventario-ativos
```

### 3. Execute o sistema

```bash
python ativos.py
```

## Persistência dos dados

Os dados dos ativos e suas vulnerabilidades são armazenados no arquivo `ativos.json`.

O sistema utiliza o módulo `persistencia.py` para:

- Salvar os dados no arquivo JSON após alterações no sistema.
- Carregar os dados do arquivo JSON ao iniciar a aplicação.
- Converter os valores armazenados no JSON novamente para os respectivos `Enum` utilizados pelo sistema.

Dessa forma, os dados não ficam disponíveis apenas durante a execução do programa, sendo mantidos entre diferentes execuções.


## Organização do código

O projeto foi dividido em diferentes módulos para separar as responsabilidades do sistema.

- **`ativos.py`** — inicia a aplicação, carregando os dados e executando o menu principal.
- **`dados.py`** — mantém o dicionário utilizado para armazenar os ativos durante a execução.
- **`enums.py`** — concentra os `Enum` utilizados para representar tipos de ativos, severidade e status de tratamento.
- **`gerenciamento_ativos.py`** — reúne as operações de cadastro, consulta, atualização e remoção de ativos.
- **`menu.py`** — controla a interação do usuário com o sistema por meio dos menus.
- **`vulnerabilidades.py`** — reúne as operações relacionadas às vulnerabilidades dos ativos.
- **`persistencia.py`** — realiza o salvamento e carregamento dos dados no arquivo JSON.
- **`ativos.json`** — arquivo utilizado para persistência dos dados.
- **`.gitignore`** — define arquivos e diretórios que não devem ser versionados.

Essa organização permite separar as responsabilidades do sistema, facilitando a manutenção e a compreensão do código.

## Controle de versão

O projeto utiliza Git para controle de versão e GitHub para hospedagem do repositório.

Durante o desenvolvimento, foram utilizadas branches para organizar as funcionalidades do sistema, incluindo:

- `feature/tipos-ativos`
- `feature/cadastro-ativos`
- `feature/vulnerabilidades`

Após o desenvolvimento das funcionalidades, as alterações foram integradas à branch `main` por meio de merge.

## Validação de entradas

O sistema realiza validações para evitar entradas inválidas durante a utilização.

Entre as validações implementadas estão:

- Verificação de IDs inteiros.
- Impedimento de cadastro de IDs duplicados.
- Verificação de campos obrigatórios vazios.
- Validação dos códigos dos tipos de ativos.
- Validação dos níveis de severidade das vulnerabilidades.
- Validação dos status de tratamento.
- Tratamento de entradas inválidas nos menus.
- Confirmação antes da remoção de um ativo.

## Objetivo acadêmico

Este projeto foi desenvolvido como atividade avaliativa da disciplina de Cibersegurança da Universidade Federal de Uberlândia (UFU).

O objetivo é aplicar conceitos de programação, estruturas de dados, controle de versão e gerenciamento de ativos e vulnerabilidades em um sistema desenvolvido em Python.

