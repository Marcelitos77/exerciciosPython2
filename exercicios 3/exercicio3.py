def calcular_maior_nota():
    maior_nota = 0
    contador = 0
    while contador < 5:
        nota = float(input(f"Digite a nota do aluno {contador + 1}: "))
        if nota > maior_nota:
            maior_nota = nota
        contador += 1
    return maior_nota

def imprimir_detalhes_aluno(nome, ra, turma, maior_nota):
    print("\n")
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
    print(f"A maior nota da turma é {maior_nota}")

def main():
    maior_nota = calcular_maior_nota()

    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"

    imprimir_detalhes_aluno(nome_aluno, ra, turma, maior_nota)

main()
