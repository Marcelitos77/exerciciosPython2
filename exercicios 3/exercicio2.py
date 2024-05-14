def calcular_fatorial(num):
    fatorial = 1
    for i in range(1, num + 1):
        fatorial *= i
    return fatorial

def imprimir_detalhes_aluno(nome, ra, turma, fatorial, num):
    print("\n")
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
    print(f"O fatorial de {num} é {fatorial}")

def main():
    num = int(input("Digite um número inteiro positivo: "))
    fatorial = calcular_fatorial(num)

    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"

    imprimir_detalhes_aluno(nome_aluno, ra, turma, fatorial, num)

main()
