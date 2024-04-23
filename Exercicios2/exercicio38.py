import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def obter_valor():
    valor = float(input("Digite um valor: "))
    return valor

def main():
    dados_aluno(nome, ra, turma)
    valor = obter_valor()

    if valor % 10 == 0:
        print("O valor é divisível por 10")
    elif valor % 5 == 0:
        print("O valor é divisível por 5")
    elif valor % 2 == 0:
        print("O valor é divisível por 2")
    else:
        print("O valor não é divisível")

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

main()