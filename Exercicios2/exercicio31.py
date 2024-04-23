import math

def dados_aluno():
    nome = "Marcelo Siqueira Oliveira"
    ra = "1051392411006"
    turma = "Desenvolvimento de Software Multiplataforma"
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def calcular_quadrado(valor):
    resultado = valor ** 2
    print(f"O valor elevado ao quadrado é: {resultado:.2f}")

def calcular_raiz_quadrada(valor):
    resultado = math.sqrt(valor)
    print(f"A raiz quadrada do valor é: {resultado:.2f}")

def calcular_divisao_por_nove(valor):
    resultado = valor / 9
    print(f"O valor dividido por 9 é: {resultado:.2f}")

def main():
    dados_aluno()
    
    valor = int(input("Digite um valor inteiro: "))
    print("")

    if valor >= 1 and valor <= 3:
        calcular_quadrado(valor)
    elif valor >= 4 and valor <= 5:
        calcular_raiz_quadrada(valor)
    elif valor >= 6 and valor <= 9:
        calcular_divisao_por_nove(valor)
    else:
        print("Valor fora das condições especificadas.")

main()

