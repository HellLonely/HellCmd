import mysql.connector
import bin.Deco as Deco
import os
def clear():
    os.system ("cls")


def connection():
    clear()
    Deco.sql_module_deco()

    in_bd_system = 1

    contadorTuplas = 0

    db_password = input("\nContraseña de la base de datos \n🐬 -> ")

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=db_password
    )

    db_cursor = db_connection.cursor()

    print(" ")
    db_cursor.execute("show databases")

    for db in db_cursor:
        maintext = str(db).replace(',', ' ', 2).replace('(', ' ').replace(')', ' ')
        print(maintext, end="|")

    db_database = input("\nQue base de datos vas a usar? \n🐬 -> ")
    print(" ")

    db_cursor.execute("use "+ db_database +";")

    while in_bd_system == 1:
        contadorTuplas = 0
        querry = input("Introduce la consulta a realizar \n🐬 -> ")

        if querry == 'exit':
            print('exit')
        else:
            db_cursor.execute("\n" + str(querry))

            # Imprime las tuplas de la querry ↓

            print(" ")
            for db in db_cursor:
                contadorTuplas = contadorTuplas + 1
                maintext = str(db).replace(',', ' ', 2).replace('(', ' ').replace(')', ' ')
                print(maintext)

            print("\n Cantidad de tuplas: " + str(contadorTuplas) + "\n")



