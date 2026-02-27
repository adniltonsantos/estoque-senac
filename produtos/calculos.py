from data import estoque


def calcular_total_estoque():
    total = sum(produto['quantidade'] for produto in estoque)
    print(f"\n Quantidade total de itens no estoque: {total}")
