import os
import random
import shutil
import string
import subprocess
from datetime import datetime
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import messagebox

# Definição dos caminhos dos arquivos
CHAVE_ARQUIVO = '../SafePassGen/dados/chave.key'
SENHAS_ARQUIVO = '../SafePassGen/dados/senhas.txt'
LIMITE_ARQUIVO = 1024 * 1024

# Funções de geração e manipulação de senhas
def gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos):
    caracteres = []
    if usar_minuscula:
        caracteres.extend(string.ascii_lowercase)
    if usar_maiuscula:
        caracteres.extend(string.ascii_uppercase)
    if usar_numeros:
        caracteres.extend(string.digits)
    if usar_simbolos:
        caracteres.extend('-!@#$%&/+*_')

    if not caracteres:
        raise ValueError("ERRO: Pelo menos um tipo de caractere deve ser selecionado")
    
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

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
    return f.encrypt(senha_bytes)

def salvar_senha(senha_criptografada, arquivo):
    with open(arquivo, 'ab') as f:
        f.write(senha_criptografada + b'\n')

def verificar_e_arquivar_arquivo(arquivo, limite):
    if not os.path.exists(arquivo):
        open(arquivo, 'w').close()
    if os.path.getsize(arquivo) > limite:
        arquivar_arquivo(arquivo)

def arquivar_arquivo(arquivo):
    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
    novo_nome = f"senhas_{timestamp}.txt"
    shutil.move(arquivo, os.path.join(os.path.dirname(arquivo), novo_nome))
    open(arquivo, 'w').close()

# Funções para a interface gráfica
def gerar_e_exibir_senha():
    try:
        tamanho = int(tamanho_entry.get())
        if not 4 <= tamanho <= 20:
            raise ValueError("ERRO: O tamanho da senha deve ser entre 4 e 20")

        usar_minuscula = var_minuscula.get()
        usar_maiuscula = var_maiuscula.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        senha = gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos)
        senha_criptografada = criptografar_senha(senha, chave)

        verificar_e_arquivar_arquivo(SENHAS_ARQUIVO, LIMITE_ARQUIVO)

        senha_criptografada_text.delete(1.0, tk.END)
        senha_criptografada_text.insert(tk.END, senha_criptografada.decode())

        salvar_senha(senha_criptografada, SENHAS_ARQUIVO)

        numero_senha = obter_numero_senha()
        numero_senha_text.delete(1.0, tk.END)
        numero_senha_text.insert(tk.END, f"Essa é a senha {numero_senha}")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def gerar_multipla_senhas():
    try:
        num_senhas = int(num_senhas_entry.get())
        if not 1 <= num_senhas <= 2000:
            raise ValueError("ERRO: O número de senhas deve ser entre 1 e 2000")

        tamanho = int(tamanho_entry.get())
        if not 4 <= tamanho <= 20:
            raise ValueError("ERRO: O tamanho da senha deve ser entre 4 e 20")

        usar_minuscula = var_minuscula.get()
        usar_maiuscula = var_maiuscula.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        senhas_geradas = [
            criptografar_senha(gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos), chave).decode()
            for _ in range(num_senhas)
        ]

        senha_criptografada_text.delete(1.0, tk.END)
        for i, senha in enumerate(senhas_geradas, start=1):
            senha_criptografada_text.insert(tk.END, f"Senha {i}: {senha}\n \n")

        verificar_e_arquivar_arquivo(SENHAS_ARQUIVO, LIMITE_ARQUIVO)

        with open(SENHAS_ARQUIVO, 'ab') as f:
            for senha in senhas_geradas:
                f.write(senha.encode() + b'\n')

        numero_senha_text.delete(1.0, tk.END)
        numero_senha_text.insert(tk.END, f"Foram geradas {num_senhas} senhas.")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def obter_numero_senha():
    if os.path.exists(SENHAS_ARQUIVO):
        with open(SENHAS_ARQUIVO, 'rb') as f:
            return len(f.readlines())
    return 1

def copiar_senha_criptografada():
    senha_criptografada = senha_criptografada_text.get("1.0", tk.END).strip()
    if senha_criptografada:
        root.clipboard_clear()
        root.clipboard_append(senha_criptografada)
        root.update()

