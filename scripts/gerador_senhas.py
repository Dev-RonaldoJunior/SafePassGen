import random
import string
from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import messagebox, Text
from PIL import Image, ImageTk
import shutil
from datetime import datetime

# Defina o caminho dos arquivos
chave_arquivo = '../SafePassGen/dados/chave.key'
senhas_arquivo = '../SafePassGen/dados/senhas.txt'

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
            pass  # Limpa o conteúdo do arquivo

def arquivar_arquivo(arquivo):
    """Arquiva o arquivo renomeando-o com a data e hora atual."""
    if os.path.exists(arquivo):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        novo_nome = f"senhas_{timestamp}.txt"
        shutil.move(arquivo, os.path.join(os.path.dirname(arquivo), novo_nome))
        # Recria o arquivo senhas.txt
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

        # Verifica se a opção para exibir a senha não criptografada está marcada
        if exibir_senha_var.get():
            senha_exibida_text.delete(1.0, tk.END)
            senha_exibida_text.insert(tk.END, senha)
        else:
            senha_exibida_text.delete(1.0, tk.END)

        # Atualiza o texto da senha criptografada
        senha_criptografada_text.delete(1.0, tk.END)
        senha_criptografada_text.insert(tk.END, senha_criptografada.decode())

        # Salva a senha criptografada
        salvar_senha(senha_criptografada, senhas_arquivo)

    except ValueError as e:
        messagebox.showerror("Erro", str(e))

def copiar_para_area_de_transferencia():
    senha = senha_exibida_text.get("1.0", tk.END).strip()
    if senha.startswith("Sua senha não criptografada é:"):
        senha = senha[len("Sua senha não criptografada é: "):]
        root.clipboard_clear()
        root.clipboard_append(senha)
        root.update()  # Atualiza a área de transferência

def copiar_senha_criptografada():
    senha_criptografada = senha_criptografada_text.get("1.0", tk.END).strip()
    if senha_criptografada.startswith("Sua senha criptografada é:"):
        senha_criptografada = senha_criptografada[len("Sua senha criptografada é: "):]
        root.clipboard_clear()
        root.clipboard_append(senha_criptografada)
        root.update()  # Atualiza a área de transferência

def confirmar_saida():
    resposta = messagebox.askyesno("Confirmação", "Você tem certeza de que deseja fechar o programa?")
    if resposta:
        root.destroy()

# Configura a interface gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

# Configura o tamanho da janela
root.geometry("600x400")

# Carregar imagem de fundo usando Pillow
fundo_img_pil = Image.open("../SafePassGen/imagens/fundo.jpg")  # Certifique-se de que a imagem está no formato PNG ou JPG
fundo_img_tk = ImageTk.PhotoImage(fundo_img_pil)

fundo_label = tk.Label(root, image=fundo_img_tk)
fundo_label.place(relwidth=1, relheight=1)

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
tamanho_label = tk.Label(root, text="Digite o tamanho da senha:", font=("Helvetica", 12))
tamanho_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

tamanho_entry = tk.Entry(root, font=("Helvetica", 12))
tamanho_entry.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

var_minuscula = tk.BooleanVar()
var_maiuscula = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

minuscula_check = tk.Checkbutton(root, text="Incluir letras minúsculas", variable=var_minuscula, font=("Helvetica", 12), bg="#ffffff")
minuscula_check.grid(row=1, column=0, padx=10, pady=5, sticky='w')

maiuscula_check = tk.Checkbutton(root, text="Incluir letras maiúsculas", variable=var_maiuscula, font=("Helvetica", 12), bg="#ffffff")
maiuscula_check.grid(row=2, column=0, padx=10, pady=5, sticky='w')

numeros_check = tk.Checkbutton(root, text="Incluir números: 1, 2, 3, etc...", variable=var_numeros, font=("Helvetica", 12), bg="#ffffff")
numeros_check.grid(row=3, column=0, padx=10, pady=5, sticky='w')

simbolos_check = tk.Checkbutton(root, text="Incluir símbolos: !@#$%&/...", variable=var_simbolos, font=("Helvetica", 12), bg="#ffffff")
simbolos_check.grid(row=4, column=0, padx=10, pady=5, sticky='w')

exibir_senha_var = tk.BooleanVar()
exibir_senha_check = tk.Checkbutton(root, text="Exibir senha não criptografada", variable=exibir_senha_var, font=("Helvetica", 12), bg="#ffffff")
exibir_senha_check.grid(row=5, column=0, padx=10, pady=5, sticky='w')

senha_exibida_text = Text(root, height=2, width=30, font=("Helvetica", 12))
senha_exibida_text.grid(row=6, column=0, padx=10, pady=10, sticky='w')

copiar_botao = tk.Button(root, text="Copiar Senha Não Criptografada", command=copiar_para_area_de_transferencia, font=("Helvetica", 12))
copiar_botao.grid(row=6, column=1, padx=10, pady=10, sticky='w')

senha_criptografada_text = Text(root, height=2, width=30, font=("Helvetica", 12))
senha_criptografada_text.grid(row=7, column=0, padx=10, pady=10, sticky='w')

copiar_botao_criptografada = tk.Button(root, text="Copiar Senha Criptografada", command=copiar_senha_criptografada, font=("Helvetica", 12))
copiar_botao_criptografada.grid(row=7, column=1, padx=10, pady=10, sticky='w')

gerar_botao = tk.Button(root, text="Gerar Senha", command=gerar_e_exibir_senha, font=("Helvetica", 12))
gerar_botao.grid(row=8, column=0, padx=10, pady=10, sticky='w')

sair_botao = tk.Button(root, text="Sair", command=confirmar_saida, font=("Helvetica", 12))
sair_botao.grid(row=8, column=1, padx=10, pady=10, sticky='w')

root.mainloop()
