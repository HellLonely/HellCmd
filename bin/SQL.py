import mysql.connector

def connection():

    contadorTuplas = 0

    db_password = input("\nContraseña de la base de datos \nsql -> ")

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=db_password
    )

    db_cursor = db_connection.cursor()


    db_cursor.execute("show databases")

    for db in db_cursor:
        print(db)

    db_database = input("\nQue base de datos vas a usar? \nsql -> ")

    db_cursor.execute("use "+ db_database +";")

    querry = input("Introduce la consulta a realizar \nsql -> ")

    db_cursor.execute("\n"+ str(querry))


    for db in db_cursor:
        contadorTuplas = contadorTuplas + 1
        print(db)

    print("\n Cantidad de tulas: " +str(contadorTuplas)+ "\n")
