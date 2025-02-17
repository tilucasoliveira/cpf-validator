# CPF Validator
Este projeto tem como objetivo desenvolver um microsserviço eficiente, escalável e econômico para validação de CPFs, utilizando arquitetura serverless. A aplicação será construída com base em princípios modernos de computação em nuvem, garantindo alta disponibilidade, baixo custo operacional e facilidade de manutenção.

# cpf-validator
Este projeto é um microsserviço para validação de CPFs utilizando Azure Functions.

## Estrutura do Projeto

- `src/ValidateCpfFunction/`: Contém o código da Azure Function.
- `tests/`: Contém os testes unitários.
- `.github/workflows/`: Contém o workflow de CI.

## Como Executar

1. Clone o repositório.
2. Instale as dependências:
    ```bash
    pip install -r src/ValidateCpfFunction/requirements.txt
    ```
3. Configure o banco de dados:
    ```bash
    sqlite3 /path/to/database.db < schema.sql
    ```
4. Execute a função localmente:
    ```bash
    func start
    ```
5. Execute os testes:
    ```bash
    python -m unittest discover -s tests
    ```

## Licença

Este projeto está licenciado sob a licença MIT.
