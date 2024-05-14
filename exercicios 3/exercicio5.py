def calcular_media_conceito(nota1, nota2):
    media = (nota1 * 4 + nota2 * 6) / 10
    if media >= 9:
        conceito = "A"
        situacao = "APROVADO"
    elif media >= 7:
        conceito = "B"
        situacao = "APROVADO"
    elif media >= 3:
        conceito = "C"
        situacao = "EXAME"
    else:
        conceito = "D"
        situacao = "DP"
    return media, conceito, situacao

def imprimir_detalhes_aluno(nome_aluno, ra, turma, nome, media, conceito, situacao):
    print("\n")
    print(f"Aluno: {nome_aluno}, RA: {ra}, Turma: {turma}\n")
    print(f"A média do aluno {nome} é {media:.2f}, o conceito é {conceito} e a situação é {situacao}.")

def main():
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input("Digite a primeira nota do aluno (NP1): "))
    nota2 = float(input("Digite a segunda nota do aluno (NP2): "))

    media, conceito, situacao = calcular_media_conceito(nota1, nota2)

    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"

    imprimir_detalhes_aluno(nome_aluno, ra, turma, nome, media, conceito, situacao)

main()
