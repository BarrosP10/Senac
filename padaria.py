# padaria.py

def main():
    print("=== Sistema de Pedidos da Padaria ===")

    # Leitura dos dados do cliente
    nome_cliente = input("Digite o nome do cliente: ")

    # Leitura dos dados do produto
    nome_produto = input("Digite o nome do produto: ")
    
    try:
        preco = float(input("Digite o preço do produto (em R$): "))
        quantidade = int(input("Digite a quantidade desejada: "))
    except ValueError:
        print("Erro: Preço deve ser um número e quantidade deve ser um inteiro.")
        return

    # Cálculo do valor total
    total = preco * quantidade

    # Exibição dos dados do pedido
    print("\n=== Resumo do Pedido ===")
    print(f"Cliente: {nome_cliente}")
    print(f"Produto: {nome_produto}")
    print(f"Preço unitário: R$ {preco:.2f}")
    print(f"Quantidade: {quantidade}")
    print(f"Total a pagar: R$ {total:.2f}")

if __name__ == "__main__":
    main()
