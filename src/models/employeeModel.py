from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class EmployeeModel(db.Model):
    """
    Modela um empregado para armazenamento no banco de dados.

    Attributes:
        id (int): ID único do empregado.
        cpf (str): CPF único do empregado.
        name (str): Nome do empregado.
        position (str): Posição/cargo do empregado.
    """

    __tablename__ = "employee"

    id = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), unique=True)
    name = db.Column(db.String(100))
    position = db.Column(db.String(20))

    def __init__(self, cpf, name, position):
        """
        Inicializa um objeto EmployeeModel.

        Args:
            cpf (str): CPF do empregado.
            name (str): Nome do empregado.
            position (str): Posição/cargo do empregado.
        """
        self.cpf = cpf
        self.name = name
        self.position = position

    def __repr__(self):
        """
        Representação string do objeto EmployeeModel.

        Returns:
            str: Uma string no formato "{id}:{name}-{position}".
        """
        return f"{self.id}:{self.name}-{self.position}"
