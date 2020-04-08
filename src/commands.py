from database.connection import readDBConfigDetails, connect

def confirmationMessage():
    while(True):
        value = input("Confirm (Y/N): ") 
        if value in ['Y', 'y']:
            return True
        elif value in ['N', 'n']:
            return False

def startExecution():
    #Confirm Database Connection Details
    print('Database Connection details:')
    dbconfig = readDBConfigDetails()
    print(dbconfig)
    if confirmationMessage() == False:
        return 
    print('Connection to Database...')
    if connect(dbconfig) == False:
        return
    print('DB connection to {} server is successful.'.format(dbconfig['server']))
