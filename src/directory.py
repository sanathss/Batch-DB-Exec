import os
from configparser import ConfigParser
from tkinter.filedialog import askdirectory

config = ConfigParser()

def getCustomDirectory():
    return askdirectory()

def readDefaultPaths():
    paths = []
    config.read('config.ini')
    if len(config.get('path', 'default1')) != 0:
        paths.append(config.get('path', 'default1'))
    if len(config.get('path', 'default2')) != 0:
        paths.append(config.get('path', 'default2'))
    if len(config.get('path', 'default3')) != 0:
        paths.append(config.get('path', 'default3'))
    return paths

def retrieveFiles(path):
    files = []
    for file in os.listdir(path):
        if file.endswith(".sql"):
            files.append(file)
    return files
