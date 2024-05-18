def tamanho_variavel():
    with open('mensagens.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    return len(conteudo)

def lista_palavras():
    with open('mensagens.txt', 'r') as arquivo:
        conteudo = arquivo.read()
    palavras = conteudo.split()
    return palavras

def imprimir_informacoes_aluno():
    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"
    print(f"Aluno: {nome_aluno}, RA: {ra}, Turma: {turma}\n")

print(f"Tamanho da variável: {tamanho_variavel()}")
print(f"Lista de palavras: {lista_palavras()}")


imprimir_informacoes_aluno()