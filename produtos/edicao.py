from data import estoque


def editar_produto():
    print("\n--- Editar Produto ---")
    try:
        codigo = int(input("Digite o código do produto que deseja editar: "))
        for p in estoque:
            if p['codigo'] == codigo:
                print(f"Editando: {p['nome']}")
                novo_nome = input("Novo nome (ou Enter para manter): ").strip()
                if novo_nome and not novo_nome.isdigit():
                    p['nome'] = novo_nome

                novo_preco = input("Novo preço (ou Enter para manter): ")
                if novo_preco:
                    p['preco'] = max(0.0, float(novo_preco))

                nova_qtd = input("Nova quantidade (ou Enter para manter): ")
                if nova_qtd:
                    p['quantidade'] = max(0, int(nova_qtd))

                print("Produto atualizado!")
                return
        print("Produto não encontrado.")
    except ValueError:
        print("Erro: Entrada inválida.")
