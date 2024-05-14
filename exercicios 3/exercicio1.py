def calcular_aumento(salario):
    if salario <= 1500:
        aumento = salario * 0.20
    elif salario > 1500 and salario < 2500:
        aumento = salario * 0.10
    else:
        aumento = salario * 0.05
    return salario + aumento

def imprimir_detalhes_aluno(nome, ra, turma, novo_salario):
    print("\n")
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
    print(f"Olá {nome}, seu novo salário com aumento é: R${novo_salario:.2f}")

def main():
    nome = input("Digite seu nome: ")
    salario = float(input("Digite seu salário: "))
    novo_salario = calcular_aumento(salario)

    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"

    imprimir_detalhes_aluno(nome_aluno, ra, turma, novo_salario)

main()
