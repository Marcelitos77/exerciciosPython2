import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def verificar_idade(nome1, idade):
    if idade < 18:
        print(f"Bem vindo {nome1}, você é menor de idade.")
    elif idade < 65:
        print(f"Bem vindo {nome1}, você é maior de idade.")
    else:
        print(f"Bem vindo {nome1}, você é maior de 65 anos.")

def main():
    nome = "Marcelo Siqueira Oliveira"
    ra = "1051392411006"
    turma = "Desenvolvimento de Software Multiplataforma"

    nome1 = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    verificar_idade(nome1, idade)
    dados_aluno(nome, ra, turma)
    

main()