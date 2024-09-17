import random
import string
from cryptography.fernet import Fernet
import os

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

def gerar_chave():
    return Fernet.generate_key()

def salvar_chave(chave, arquivo):
    with open(arquivo, 'wb') as f:
        f.write(chave)

def carregar_chave(arquivo):
    with open(arquivo, 'rb') as f:
        return f.read()

def criptografar_senha(senha, chave):
    f = Fernet(chave)
    senha_bytes = senha.encode('utf-8')
    senha_criptografada = f.encrypt(senha_bytes)
    return senha_criptografada

def salvar_senha(senha_criptografada, arquivo):
    with open(arquivo, 'ab') as f:
        f.write(senha_criptografada + b'\n')

def main():
    # Defina o caminho dos arquivos
    chave_arquivo = '../SafePassGen/dados/chave.key'
    senhas_arquivo = '../SafePassGen/dados/senhas.txt'
    
    # Criar pasta dados se não existir
    if not os.path.exists(os.path.dirname(chave_arquivo)):
        os.makedirs(os.path.dirname(chave_arquivo))
    
    # Verifica se a chave já foi gerada, se não, gera e salva
    if not os.path.exists(chave_arquivo):
        chave = gerar_chave()
        salvar_chave(chave, chave_arquivo)
    else:
        chave = carregar_chave(chave_arquivo)
    
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

            # Criptografar e salvar a senha
            senha_criptografada = criptografar_senha(senha, chave)
            salvar_senha(senha_criptografada, senhas_arquivo)

            repetir = escolher_opcao("Deseja gerar outra senha? (s/n): ")
            if repetir != 's':
                print("Programa finalizado.")
                break

        except ValueError as e:
            print(e)
            print("Tente novamente.")

if __name__ == "__main__":
    main()
