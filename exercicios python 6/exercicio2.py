def adicionar_email():
    email = input("Digite o e-mail para adicionar: ")
    with open('emails.txt', 'a') as arquivo:
        arquivo.write(email + '\n')
    print(f"E-mail {email} adicionado com sucesso!")

def imprimir_informacoes_aluno():
    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"
    print(f"Aluno: {nome_aluno}, RA: {ra}, Turma: {turma}\n")

for _ in range(3):
    adicionar_email()

imprimir_informacoes_aluno()