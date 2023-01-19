import os
import bin.Help as Help

def connect(command):
    command = str(command)
    if command == 'help' or command =='--help':
        Help.helpmenu()
    elif command == 'cls' or command =='clear':
        os.system ("cls") 


