from tkinter.filedialog import askdirectory

from configparser import ConfigParser
config = ConfigParser()

def getCustomDirectory():
    return askdirectory()

#Find Path and list .sql files in order
config.read('config.ini')
print(config.get('path', 'default1'))