def adicionar_senha():
    senha = input("Digite a senha para adicionar: ")
    with open('senhas.txt', 'a') as arquivo:
        arquivo.write(senha + '\n')
    print(f"Senha adicionada com sucesso!")

def imprimir_informacoes_aluno():
    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"
    print(f"Aluno: {nome_aluno}, RA: {ra}, Turma: {turma}\n")

for _ in range(5):
    adicionar_senha()

imprimir_informacoes_aluno()
