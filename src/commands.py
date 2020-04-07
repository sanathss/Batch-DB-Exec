from database.connection import readDBConfigDetails

from tkinter.filedialog import askdirectory

def getFileDirectory():
    return askdirectory()

def startExecution():
    #Confirm Database Connection Details
    print(readDBConfigDetails())