import math

def dados_aluno(nome, ra, turma):
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")

def media_notas(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media  

def main():
    nome = "Marcelo Siqueira Oliveira"
    ra = "1051392411006"
    turma = "Desenvolvimento de Software Multiplataforma"  
    dados_aluno(nome, ra, turma)

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = media_notas(nota1, nota2)

    if media >= 7:
        print(f"Sua média é: {media:.2f}. Você está aprovado.")
    else:
        print(f"Sua média é: {media:.2f}. Você ainda tem uma chance! Estude mais para o exame.")
        exame = float(input("Digite a nota do exame: "))
        nota_final = (media + exame) / 2

        if nota_final >= 5:
            print("Parabéns, você aproveitou a sua chance! Está aprovado.")
        else:
            print("Estude mais para a próxima. Você não alcançou o mínimo necessário.")

main()
