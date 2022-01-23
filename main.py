import pyodbc

name = input()
password = input()


try:
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\clayt\OneDrive\Documentos\integration_python_and_MS-Access\database\login.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()

    newUser = (
        (2, 'john', '4321', 'john@gmail.com'),
        (3, 'thomas', '4341', 'thomas@gmail.com')
    )

    cursor.execute('SELECT userName, password FROM login')
    
    for user in cursor.fetchall():
        if name == user[0]:
            if password == user[1]:
                print("LOGIN ACCEPTED")
            else: print("Wrong password")

except pyodbc.Error as e:
    print('ERROR in connection: ', e)