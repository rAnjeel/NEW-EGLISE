import pyodbc

class Connection:
    # Paramètres de connexion par défaut
    SERVER = "DESKTOP-RCL8G7D\\SQLEXPRESS"
    DATABASE = "eglise"
    USERNAME = "sa"
    PASSWORD = "rabearison"
# f"UID={Connection.USERNAME};"
#                 f"PWD={Connection.PASSWORD};"
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            connection_string = (
                f"DRIVER={{ODBC Driver 17 for SQL Server}};"
                f"SERVER={Connection.SERVER};"
                f"DATABASE={Connection.DATABASE};"
                f"Trusted_Connection=yes;"
            )
            self.connection = pyodbc.connect(connection_string)
        except pyodbc.Error as e:
            raise e

    def close(self):
        if self.connection:
            self.connection.close()
        else:
            raise Exception("Aucune connexion active à la base de données.")

    def recupererDonnees(self, query, params=None):
        data = []
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            for row in cursor.fetchall():
                data.append(dict(zip(columns, row)))
            cursor.close()
        except pyodbc.Error as e:
            raise e
        return data

