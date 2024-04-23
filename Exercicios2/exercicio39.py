import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def calcular_cubo(valor):
    return valor ** 3

def calcular_fatorial(valor):
    fatorial = 1
    for i in range(1, valor + 1):
        fatorial *= i
    return fatorial

def calcular_divisao_por_nove(valor):
    return valor / 9

def main():
    nome = "Marcelo Siqueira Oliveira"
    ra = "1051392411006"
    turma = "Desenvolvimento de Software Multiplataforma"

    valor = int(input("Digite um valor: "))
    dados_aluno(nome, ra, turma)

    if valor == 1 or valor == 2:
        resultado = calcular_cubo(valor)
        print(f"O valor elevado ao cubo é: {resultado}")
    elif valor % 3 == 0:
        resultado = calcular_fatorial(valor)
        print(f"O fatorial de {valor} é: {resultado}")
    else:
        print("Valor inválido.")

main()