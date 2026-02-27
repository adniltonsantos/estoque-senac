# utils.py
# Funções utilitárias

def formatar_moeda(valor: float) -> str:
    """Formata um valor numérico como moeda brasileira (R$)."""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
