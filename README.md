# Gerador de Senhas em Python

Este é um projeto simples de um **Gerador de Senhas** desenvolvido em Python. Ele permite gerar senhas com opções personalizáveis de tamanho (mínimo de 4 e máximo de 20 caracteres) e escolha de inclusão de letras maiúsculas, letras minúsculas, números e símbolos. O programa possui tratamento de erros e permite continuar gerando novas senhas sem precisar reiniciar o programa.

## Funcionalidades

- Geração de senhas com comprimento personalizado (entre 4 e 20 caracteres).
- Opções de inclusão de:
  - Letras minúsculas
  - Letras maiúsculas
  - Números
  - Símbolos
- Tratamento de erros para entradas inválidas, como:
  - Inserção de valores não numéricos no tamanho da senha.
  - Tamanho de senha fora do intervalo permitido (4 a 20 caracteres).
  - Escolhas incorretas ao selecionar as opções (s/n).
  - Garantia de que pelo menos um tipo de caractere será escolhido.
- Continuação do programa para gerar novas senhas sem precisar reiniciar.

## Requisitos

- Python 3.x

## Como usar

1. **Clone o repositório ou baixe o arquivo:**
   ```bash
   git clone https://github.com/usuario/gerador-de-senhas.git
   ```

2. **Navegue até o diretório do projeto:**
   ```bash
   cd gerador-de-senhas
   ```

3. **Execute o script:**
   ```bash
   python gerador_senhas.py
   ```

4. **Interaja com o programa:**
   - Escolha o tamanho da senha entre 4 e 20 caracteres.
   - Escolha se deseja incluir letras minúsculas, letras maiúsculas, números e símbolos.
   - Receba sua senha gerada com base nas suas preferências.
   - Opção de gerar uma nova senha ou finalizar o programa.

## Exemplo de Execução

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

## Tratamento de Erros

O programa lida com vários tipos de erros para garantir que o usuário insira valores corretos:

- **Tamanho inválido:** Se o usuário inserir um valor fora do intervalo permitido (4 a 20) ou não numérico, o programa exibe uma mensagem de erro e pede que o usuário tente novamente.
- **Escolha de opções inválida:** Se o usuário inserir algo diferente de "s" ou "n" ao selecionar as opções, o programa solicita que ele insira uma resposta válida.
- **Seleção de tipos de caracteres:** Se o usuário não selecionar nenhum tipo de caractere (letras, números ou símbolos), o programa exibe uma mensagem de erro e repete o processo.

## Estrutura do Projeto

```
SAFEPASSGEN/
│
├── gerador_senhas.py  # Script principal do gerador de senhas
├── README.md          # Arquivo de documentação do projeto
```

## Melhorias Futuras

Algumas melhorias que podem ser adicionadas no futuro:

- Interface gráfica (GUI) usando `tkinter` para facilitar o uso do gerador.
- Opções avançadas de personalização, como repetição de caracteres.
- Armazenamento seguro de senhas geradas.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request no repositório.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.