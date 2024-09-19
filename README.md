# SafePassGen

SafePassGen é uma aplicação Python com interface gráfica para gerar senhas seguras e criptografadas. O projeto utiliza a biblioteca `cryptography` para garantir que as senhas geradas sejam armazenadas de forma segura.

## Funcionalidades

- **Geração de Senhas**: Permite gerar senhas com diferentes configurações:
  - Tamanho da senha (entre 4 e 20 caracteres)
  - Inclusão de letras minúsculas, maiúsculas, números e símbolos

- **Criptografia de Senhas**: As senhas geradas são criptografadas usando a biblioteca `cryptography` para garantir segurança.

- **Armazenamento e Arquivamento**: As senhas criptografadas são armazenadas em um arquivo e o sistema arquiva o arquivo se o tamanho exceder 1 MB.

- **Interface Gráfica**: Interface amigável desenvolvida com `tkinter` para interação do usuário.

- **Copiar Senha**: Copia a senha criptografada para a área de transferência.

- **Abrir Leitor de Senhas**: Permite abrir um script auxiliar para leitura de senhas.

## Requisitos

- Python 3.x
- Bibliotecas: `cryptography`, `tkinter`, `shutil`, `datetime`, `subprocess`

Para instalar as bibliotecas necessárias, você pode usar o arquivo `requirements.txt` incluído no projeto:

```bash
pip install -r requirements.txt
```

## Estrutura do Projeto

```
/SAFEPASSGEN
    /dados
        chave.key
        senhas.txt
    /scripts
        gerador_senhas.py
        leitor_senhas.py
    .gitignore
    LICENSE
    README.md
    requirements.txt
```

- **/dados**: Contém arquivos de chave e senhas.
- **/scripts**: Contém o script principal para geração de senhas e um script auxiliar (leitor de senhas).
- **.gitignore**: Arquivo para ignorar arquivos e pastas desnecessários no controle de versão.
- **LICENSE**: Arquivo de licença do projeto.
- **README.md**: Este arquivo.
- **requirements.txt**: Lista de dependências do projeto.

## Como Usar

1. **Configuração Inicial**:
   - Certifique-se de que a pasta `/dados` existe. Se não, ela será criada automaticamente pelo script.

2. **Executar o Gerador de Senhas**:
   - Navegue até o diretório `scripts` e execute o script `gerador_senhas.py`:
   
     ```bash
     python gerador_senhas.py
     ```
   - A interface gráfica será exibida, permitindo a configuração e geração de senhas.

3. **Gerar Senha**:
   - Insira o tamanho da senha desejada (entre 4 e 20 caracteres).
   - Selecione as opções de caracteres desejadas (letras minúsculas, maiúsculas, números e símbolos).
   - Clique no botão "Gerar Senha" para criar a senha e exibi-la.

4. **Copiar Senha**:
   - Clique no botão "Copiar Senha" para copiar a senha criptografada para a área de transferência.

5. **Abrir Leitor de Senhas**:
   - Clique no botão "Abrir Leitor de senhas" para abrir o script auxiliar para leitura de senhas.

6. **Sair**:
   - Clique no botão "Sair" e confirme para fechar o aplicativo.

## FAQ

**P: O que devo fazer se esquecer a chave de criptografia?**  
R: A chave é essencial para descriptografar as senhas. Se você perder a chave, não será possível recuperar as senhas armazenadas.

**P: Como posso garantir que minhas senhas são realmente seguras?**  
R: Utilize um comprimento mínimo de senha e inclua uma combinação de letras maiúsculas, minúsculas, números e símbolos para aumentar a segurança.

## Melhorias Futuras

1. **Recuperação de Chave**: Implementar um sistema para recuperação ou armazenamento seguro da chave de criptografia.

2. **Melhorias na Interface**: Adicionar temas personalizáveis e melhorar a experiência do usuário com opções de visualização mais intuitivas.

3. **Geração de Senhas em Massa**: Adicionar funcionalidade para gerar múltiplas senhas de uma vez.

4. **Integração com Gerenciadores de Senhas**: Integrar o gerador de senhas com gerenciadores de senhas populares para facilitar o uso das senhas geradas.

5. **Sistema de Backup**: Implementar uma funcionalidade para backup automático das senhas criptografadas.

6. **Validação de Senha**: Adicionar validação de força da senha para garantir que as senhas atendam a padrões de segurança recomendados.

## Contribuições

Contribuições são bem-vindas! Se você encontrar problemas ou quiser melhorar o projeto, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto é licenciado sob a Licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato

Para mais informações, você pode me contatar pelo [seu email](dev.ronaldojunior@gmail.com).