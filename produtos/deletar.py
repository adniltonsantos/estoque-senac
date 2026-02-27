from data import estoque


def deletar_produto():
    print("\n--- Deletar Produto ---")
    try:
        codigo = int(input("Digite o código do produto para excluir: "))
        for i, p in enumerate(estoque):
            if p['codigo'] == codigo:
                confirmar = input(f"Tem certeza que deseja excluir {p['nome']}? (s/n): ")
                if confirmar.lower() == 's':
                    estoque.pop(i)
                    print("Produto removido!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Erro: Código inválido.")
