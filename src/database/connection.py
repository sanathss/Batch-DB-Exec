import json
import os

import pyodbc

def readDBConfigDetails():
    try:
        with open('dbconfig.json') as config_file:
            return json.load(config_file)
    except:
        print("\tCould not find dbconfig.json file.")

def connect(config):
    return pyodbc.connect(driver = '{SQL Server}',
                          server = config['server'],
                          database = config['database'],
                          uid = config['uid'],
                          pwd = config['pwd'])

def testConnect(config):
    try:
        connect(config)
        return True
    except:
        return False

def executeFiles(config, path, files):
    conn = connect(config)
    for file in files:
        with open(os.path.join(path, file)) as f:
            try:
                data = f.read()
                cursor = conn.cursor()
                cursor.execute(data)
                conn.commit()
                print("\t{}".format(file))
                print("\t\tSuccess")
            except Exception as e:
                print("\t{}".format(file))
                print("\t\tFailed - {}".format(e))
