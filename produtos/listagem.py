from data import estoque
from utils import formatar_moeda


def listar_produtos():
    print("\n" + "=" * 65)
    print(f"{'CÓDIGO':<10} | {'NOME':<20} | {'PREÇO':<15} | {'QTD':<8}")
    print("-" * 65)
    if not estoque:
        print("Estoque vazio.")
    for p in estoque:
        print(
            f"{p['codigo']:<10} | {p['nome']:<20} | {formatar_moeda(p['preco']):<15} | {p['quantidade']:<8}"
        )
    print("=" * 65)
