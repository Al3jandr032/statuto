
import statuto
import json

mapping = {"other": [{
            "key": "preprocessing_queue",
            "mapping": lambda _key: _key.strip(" []\n").split(",")
        }]}
config = statuto.load("../config/dbconfig.ini","ini", mapping, asDict=False)
# print type(config)
# print config
# print dir(config)
# print config.keys()
# print json.dumps(config)

# config = statuto.load("../config/dbconfig.json","json", mapping)
# print type(config)
# print config.keys()
# print json.dumps(config)

# config = statuto.load("../config/dbconfig.yaml","yaml", mapping)
# print type(config)
# print config.keys()
# print json.dumps(config)

# config = statuto.load("../config/dbconfig.xml","xml", mapping)
# print type(config)
# print config.keys()
# print json.dumps(config)