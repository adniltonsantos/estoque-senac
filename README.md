# estoque-senac

PTI Gerenciamento de Estoque

## Estrutura de arquivos

O projeto agora está organizado em um pacote `produtos` que separado funcionalidades em módulos menores para facilitar a manutenção:

```text
README.md
main.py               # Programa principal que exibe o menu e chama as funções
produtos/             # pacote contendo operações sobre produtos
├── __init__.py       # reexporta as funções públicas
├── cadastro.py        # lógica de cadastro
├── listagem.py        # mostra produtos na tela
├── edicao.py          # edição de registros
├── deletar.py         # remoção de itens
└── calculos.py        # cálculos (total do estoque, etc.)
data.py               # dados iniciais do estoque (lista de dicionários)
utils.py              # funções utilitárias como formatação de moeda
```

## Como usar

Execute o script `main.py` com Python 3:

```sh
python3 main.py
```

O programa exibirá um menu interativo para cadastrar, listar, editar, excluir produtos e calcular o total em estoque.

