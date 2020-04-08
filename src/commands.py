from database.connection import readDBConfigDetails

from tkinter.filedialog import askdirectory

def getFileDirectory():
    return askdirectory()

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
    print(readDBConfigDetails())
    if confirmationMessage() == False:
        return 