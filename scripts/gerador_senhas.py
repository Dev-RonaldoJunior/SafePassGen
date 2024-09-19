import random
import string
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox
import shutil
from datetime import datetime
import subprocess

# Defina o caminho dos arquivos
chave_arquivo = '../SafePassGen/dados/chave.key'
senhas_arquivo = '../SafePassGen/dados/senhas.txt'

# Funções
def gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos):
    todos_caracteres = []
    if usar_minuscula:
        todos_caracteres += list(string.ascii_lowercase)
    if usar_maiuscula:
        todos_caracteres += list(string.ascii_uppercase)
    if usar_numeros:
        todos_caracteres += list(string.digits)
    if usar_simbolos:
        todos_caracteres += list('-!@#$%&/+*_')
    
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

def limpar_arquivo_se_necessario(arquivo, limite):
    """Limpa o arquivo se o tamanho exceder o limite."""
    if os.path.getsize(arquivo) > limite:
        with open(arquivo, 'w') as f:
            pass

def arquivar_arquivo(arquivo):
    """Arquiva o arquivo renomeando-o com a data e hora atual."""
    if os.path.exists(arquivo):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        novo_nome = f"senhas_{timestamp}.txt"
        shutil.move(arquivo, os.path.join(os.path.dirname(arquivo), novo_nome))
        open(arquivo, 'w').close()

def gerar_e_exibir_senha():
    try:
        tamanho = int(tamanho_entry.get())
        if tamanho < 4 or tamanho > 20:
            raise ValueError("ERRO = O tamanho da senha deve ser entre 4 e 20 caracteres")

        usar_minuscula = var_minuscula.get()
        usar_maiuscula = var_maiuscula.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        senha = gerar_senha(tamanho, usar_minuscula, usar_maiuscula, usar_numeros, usar_simbolos)
        senha_criptografada = criptografar_senha(senha, chave)
        
        # Verifica se o arquivo existe, se não, cria um
        if not os.path.exists(senhas_arquivo):
            open(senhas_arquivo, 'w').close()

        # Arquiva o arquivo se necessário
        if os.path.getsize(senhas_arquivo) > 1024 * 1024:  # Limite de 1 MB
            arquivar_arquivo(senhas_arquivo)

        # Atualiza o texto da senha criptografada
        senha_criptografada_text.delete(1.0, tk.END)
        senha_criptografada_text.insert(tk.END, senha_criptografada.decode())

        # Salva a senha criptografada
        salvar_senha(senha_criptografada, senhas_arquivo)

        # Atualiza e mostra o número da senha
        numero_senha = obter_numero_senha()
        numero_senha_text.delete(1.0, tk.END)
        numero_senha_text.insert(tk.END, f"Essa é a senha {numero_senha}")

    except ValueError as e:
        messagebox.showerror("Erro", "Você deve digitar um valor entre 4 e 20")

def obter_numero_senha():
    """Obtém o número da próxima senha a ser criada, com base no número de senhas existentes."""
    if os.path.exists(senhas_arquivo):
        with open(senhas_arquivo, 'rb') as f:
            linhas = f.readlines()
        return len(linhas)
    return 1

def copiar_senha_criptografada():
    """Copia a senha criptografada para a área de transferência."""
    senha_criptografada = senha_criptografada_text.get("1.0", tk.END).strip()
    if senha_criptografada:
        root.clipboard_clear()
        root.clipboard_append(senha_criptografada)
        root.update()

def confirmar_saida():
    resposta = messagebox.askyesno("Sair", "Tem certeza de que deseja sair?")
    if resposta:
        root.destroy()

def limpar_tamanho_entry(event):
    if tamanho_entry.get() == "Digite um valor entre 4 e 20":
        tamanho_entry.delete(0, tk.END)

def limpar_senha_criptografada(event):
    if senha_criptografada_text.get("1.0", tk.END).strip():
        senha_criptografada_text.delete(1.0, tk.END)

def abrir_leitor():
    """Abre o script do leitor de senhas."""
    try:
        subprocess.Popen(['python', '../SafePassGen/scripts/leitor_senhas.py'])
    except Exception as e:
        messagebox.showerror("Erro", f"Não foi possível abrir o leitor de senhas: {e}")

