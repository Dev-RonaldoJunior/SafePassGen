import random

# Listas com caracteres possíveis.
minuscula = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maiuscula = [letra.upper() for letra in minuscula]
numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
simbolos = ['!', '@', '#', '$', '%', '&']

while True:
    try:
        # Pede ao usuário o tamanho da senha e opções.
        print("Mínimo de tamanho = 4, Máximo de tamanho = 20")
        tamanho = input("Digite o tamanho da sua senha: ")

        # Verifica se o tamanho é um número válido.
        if not tamanho.isdigit():
            raise ValueError("ERRO = Digite um valor válido inteiro")
        
        tamanho = int(tamanho)
        if tamanho < 4 or tamanho > 20:
            raise ValueError("ERRO = O tamanho da senha deve ser entre 4 e 20 caracteres")
        
        # Função para garantir que o usuário digite 's' ou 'n'.
        def escolher_opcao(mensagem):
            while True:
                opcao = input(mensagem).lower()
                if opcao == 's' or opcao == 'n':
                    return opcao
                else:
                    print("ERRO = Digite 's' para sim ou 'n' para não.")
        
        # Pergunta se o usuário quer incluir diferentes tipos de caracteres.
        usar_minuscula = escolher_opcao("Incluir letras minúsculas? (s/n): ") == 's'
        usar_maiuscula = escolher_opcao("Incluir letras maiúsculas? (s/n): ") == 's'
        usar_numeros = escolher_opcao("Incluir números? (s/n): ") == 's'
        usar_simbolos = escolher_opcao("Incluir símbolos? (s/n): ") == 's'

        # Cria uma lista com os caracteres selecionados.
        todos_caracteres = []
        if usar_minuscula:
            todos_caracteres += minuscula
        if usar_maiuscula:
            todos_caracteres += maiuscula
        if usar_numeros:
            todos_caracteres += numeros
        if usar_simbolos:
            todos_caracteres += simbolos

        # Verifica se pelo menos um tipo de caractere foi selecionado.
        if not todos_caracteres:
            raise ValueError("ERRO = Pelo menos um tipo de caractere deve ser selecionado")

        # Gera a senha.
        senha = ''.join(random.choice(todos_caracteres) for _ in range(tamanho))
        print(f"Sua senha gerada é: {senha}")

        # Pergunta se o usuário quer gerar outra senha ou finalizar.
        repetir = escolher_opcao("Deseja gerar outra senha? (s/n): ")
        if repetir != 's':
            print("Programa finalizado.")
            break

    except ValueError as e:
        print(e)
        print("Tente novamente.")
