import json

conn = None

def connect():
    try:
        with open('dbconfig.json') as config_file:
            return json.load(config_file)
    except:
        print('Could not find dbconfig.json file.')