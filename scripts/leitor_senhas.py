from cryptography.fernet import Fernet
import os

def carregar_chave(arquivo):
    with open(arquivo, 'rb') as f:
        return f.read()

def descriptografar_senha(senha_criptografada, chave):
    f = Fernet(chave)
    senha_bytes = f.decrypt(senha_criptografada)
    return senha_bytes.decode('utf-8')

def ler_senhas(arquivo):
    senhas = []
    if os.path.exists(arquivo):
        with open(arquivo, 'rb') as f:
            for linha in f:
                senhas.append(linha.strip())
    return senhas

def main():
    # Defina o caminho dos arquivos
    chave_arquivo = '../SafePassGen/dados/chave.key'
    senhas_arquivo = '../SafePassGen/dados/senhas.txt'

    # Carregar a chave de criptografia
    chave = carregar_chave(chave_arquivo)
    
    # Ler e descriptografar senhas
    senhas_criptografadas = ler_senhas(senhas_arquivo)
    if not senhas_criptografadas:
        print("Nenhuma senha encontrada para descriptografar.")
        return

    print("Senhas descriptografadas:")
    for i, senha_criptografada in enumerate(senhas_criptografadas, start=1):
        try:
            senha = descriptografar_senha(senha_criptografada, chave)
            print(f"Senha {i}: {senha}")
        except Exception as e:
            print(f"Erro ao descriptografar uma senha: {e}")

if __name__ == "__main__":
    main()
