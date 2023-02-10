import mysql.connector

def connection():

    contadorTuplas = 0

    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd=""
    )

    db_cursor = db_connection.cursor()
    db_cursor.execute("use traballadores;")

    querry = input("Introduce la consulta a realizar \n sql -> ")

    db_cursor.execute("\n"+ str(querry))


    for db in db_cursor:
        contadorTuplas = contadorTuplas + 1
        print(db)

    print("\n Cantidad de tulas: " +str(contadorTuplas)+ "\n")
