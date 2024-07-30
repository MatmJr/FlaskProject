from flask import Blueprint, render_template, request, redirect, abort
from models.employeeModel import EmployeeModel, db

employee_blueprint = Blueprint("employee", __name__)


@employee_blueprint.route("/")
def index():
    """
    Renderiza a página principal.

    Returns:
        str: O conteúdo HTML da página principal.
    """
    return render_template("mainpage.html")


@employee_blueprint.route("/create", methods=["GET", "POST"])
def create():
    """
    Renderiza a página de criação de funcionário e processa a criação de um novo funcionário.

    Returns:
        str: O conteúdo HTML da página de criação de funcionário se o método for GET.
        werkzeug.wrappers.response.Response: Redireciona para a página de dados se o método for POST.
    """

    if request.method == "GET":
        return render_template("createpage.html")

    if request.method == "POST":
        cpf = request.form["cpf"]
        name = request.form["name"]
        position = request.form["position"]
        employee = EmployeeModel(cpf=cpf, name=name, position=position)

        db.session.add(employee)
        db.session.commit()
        return redirect("/data")


@employee_blueprint.route("/data")
def DataView():
    """
    Renderiza a página que exibe a lista de funcionários.

    Returns:
        str: O conteúdo HTML da página com a lista de funcionários.
    """
    employee = EmployeeModel.query.all()
    return render_template("datalist.html", employee=employee)


@employee_blueprint.route("/data/<int:id>")
def findEmployee(id):
    """
    Renderiza a página que exibe os detalhes de um funcionário específico.

    Args:
        id (int): O ID do funcionário a ser encontrado.

    Returns:
        str: O conteúdo HTML da página com os detalhes do funcionário se encontrado.
        str: Mensagem indicando que o funcionário não existe se não encontrado.
    """
    employee = EmployeeModel.query.filter_by(id=id).first()
    if employee:
        return render_template("data.html", employee=employee)
    return f"Empregado com id={id} não existe"


@employee_blueprint.route("/data/<int:id>/update", methods=["GET", "POST"])
def update(id):
    """
    Renderiza a página de atualização de um funcionário e processa a atualização dos dados do funcionário.

    Args:
        id (int): O ID do funcionário a ser atualizado.

    Returns:
        str: O conteúdo HTML da página de atualização de funcionário se o método for GET.
        werkzeug.wrappers.response.Response: Redireciona para a página de detalhes do funcionário se o método for POST.
        str: Mensagem indicando que o funcionário não existe se o ID não for encontrado.
    """
    employee = EmployeeModel.query.get(id)
    if not employee:
        return "Empregado com id={id} não existe"

    if request.method == "POST":
        employee.cpf = request.form["cpf"]
        employee.name = request.form["name"]
        employee.position = request.form["position"]
        db.session.commit()
        return redirect(f"/data/{id}")

    return render_template("update.html", employee=employee)


@employee_blueprint.route("/data/<int:id>/delete", methods=["GET", "POST"])
def delete(id):
    """
    Renderiza a página de exclusão de um funcionário e processa a exclusão do funcionário.

    Args:
        id (int): O ID do funcionário a ser excluído.

    Returns:
        str: O conteúdo HTML da página de exclusão de funcionário se o método for GET.
        werkzeug.wrappers.response.Response: Redireciona para a página de lista de funcionários se o método for POST.
        werkzeug.exceptions.HTTPException: Retorna um erro 404 se o funcionário não for encontrado.
    """
    employee = EmployeeModel.query.filter_by(id=id).first()
    if request.method == "POST":
        if employee:
            db.session.delete(employee)
            db.session.commit()

            return redirect("/data")
        abort(404)
    return render_template("delete.html", employee=employee)
