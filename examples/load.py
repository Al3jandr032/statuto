
import statuto
mapping = {"other": [{
            "key": "preprocessing_queue",
            "mapping": lambda _key: _key.strip(" []\n").split(",")
        }]}
config = statuto.load("../config/dbconfig.ini","ini", mapping)
print config