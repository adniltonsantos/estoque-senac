from data import estoque


def cadastrar_produto():
    print("\n--- Cadastro de Novo Produto ---")
    while True:
        try:
            codigo = int(input("Digite o código do produto: "))
            if any(p['codigo'] == codigo for p in estoque):
                print("Erro: Este código já está cadastrado.")
                continue
            break
        except ValueError:
            print("Erro: O código deve ser um número inteiro.")
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if not nome or nome.isdigit():
            print("Erro: Nome inválido (não pode ser vazio ou apenas números).")
            continue
        break
    while True:
        try:
            preco = float(input("Digite o preço: "))
            if preco < 0:
                print("Erro: O preço não pode ser negativo.")
                continue
            break
        except ValueError:
            print("Erro: Valor numérico inválido.")
    while True:
        try:
            quantidade = int(input("Digite a quantidade: "))
            if quantidade < 0:
                print("Erro: A quantidade não pode ser negativa.")
                continue
            break
        except ValueError:
            print("Erro: Valor numérico inválido.")
    novo_produto = {
        "codigo": codigo,
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
    }
    estoque.append(novo_produto)
    print(f"\n Produto '{nome}' cadastrado com sucesso!")
