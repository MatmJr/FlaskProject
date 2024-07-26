# FlaskProject

# Flask Employee Management System

Este é um sistema de gerenciamento de funcionários construído com Flask. Ele permite criar, visualizar e listar funcionários.

## Requisitos

- Python 3.7+
- pip (gerenciador de pacotes do Python)

## Configuração do Ambiente

### 1. Clonar o Repositório

```bash
git clone https://github.com/MatmJr/FlaskProject
cd FlaskProject
```

### 2. Configurar o Ambiente Virtual

Crie, ative e instale as bibliotecas em um ambiente virtual para o projeto:
- **Windows:**

  ```bash
  python -m venv .venv && .\.venv\Scripts\activate && pip install -r requirements.txt
  ```

- **macOS e Linux:**

  ```bash
  python -m venv .venv || source .venv/bin/activate || pip install -r requirements.txt
  ```

## Executar o Aplicativo

Para iniciar o servidor Flask, execute:

```bash
python src\app.py
```

O aplicativo estará disponível em [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Executar o teste

```bash
pytest --cov=src
```
**Desafio:** Atingir 100% de cobertura nos testes.

## Estrutura do Projeto

```
src/
  ├── models/
  │   └── employeeModel.py
  ├── controllers/
  │   └── employeeController.py
  ├── views/
  │   ├── mainpage.html
  │   ├── createpage.html
  │   ├── datalist.html
  │   ├── data.html
  │   ├── update.html
  │   └── delete.html
  ├── app.py
  ├── test_app.py
── requirements.txt
── LICENSE.md
── README.md
```

## Contribuição

1. Faça um fork do projeto.
2. Crie um branch para sua feature (`git checkout -b feature/nome-da-feature`).
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`).
4. Push para o branch (`git push origin feature/nome-da-feature`).
5. Crie um novo Pull Request.
