import os
import bin.Help as Help
import bin.Directory as Dir


def connect(command):
    command = str(command)
    if command == 'help' or command =='--help':
        Help.helpmenu()
    elif command == 'cls' or command =='clear':
        os.system ("cls") 
    elif command == 'exit' or command =='close':
        exit()
    elif command == 'dir' or command =='ls':
        Dir.DirSimple()
    elif command.startswith('cd'):
        path = command.split(' ')[1]
        Dir.cd(path)

    
    

