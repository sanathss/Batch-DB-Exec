import json

from database.connection import testConnect, executeFiles, readDBConfigDetails
from directory import getCustomDirectory, readDefaultPaths, retrieveFiles


def confirmationMessage():
    while(True):
        value = input("Confirm (Y/N): ") 
        if value in ['Y', 'y']:
            return True
        elif value in ['N', 'n']:
            return False

def pathSelection(pathSelection):
    while(True):
        try:
            value = input("Path selection: ") 
            if value in ['S', 's']:
                return getCustomDirectory()
            elif int(value) in [1, 2, 3]:
                return pathSelection[int(value)-1]
            else:
                print("\tEnter valid value.")
        except:
            print("\tEnter valid value.")

def startExecution():
    #Confirm Database Connection Details
    print('Database Connection details:')
    dbconfig = readDBConfigDetails()
    print("\t" + json.dumps(dbconfig))
    if confirmationMessage() == False:
        return 
    print('Connecting to Database...')
    if testConnect(dbconfig) == False:
        return
    print("\tDB connection to {} server is successful.".format(dbconfig['server']))
    #Find Path and list .sql files in order
    print('Select folder with .sql files:')
    defaultPaths = readDefaultPaths()
    index = 0
    for path in defaultPaths:
        print("\t{}    {}".format((index+1), path))
        index = index + 1
    print("\tS    Select custom folder directory.")
    sqlPath = pathSelection(defaultPaths)
    print("Searching {} ...".format(sqlPath))
    files = retrieveFiles(sqlPath)
    print("\tFound {} SQL file(s).".format(len(files)))
    for file in files:
        print("\t" + file)
    if confirmationMessage() == False:
        return 
    print('Executing...')
    executeFiles(dbconfig, sqlPath, files)
    print('Tasks Complete.')