# Configura a interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

# Define ícone do programa
root.iconbitmap("icones/icon.ico")

# Define a cor de fundo
cor_fundo = "#4A90E2"

# Configura o tamanho da janela e a cor de fundo
root.geometry("360x420")
root.configure(bg=cor_fundo)

# Desativa a opção de maximizar
root.resizable(False, False)

# Cria a pasta dados se não existir
if not os.path.exists(os.path.dirname(chave_arquivo)):
    os.makedirs(os.path.dirname(chave_arquivo))

# Verifica se a chave já foi gerada, se não, gera e salva
if not os.path.exists(chave_arquivo):
    chave = gerar_chave()
    salvar_chave(chave, chave_arquivo)
else:
    chave = carregar_chave(chave_arquivo)

# Configura a interface
tamanho_label = tk.Label(root, text="Digite o tamanho da senha:", font=("Helvetica", 12), bg=cor_fundo, fg="white")
tamanho_label.grid(row=0, column=0, padx=10, pady=5, sticky='w')

tamanho_entry = tk.Entry(root, font=("Helvetica", 8))
tamanho_entry.grid(row=0, column=0, padx=210, pady=5, sticky='w')
tamanho_entry.insert(0, "     Valor entre 4 e 20")
tamanho_entry.bind("<FocusIn>", limpar_tamanho_entry)

var_minuscula = tk.BooleanVar()
var_maiuscula = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

# Row 1
minuscula_check = tk.Checkbutton(root, text="Incluir letras minúsculas", variable=var_minuscula, font=("Helvetica", 12), bg=cor_fundo, fg="white", selectcolor="#0066CC")
minuscula_check.grid(row=1, column=0, padx=10, pady=5, sticky='w')

# Row 2
maiuscula_check = tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=var_maiuscula, font=("Helvetica", 12), bg=cor_fundo, fg="white", selectcolor="#0066CC")
maiuscula_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')

# Row 3
numeros_check = tk.Checkbutton(root, text="Incluir números: 1, 2, 3, etc...", variable=var_numeros, font=("Helvetica", 12), bg=cor_fundo, fg="white", selectcolor="#0066CC")
numeros_check.grid(row=3, column=0, padx=10, pady=5, sticky='w')

# Row 4
simbolos_check = tk.Checkbutton(root, text="Incluir símbolos: !@#$%&/...", variable=var_simbolos, font=("Helvetica", 12), bg=cor_fundo, fg="white", selectcolor="#0066CC")
simbolos_check.grid(row=4, column=0, padx=10, pady=5, sticky='w')

# Row 5
gerar_senha_btn = tk.Button(root, text="Gerar Senha", command=gerar_e_exibir_senha, font=("Helvetica", 9), bg="white", fg="black")
gerar_senha_btn.grid(row=5, column=0, padx=80, pady=10, sticky='w')

# Row 7
numero_senha_text = tk.Text(root, height=1, width=34, font=("Helvetica", 10))
numero_senha_text.grid(row=7, column=0, padx=10, pady=10, sticky='w')

# Row 9
senha_criptografada_text = tk.Text(root, height=5, width=34, font=("Helvetica", 10))
senha_criptografada_text.grid(row=9, column=0, padx=10, pady=5, sticky='w')
senha_criptografada_text.insert(tk.END, """
                
                Senha Criptografada""")
senha_criptografada_text.bind("<FocusIn>", limpar_senha_criptografada)

copiar_btn = tk.Button(root, text="Copiar Senha", command=copiar_senha_criptografada, font=("Helvetica", 10), bg="white", fg="black")
copiar_btn.grid(row=9, column=0, padx=261, pady=10, sticky='w')

# Row 10
abrir_leitor_btn = tk.Button(root, text="Abrir Leitor de senhas", command=abrir_leitor, font=("Helvetica", 10), bg="white", fg="black")
abrir_leitor_btn.grid(row=10, column=0, padx=10, pady=10, sticky='w')

sair_btn = tk.Button(root, text="Sair", command=confirmar_saida, font=("Helvetica", 9), bg="red", fg="white")
sair_btn.grid(row=10, column=0, padx=285, pady=10, sticky='w')


root.mainloop()