def confirmar_saida():
    if messagebox.askyesno("Sair", "Tem certeza de que deseja sair?"):
        root.destroy()

def abrir_leitor():
    try:
        subprocess.Popen(['python', '../SafePassGen/scripts/leitor_senhas.py'])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o leitor de senhas: {e}")

# Configuração da interface gráfica
root = tk.Tk()
root.title("SafePassGen")
root.geometry("360x420")
root.configure(bg="#4A90E2")
root.resizable(False, False)
root.iconbitmap("icones/icon.ico")

# Verifica se a chave já foi gerada
if not os.path.exists(CHAVE_ARQUIVO):
    chave = gerar_chave()
    salvar_chave(chave, CHAVE_ARQUIVO)
else:
    chave = carregar_chave(CHAVE_ARQUIVO)

# Criação de widgets
def criar_widget_label(root, texto, linha, coluna, pad_x=10, pad_y=5, col_span=1):
    label = tk.Label(root, text=texto, font=("Helvetica", 10), bg="#4A90E2", fg="white")
    label.grid(row=linha, column=coluna, padx=pad_x, pady=pad_y, sticky='w', columnspan=col_span)

criar_widget_label(root, "Digite o tamanho da senha:", 0, 0)
tamanho_entry = tk.Entry(root, font=("Helvetica", 8))
tamanho_entry.grid(row=0, column=0, padx=180, pady=5, sticky='w')
tamanho_entry.insert(0, "20")

criar_widget_label(root, "Número de senhas geradas:", 1, 0)
num_senhas_entry = tk.Entry(root, font=("Helvetica", 8))
num_senhas_entry.grid(row=1, column=0, padx=180, pady=5, sticky='w')
num_senhas_entry.insert(0, "1")

# Botões e caixas de seleção
var_minuscula = tk.BooleanVar()
var_maiuscula = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

def criar_checkbutton(root, texto, var, linha):
    check = tk.Checkbutton(root, text=texto, variable=var, font=("Helvetica", 10), bg="#4A90E2", fg="white", selectcolor="#0066CC")
    check.grid(row=linha, column=0, padx=10, pady=5, sticky='w')

criar_checkbutton(root, "Incluir letras minúsculas", var_minuscula, 2)
criar_checkbutton(root, "Incluir letras maiúsculas", var_maiuscula, 3)
criar_checkbutton(root, "Incluir números", var_numeros, 4)
criar_checkbutton(root, "Incluir símbolos", var_simbolos, 5)

# Botões de ação
tk.Button(root, text="Gerar Senha", command=gerar_e_exibir_senha, font=("Helvetica", 9), bg="white", fg="black").grid(row=6, column=0, padx=10, pady=5, sticky='w')

tk.Button(root, text="Gerar Múltiplas Senhas", command=gerar_multipla_senhas, font=("Helvetica", 9), bg="white", fg="black").grid(row=6, column=0, padx=100, pady=5, sticky='w')

# Exibição das senhas
senha_criptografada_text = tk.Text(root, height=6, width=40, font=("Helvetica", 8))
senha_criptografada_text.grid(row=7, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Botão para copiar senha
tk.Button(root, text="Copiar Senha", command=copiar_senha_criptografada, font=("Helvetica", 10), bg="green", fg="white").grid(row=7, column=0, padx=260, pady=5, sticky='w')

# Exibição do número de senhas
numero_senha_text = tk.Text(root, height=1, width=40, font=("Helvetica", 8))
numero_senha_text.grid(row=8, column=0, columnspan=2, padx=10, pady=5, sticky='w')

# Botão para abrir o leitor de senhas
tk.Button(root, text="Abrir Leitor de Senhas", command=abrir_leitor, font=("Helvetica", 10), bg="purple", fg="white").grid(row=9, column=0, padx=10, pady=5, sticky='w')

# Botão para sair
tk.Button(root, text="Sair", command=confirmar_saida, font=("Helvetica", 10), bg="red", fg="white").grid(row=9, column=0, padx=295, pady=5, sticky='w')

# Inicia o programa
root.mainloop()
