import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def valor_salario():
    valorSalario = float(input("Digite o valor do salário: "))
    return valorSalario

def main():
    dados_aluno(nome, ra, turma)
    valorSalario = valor_salario()

    if valorSalario <= 1500:
        valorComAcrescimo = valorSalario * 1.2
        print(f"O valor do salário com acrescimo é R$ {valorComAcrescimo:.2f}")
    elif valorSalario > 1500 or valorSalario <= 2500:
        valorComAcrescimo = valorSalario * 1.1
        print(f"O valor do salário com acrescimo é R$ {valorComAcrescimo:.2f}")
    else:
        valorComAcrescimo = valorSalario * 1.05
        print(f"O valor do salário com acrescimo é R$ {valorComAcrescimo:.2f}")

nome = "Marcelo Siqueira Oliveira"
ra = "1051392411006"
turma = "Desenvolvimento de Software Multiplataforma"

main()
