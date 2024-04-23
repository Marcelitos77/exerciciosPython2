import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def obter_valor():
    valor = int(input("Digite um valor: "))
    return valor

def main():
    dados_aluno(nome, ra, turma)
    valor = obter_valor()

    if valor < 0:
        valorPositivo = abs(valor)
        print(f"O valor é {valorPositivo}")
    elif valor > 10:
        novoValor = int(input(f"Valor inválido, digite um novo valor: "))
        valorFinal = valor - novoValor
        print(f"A diferença entre os valores é {valorFinal}")
    else:
        valorDividido = valor / 5
        print(f"O valor dividido é {valorDividido}")

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

main()

