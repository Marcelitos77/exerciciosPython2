def calcular_imc(peso, sexo, altura):
    imc = peso / (altura ** 2)
    if sexo.upper() == 'F':
        if imc < 19:
            resultado = "abaixo do peso"
        elif imc <= 24:
            resultado = "no peso ideal"
        else:
            resultado = "acima do peso"
    else:
        if imc < 20:
            resultado = "abaixo do peso"
        elif imc <= 25:
            resultado = "no peso ideal"
        else:
            resultado = "acima do peso"
    return imc, resultado

def imprimir_detalhes_aluno(nome, ra, turma, imc, resultado):
    print("\n")
    print(f"Aluno: {nome}, RA: {ra}, Turma: {turma}\n")
    print(f"Seu IMC é {imc:.2f} e você está {resultado}.")

def main():
    peso = float(input("Digite seu peso em kg: "))
    sexo = input("Digite seu sexo (M para masculino, F para feminino): ")
    altura = float(input("Digite sua altura em cm: ")) / 100  

    imc, resultado = calcular_imc(peso, sexo, altura)

    nome_aluno = "Marcelo Siqueira Oliveira"
    ra = "105139241006"
    turma = "Desenvolvimento de Software Multiplataforma"

    imprimir_detalhes_aluno(nome_aluno, ra, turma, imc, resultado)

main()

