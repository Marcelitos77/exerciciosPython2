import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def compra():
    valorDaCompra = float(input("Digite o valor da compra: "))
    return valorDaCompra

def main():
    dados_aluno(nome, ra, turma)
    valorDaCompra = compra()

    if valorDaCompra >= 300:
        valorComDesconto = valorDaCompra * 0.8
        print(f"O valor a ser pago com desconto é R$ {valorComDesconto:.2f}")
    elif valorDaCompra >= 200 and valorDaCompra < 300:
        valorComDesconto = valorDaCompra * 0.9
        print(f"O valor a ser pago com desconto é R$ {valorComDesconto:.2f}")
    else:
        valorComDesconto = valorDaCompra * 0.95
        print(f"O valor a ser pago com desconto é R$ {valorComDesconto:.2f}")

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

main()


