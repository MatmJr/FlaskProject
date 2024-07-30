from flask import Flask
from models.employeeModel import db
from controllers.employeeController import employee_blueprint

"""
Este módulo inicializa e executa a aplicação Flask para o gerenciamento de funcionários.

Configurações:
    SQLALCHEMY_DATABASE_URI (str): URI do banco de dados.
    SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag para desativar o recurso de rastreamento de modificações do SQLAlchemy.

Blueprints:
    employee_blueprint: Blueprint para gerenciar as rotas relacionadas aos funcionários.

Execução:
    Cria o banco de dados e inicia o servidor Flask no modo de depuração.

"""

app = Flask(__name__, template_folder="views")

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///employees.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(employee_blueprint, url_prefix="/")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
