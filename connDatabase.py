import pyodbc

def login(name, password):
    con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\clayt\OneDrive\Documentos\integration_python_and_MS-Access\database\login.accdb;'
    conn = pyodbc.connect(con_string)

    cursor = conn.cursor()

    cursor.execute('SELECT userName, password FROM login')
    
    for user in cursor.fetchall():
        if name == user[0]:
            if password != user[1]:
                return 0
            else: return 1
            
            