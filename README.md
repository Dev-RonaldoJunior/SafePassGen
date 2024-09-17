
---

# Gerador de Senhas em Python

Este é um projeto simples de um **Gerador de Senhas** desenvolvido em Python. Ele permite gerar senhas com opções personalizáveis de tamanho (mínimo de 4 e máximo de 20 caracteres) e escolha de inclusão de letras maiúsculas, letras minúsculas, números e símbolos. O programa possui tratamento de erros, armazenamento seguro das senhas geradas e permite continuar gerando novas senhas sem precisar reiniciar o programa.

## Funcionalidades

- Geração de senhas com comprimento personalizado (entre 4 e 20 caracteres).
- Opções de inclusão de:
  - Letras minúsculas
  - Letras maiúsculas
  - Números
  - Símbolos
- Armazenamento seguro das senhas geradas usando criptografia.
- Leitura das senhas armazenadas com exibição numerada.
- Tratamento de erros para entradas inválidas, como:
  - Inserção de valores não numéricos no tamanho da senha.
  - Tamanho de senha fora do intervalo permitido (4 a 20 caracteres).
  - Escolhas incorretas ao selecionar as opções (s/n).
  - Garantia de que pelo menos um tipo de caractere será escolhido.
- Continuação do programa para gerar novas senhas sem precisar reiniciar.

## Requisitos

- Python 3.x
- Biblioteca `cryptography` para criptografia e descriptografia

## Como usar

1. **Clone o repositório ou baixe o arquivo:**
   ```bash
   git clone https://github.com/usuario/SafePassGen.git
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd SafePassGen
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Execute o script para gerar senhas:**
   ```bash
   python scripts/gerador_senhas.py
   ```

5. **Execute o script para ler as senhas armazenadas:**
   ```bash
   python scripts/leitor_senhas.py
   ```

6. **Interaja com o programa:**
   - No `gerador_senhas.py`:
     - Escolha o tamanho da senha entre 4 e 20 caracteres.
     - Escolha se deseja incluir letras minúsculas, letras maiúsculas, números e símbolos.
     - Receba sua senha gerada com base nas suas preferências.
     - Opção de gerar uma nova senha ou finalizar o programa.
   - No `leitor_senhas.py`:
     - Veja as senhas armazenadas com uma numeração clara.
     
---

## Exemplo de Execução

### Gerador de Senhas:

- Ao executar o programa `gerador_senhas.py` pela primeira vez, dois arquivos serão criados:
  - **`chave.key`:** Contém a chave de criptografia gerada automaticamente. Esta chave é essencial para descriptografar as senhas armazenadas.
  - **`senhas.txt`:** Armazena as senhas geradas, criptografadas para garantir sua segurança.
  
- O usuário pode escolher o tamanho da senha (entre 4 e 20 caracteres) e quais tipos de caracteres incluir (letras minúsculas, maiúsculas, números e símbolos).

Exemplo de execução:

```bash
Mínimo de tamanho = 4, Máximo de tamanho = 20
Digite o tamanho da sua senha: 8
Incluir letras minúsculas? (s/n): s
Incluir letras maiúsculas? (s/n): s
Incluir números? (s/n): s
Incluir símbolos? (s/n): n
Sua senha gerada é: Abc123de
Deseja gerar outra senha? (s/n): s
```

### Leitor de Senhas:

- O programa `leitor_senhas.py` lê e descriptografa as senhas armazenadas no arquivo `senhas.txt`, exibindo-as de forma legível para o usuário. 

Exemplo de execução:

```bash
Senha 1: Abc123de
Senha 2: FgH456ij
```

---

Esse novo texto dá mais contexto e explica de forma clara como os arquivos funcionam e como o usuário deve interagir com o programa.

## Tratamento de Erros

O programa lida com vários tipos de erros para garantir que o usuário insira valores corretos:

- **Tamanho inválido:** Se o usuário inserir um valor fora do intervalo permitido (4 a 20) ou não numérico, o programa exibe uma mensagem de erro e pede que o usuário tente novamente.
- **Escolha de opções inválida:** Se o usuário inserir algo diferente de "s" ou "n" ao selecionar as opções, o programa solicita que ele insira uma resposta válida.
- **Seleção de tipos de caracteres:** Se o usuário não selecionar nenhum tipo de caractere (letras, números ou símbolos), o programa exibe uma mensagem de erro e repete o processo.

## Estrutura do Projeto

```
SafePassGen/
│
├── dados/
│   ├── chave.key         # Chave de criptografia
│   └── senhas.txt        # Arquivo de senhas criptografadas
│
├── scripts/
│   ├── gerador_senhas.py  # Script principal do gerador de senhas
│   └── leitor_senhas.py   # Script para leitura das senhas armazenadas
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt      # Arquivo com as dependências do projeto
```

## Melhorias Futuras

Algumas melhorias que podem ser adicionadas no futuro:

- Interface gráfica (GUI) usando `tkinter` para facilitar o uso do gerador.
- Opções avançadas de personalização, como repetição de caracteres.
- Melhoria na segurança do armazenamento de senhas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---