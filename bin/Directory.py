import os
import time

def DirSimple():
    pathfile = open('bin/path.txt')
    path = str(pathfile.readline())
    with os.scandir(path) as ficheros:
        print("Ruta → "+ path+"\n")
        contadorArchivos = 0
        space = " "

        print("   Nombre" + space*22+"🧱 Peso")
        print("   ------"+ space*22+"-------")

        for fichero in ficheros:
            contadorArchivos += 1
            fold = '  🗁'
            folder = '.' in fichero.name
            if folder == True:
                fold = " 📝"

            numeroLetrasTexto = len(fichero.name)
            numeroLetrasPonerTexto = 25 - int(numeroLetrasTexto)

            fileSizeHeight = os.stat(fichero).st_size

            ti_m = os.path.getmtime(fichero)
            m_ti = time.ctime(ti_m)

            #print(" ↳ " + fichero.name + fold + "                   🖊️ : "+ m_ti+"       🧱 Peso: " + str(fileSizeHeight) + " Bites")
            print(" ↳ " + fichero.name + fold + space * numeroLetrasPonerTexto + str(fileSizeHeight))
        print("\n Elementos : " + str(contadorArchivos))

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



def disckManager():

    outputDiskManager = os.system('fsutil fsinfo drives')

