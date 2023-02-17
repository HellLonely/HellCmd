import os
import bin.Help as Help
import bin.Directory as Dir
import bin.SQL as SQL
import bin.ImgConverter as IMG


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
    elif command == 'disk' or command =='managerDisk':
        Dir.disckManager()
    elif command == 'sicm' or command =='--image':
        IMG.start_module()
    elif command.startswith('cd'):
        path = command.split(' ')[1]
        Dir.cd(path)
    elif command == 'sql' or command == '--sql':
        SQL.connection()

    else:
        print("❌ | Comando no valido ")
        print("\n     Prueba a usar 'help' o '--help'")

    
    

