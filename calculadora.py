# calculadora.py

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: divisão por zero!"
    return a / b

def main():
    print("Calculadora Simples")
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: entrada inválida. Digite apenas números.")
        return

    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Digite o número da operação desejada: ")

    if operacao == '1':
        resultado = soma(num1, num2)
        print(f"Resultado: {resultado}")
    elif operacao == '2':
        resultado = subtracao(num1, num2)
        print(f"Resultado: {resultado}")
    elif operacao == '3':
        resultado = multiplicacao(num1, num2)
        print(f"Resultado: {resultado}")
    elif operacao == '4':
        resultado = divisao(num1, num2)
        print(f"Resultado: {resultado}")
    else:
        print("Operação inválida.")

if __name__ == "__main__":
    main()
