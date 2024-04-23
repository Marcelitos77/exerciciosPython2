import math

def dados_aluno():
    nome = "Marcelo Siqueira Oliveira"
    ra = "1051392411006"
    turma = "Desenvolvimento de Software Multiplataforma"
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")


def media_notas(nota1, nota2):
        media = (nota1 + nota2) / 2
        return media
    
def main():
    dados_aluno()

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))


media = media_notas(nota1, nota2)

if media >= 7:
    print(f"A sua média é: {media:.2f} você está aprovado")
else:
    print(f"A sua média é: {media:.2f}, Você  ainda  tem  uma  chance!  Estude  mais  para  o exame.")

main()


