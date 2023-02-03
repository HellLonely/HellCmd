import os
import bin.Deco as Deco
import bin.Operator as Operator
import bin.Help as Help

Deco.preset()

scape = False


def error():
    print ("Ha ocurrido un error en el siguiente módulo")

def clear():
    os.system ("cls") 

while scape == False:
    command = str(input("∇ "))
    print(" ")
    Operator.connect(command)
    print(" ")

    