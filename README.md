# Desafio Técnico LangChain: Ingestão e Busca Semântica com LangChain e Postgres

Este repositório contém códigos e exemplos práticos para o desafio técnico de LangChain, focado em ingestão e busca semântica utilizando LangChain e Postgres.

## Configuração do Ambiente

Para configurar o ambiente e instalar as dependências do projeto, siga os passos abaixo:

1. **Criar e ativar um ambiente virtual (`venv`):**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate
   ```

2. **Instalar as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar as variáveis de ambiente:**

   - Duplique o arquivo `.env.example` e renomeie para `.env`
   - Abra o arquivo `.env` e substitua os valores pelas suas chaves de API reais obtidas conforme instruções abaixo

4. **Subir o container do Postgres:**

   ```bash
   docker-compose up -d
   ```

5. **Executar o script de ingestão dos dados:**
   ```bash
   python src/ingest.py
   ```

## Requisitos para Execução dos Códigos

Para executar os códigos fornecidos no curso, é necessário criar chave de API (API Key) para o serviço da OpenAI. Abaixo, fornecemos instruções detalhadas para a criação dessa chave.

### Criando uma API Key na OpenAI

1. **Acesse o site da OpenAI:**

   [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

2. **Faça login ou crie uma conta:**

   - Se já possuir uma conta, clique em "Log in" e insira suas credenciais.
   - Caso contrário, clique em "Sign up" para criar uma nova conta.

3. **Navegue até a seção de API Keys:**

   - Após o login, clique em "API Keys" no menu lateral esquerdo.

4. **Crie uma nova API Key:**

   - Clique no botão "Create new secret key".
   - Dê um nome para a chave que a identifique facilmente.
   - Clique em "Create secret key".

5. **Copie e armazene sua API Key:**

   - A chave será exibida uma única vez. Copie-a e cole no arquivo `.env` na variável `OPENAI_API_KEY`.

Para mais detalhes, consulte o tutorial completo: [Como Gerar uma API Key na OpenAI?](https://hub.asimov.academy/tutorial/como-gerar-uma-api-key-na-openai/)

**Nota:** Certifique-se de não compartilhar suas chaves de API publicamente e de armazená-las em locais seguros, pois elas concedem acesso aos serviços correspondentes.

## Execução do chat

Para executar o chat, utilize o seguinte comando:

```bash
python src/chat.py
```

Para sair do chat, digite `sair`.
