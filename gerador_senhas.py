import random
import string

def escolher_opcao(mensagem):
    while True:
        opcao = input(mensagem).lower()
        if opcao in ['s', 'n']:
            return opcao
        print("ERRO = Digite 's' para sim ou 'n' para não.")

def gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos):
    todos_caracteres = []
    if usar_minuscula:
        todos_caracteres += list(string.ascii_lowercase)
    if usar_maiuscula:
        todos_caracteres += list(string.ascii_uppercase)
    if usar_numeros:
        todos_caracteres += list(string.digits)
    if usar_simbolos:
        todos_caracteres += list('!@#$%&')
    
    if not todos_caracteres:
        raise ValueError("ERRO = Pelo menos um tipo de caractere deve ser selecionado")
    
    return ''.join(random.choice(todos_caracteres) for _ in range(tamanho))

while True:
    try:
        print("Mínimo de tamanho = 4, Máximo de tamanho = 20")
        tamanho = input("Digite o tamanho da sua senha: ")
        
        if not tamanho.isdigit():
            raise ValueError("ERRO = Digite um valor válido inteiro")
        
        tamanho = int(tamanho)
        if tamanho < 4 or tamanho > 20:
            raise ValueError("ERRO = O tamanho da senha deve ser entre 4 e 20 caracteres")
        
        usar_minuscula = escolher_opcao("Incluir letras minúsculas? (s/n): ") == 's'
        usar_maiuscula = escolher_opcao("Incluir letras maiúsculas? (s/n): ") == 's'
        usar_numeros = escolher_opcao("Incluir números? (s/n): ") == 's'
        usar_simbolos = escolher_opcao("Incluir símbolos? (s/n): ") == 's'

        senha = gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos)
        print(f"Sua senha gerada é: {senha}")

        repetir = escolher_opcao("Deseja gerar outra senha? (s/n): ")
        if repetir != 's':
            print("Programa finalizado.")
            break

    except ValueError as e:
        print(e)
        print("Tente novamente.")
