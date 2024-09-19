from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox
import subprocess

def carregar_chave(arquivo):
    """Carrega a chave de criptografia do arquivo."""
    try:
        with open(arquivo, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"O arquivo {arquivo} não foi encontrado.")
    except Exception as e:
        raise Exception(f"Erro ao carregar a chave: {e}")

def descriptografar_senha(senha_criptografada, chave):
    """Descriptografa a senha criptografada usando a chave fornecida."""
    try:
        f = Fernet(chave)
        senha_bytes = f.decrypt(senha_criptografada)
        return senha_bytes.decode('utf-8')
    except Fernet.InvalidToken:
        raise Exception("Token de criptografia inválido. Verifique se a chave está correta.")
    except Exception as e:
        raise Exception(f"Erro ao descriptografar a senha: {e}")

def ler_senhas(arquivo):
    """Lê senhas criptografadas do arquivo."""
    senhas = []
    if os.path.exists(arquivo):
        try:
            with open(arquivo, 'rb') as f:
                for linha in f:
                    senhas.append(linha.strip())
        except Exception as e:
            raise Exception(f"Erro ao ler o arquivo de senhas: {e}")
    else:
        messagebox.showinfo("Informação", "O arquivo de senhas não existe.")
    return senhas

def mostrar_senhas():
    """Lê e exibe todas as senhas descriptografadas na interface gráfica."""
    try:
        chave = carregar_chave(chave_arquivo)
        senhas_criptografadas = ler_senhas(senhas_arquivo)
        if not senhas_criptografadas:
            messagebox.showinfo("Informação", "Nenhuma senha encontrada para descriptografar.")
            return

        texto_senhas.delete(1.0, tk.END)  # Limpa o campo de texto
        for i, senha_criptografada in enumerate(senhas_criptografadas, start=1):
            try:
                senha = descriptografar_senha(senha_criptografada, chave)
                texto_senhas.insert(tk.END, f"Senha {i}: {senha}\n")
            except Exception as e:
                texto_senhas.insert(tk.END, f"Erro ao descriptografar uma senha: {e}\n")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def buscar_senha_por_numero():
    """Busca e exibe a senha descriptografada pelo número fornecido na interface gráfica."""
    try:
        numero = int(entry_numero.get())
        chave = carregar_chave(chave_arquivo)
        senhas_criptografadas = ler_senhas(senhas_arquivo)

        if 1 <= numero <= len(senhas_criptografadas):
            senha_criptografada = senhas_criptografadas[numero - 1]
            senha = descriptografar_senha(senha_criptografada, chave)
            texto_senhas.delete(1.0, tk.END)  # Limpa o campo de texto
            texto_senhas.insert(tk.END, f"Senha {numero}: {senha}\n")
        else:
            messagebox.showinfo("Informação", "Número de senha fora do intervalo.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira um número válido.")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

def confirmar_saida():
    """Confirma se o usuário deseja sair do programa."""
    resposta = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja fechar o programa?")
    if resposta:
        root.destroy()

def abrir_gerador():
    """Abre o script de gerador de senhas."""
    try:
        caminho_gerador = os.path.abspath('../SafePassGen/scripts/gerador_senhas.py')
        subprocess.Popen(['python', caminho_gerador])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o gerador de senhas: {e}")

# Configura a interface gráfica
root = tk.Tk()
root.title("Leitor de Senhas")

# Define o ícone do programa (se disponível)
root.iconbitmap("icones/icon.ico")

# Define a cor de fundo
cor_fundo = "#4A90E2"

# Configura o tamanho da janela e a cor de fundo
root.geometry("360x420")
root.configure(bg=cor_fundo)

# Desativa a opção de maximizar
root.resizable(False, False)

# Define o caminho dos arquivos
chave_arquivo = '../SafePassGen/dados/chave.key'
senhas_arquivo = '../SafePassGen/dados/senhas.txt'

# Configura a interface

# Row 0
label_numero = tk.Label(root, text="Número da Senha:", font=("Helvetica", 9), bg=cor_fundo, fg="white")
label_numero.grid(row=0, column=0, padx=5, pady=5, sticky="w")

entry_numero = tk.Entry(root, font=("Helvetica", 9))
entry_numero.grid(row=0, column=0, padx=115, pady=5, sticky="w")

buscar_senha_btn = tk.Button(root, text="Buscar Senha", command=buscar_senha_por_numero, font=("Helvetica", 9), bg="white", fg="black")
buscar_senha_btn.grid(row=0, column=0, columnspan=2, padx=265, pady=5, sticky="w")

# Row 1
label_numero = tk.Label(root, text="Número da Senha:", font=("Helvetica", 9), bg=cor_fundo, fg="white")
label_numero.grid(row=1, column=0, padx=10, pady=0, sticky="w")

# Row 2
texto_senhas = tk.Text(root, height=20, width=35, font=("Helvetica", 9))
texto_senhas.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='w')

mostrar_senhas_btn = tk.Button(root, text="Mostrar Senhas", command=mostrar_senhas, font=("Helvetica", 8), bg="white", fg="black")
mostrar_senhas_btn.grid(row=2, column=0, padx=265, pady=5, sticky='w')

# Row 3
abrir_gerador_btn = tk.Button(root, text="Abrir Gerador de Senhas", command=abrir_gerador, font=("Helvetica", 9), bg="white", fg="black")
abrir_gerador_btn.grid(row=3, column=0, padx=10, pady=5, sticky='w')

sair_btn = tk.Button(root, text="Sair", command=confirmar_saida, font=("Helvetica", 9), bg="red", fg="white")
sair_btn.grid(row=3, column=0, columnspan=2, padx=280, pady=10, sticky='w')


# Inicia o programa
root.mainloop()
