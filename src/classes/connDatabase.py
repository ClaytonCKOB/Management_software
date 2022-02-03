import pyodbc
           
class connDatabase:
    def __init__(self, db_name):
        self.dbname = db_name
        self.conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\clayt\OneDrive\Documentos\Management_software\database\login.accdb;')
        self.cursor = self.conn.cursor()

    def insertProduct(self, pedido, cliente, modelo, colecao, cor, acionamento, largura, altura, tubo):
        self.cursor.execute('INSERT INTO pedido (pedido, cliente, modelo, colecao, cor, acionamento, largura, altura, tubo) '+
        'VALUES ('+pedido+', '+cliente+', '+modelo+', '+colecao+', '+cor+', '+acionamento+', '+largura+', '+altura+', '+tubo+')')

    def loginVerification(self, name, password):
        self.cursor.execute('SELECT userName, password FROM login')
        for user in self.cursor.fetchall():
            if name == user[0]:
                if password != user[1]:
                    return 0
                else: return 1