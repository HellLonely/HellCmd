import os

def DirSimple():
    pathfile = open('bin/path.txt')
    path = str(pathfile.readline())
    with os.scandir(path) as ficheros:
        print(path)
        for fichero in ficheros:
            fold = '  🗁'
            folder = '.' in fichero.name
            if folder == True:
                fold = " 📝"

            print(" ↳ " + fichero.name + fold)

def cd(path):
    if path.startswith("/"):
        # mark = path[1:]
        pathfile = open('bin/path.txt')
        pathorigin = str(pathfile.readline())
        pathfile = open('bin/path.txt', 'w')
        pathfile.write(pathorigin+path)
        print("Te has movido con exito a la carpeta "+pathorigin+path)
        pathfile.close()
    elif path.startswith(".."):
        pathfile = open('bin/path.txt')
        pathorigin = str(pathfile.readline())
        paths = pathorigin.split('/')[0]
        pathfile = open('bin/path.txt', 'w')
        print("Te has movido con exito al disco "+paths+":")
        pathfile.write(str(paths))
        pathfile.close()
    elif path == ('root'):
        pathfile = open('bin/path.txt')
        pathorigin = str(pathfile.readline())
        paths = pathorigin.split(':')[0]
        pathfile = open('bin/path.txt', 'w')
        pathfile.write(str(str(paths)+":"))
        print("Te has movido con exito al disco "+paths+":")
        pathfile.close()

