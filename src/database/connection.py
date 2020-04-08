import json

import pyodbc

conn = None

def readDBConfigDetails():
    try:
        with open('dbconfig.json') as config_file:
            return json.load(config_file)
    except:
        print('Could not find dbconfig.json file.')

def connect(config):
    try:
        conn = pyodbc.connect(driver = '{SQL Server}',
                              server = config['server'],
                              database = config['database'],
                              uid = config['uid'],
                              pwd = config['pwd'])
        return True
    except:
        return False