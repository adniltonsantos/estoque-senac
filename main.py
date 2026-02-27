# main.py
# Ponto de entrada do sistema de estoque.

from produtos import (
    cadastrar_produto,
    listar_produtos,
    editar_produto,
    deletar_produto,
    calcular_total_estoque,
)


def menu():
    while True:
        print("\nSISTEMA DE ESTOQUE - SENAC")
        print("1. Cadastrar Produto")
        print("2. Listar Produtos")
        print("3. Editar Produto")
        print("4. Deletar Produto")
        print("5. Calcular Total no Estoque")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            editar_produto()
        elif opcao == '4':
            deletar_produto()
        elif opcao == '5':
            calcular_total_estoque()
        elif opcao == '0':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    menu()
