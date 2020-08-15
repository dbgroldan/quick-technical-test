import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv()

_config = {
    'db_tables_path': os.getenv('DB_TABLES_PATH'),
    'db_config': (os.getenv('DB_NAME'), os.getenv('DB_USER'),
        os.getenv('DB_HOST'), os.getenv('DB_PORT'),
        os.getenv('DB_PASSWORD')),
    'port_http': os.getenv("PORT_HTTP"),
    'host': os.getenv("HOST")
}

def getConfig():
    return _config
