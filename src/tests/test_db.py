import pytest, sys, os

top_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(top_dir)
from database.postg_connection import Connection
from config.settings import getConfig

@pytest.fixture()
def env_db_props():
    db_config = getConfig().get('db_config')
    yield db_config

@pytest.fixture()
def env_table_props():
    db_tables_path = getConfig().get('db_tables_path')
    yield db_tables_path

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

def test_table_user_exist(cursor_postgres):
    query = """SELECT table_name
        FROM information_schema.tables
        WHERE table_schema = 'user_schema'
        ORDER BY table_name;
        """
    cursor_postgres.execute(query)
    resp = cursor_postgres.fetchall()
    assert  resp
