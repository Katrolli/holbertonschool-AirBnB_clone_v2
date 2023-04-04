from models import storage
from models.state import State
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

cities_by_state = {}
states = storage.all("State").values()
for state in states:
    print(state.cities)
