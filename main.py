from db_init import init_db
from config_store import get_config

init_db()
print("Current Config:", get_config())

