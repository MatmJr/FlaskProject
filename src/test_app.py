import pytest
from app import app, db
from models.employeeModel import EmployeeModel


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        yield client
        # Limpar o banco em memória.
        with app.app_context():
            db.drop_all() 

def test_index(client):
    """ Teste da rota principal """
    test = client.get('/')
    assert test.status_code == 200
    assert b'Bem Vindos ao desafio CRUD' in test.data
    
def test_create_employeer(client):
    test = client.get('/create')
    test2 = client.post('/create', data={'cpf':'99999999999', 'name':'João do Teste', 'position':'Tester'}, follow_redirects=True)
    assert test.status_code == 200
    assert test2.status_code == 200
    
    with app.app_context():
        employeer = EmployeeModel.query.all()
        assert len(employeer) == 1
        assert employeer[0].name == 'João do Teste'
        assert employeer[0].cpf == '99999999999'
        assert employeer[0].position == 'Tester'
        
    # desafio: atingir 100% de cobertura nos testes 