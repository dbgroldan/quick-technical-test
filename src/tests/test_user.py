import pytest, sys, os

top_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(top_dir)

from database.postg_connection import Connection
from user.user_service import UserService
from config.settings import getConfig

user_test = {
    "first_name": "Test",
    "last_name": "Doe",
    "email": "user_test@example.com",
    "password": "SECRET",
    "age": 23,
    "image": "image.svg"
}

@pytest.fixture()
def env_db_props():
    db_config = getConfig().get('db_config')
    yield db_config

@pytest.fixture()
def connection_postgres(env_db_props):
    db_config = 'dbname=%s user=%s host=%s port=%s password=%s'%env_db_props
    connection = Connection(db_config)
    conn, _ = connection.getConnection()
    yield conn
    conn.close()

@pytest.fixture()
def cursor_postgres(connection_postgres):
    cursor = connection_postgres.cursor()
    yield cursor
    connection_postgres.rollback()

@pytest.fixture()
def max_user(cursor_postgres):
    query = """select max(id) from user_schema.user;"""
    cursor_postgres.execute(query)
    resp = cursor_postgres.fetchone()[0]
    yield str(resp)

@pytest.fixture()
def user_service_control():
    user_control = UserService()
    yield user_control

def test_add_user_service(user_service_control, connection_postgres):
    code, _ = user_service_control.add_user(user_test)
    connection_postgres.rollback();
    assert  code == 201 or code == 409

def test_update_user_service(user_service_control, max_user):
    data = { 'email': 'mail@mail.com', 'image': 'x_image.svg'}
    code, _ = user_service_control.update_user(max_user, data)
    assert  code == 200 or code == 409

def test_get_all_user_service(user_service_control):
    code, _ = user_service_control.get_all()
    assert  code == 200

def test_get_user_service(user_service_control, max_user):
    code, _ = user_service_control.get(max_user)
    assert  code == 200

def test_delete_user_service(user_service_control, max_user):
    code, _ = user_service_control.delete(max_user)
    assert  code == 200
