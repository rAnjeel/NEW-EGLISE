from datetime import datetime
from Connection import Connection
import pyodbc

class Caisse:
    def __init__(self, id_caisse, id_eglise, montant, datetime):
        self._id_caisse = id_caisse
        from Eglise import Eglise
        self._eglise = Eglise.recupererParId(id_eglise)
        self._montant = montant
        self._datetime = datetime

    def __json__(self):
        return {
            'id_caisse': self._id_caisse,
            'eglise': self._eglise.__json__(),
            'montant': self._montant,
            'datetime': self._datetime
        }


    @property
    def id_caisse(self):
        return self._id_caisse

    @id_caisse.setter
    def id_caisse(self, value):
        self._id_caisse = value

    @property
    def eglise(self):
        return self._eglise

    @eglise.setter
    def eglise(self, value):
        self._eglise = value

    @property
    def montant(self):
        return self._montant

    @montant.setter
    def montant(self, value):
        self._montant = value

    @property
    def datetime(self):
        return self._datetime

    @datetime.setter
    def datetime(self, value):
        self._datetime = value

    @staticmethod
    def inserer(id_eglise, montant, datetimey):
        try:
            date_obj = datetime.strptime(datetimey, '%Y-%m-%d')
            if date_obj.weekday() != 6:
                raise Exception("Veuillez inserer un dimanche.")
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO caisse (id_eglise, montant, datetime) VALUES (?, ?, ?)",
                           (id_eglise, montant, datetimey))
            connection.connection.commit()
            print("Entrée de caisse insérée avec succès dans la base de données.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def update(id_caisse, id_eglise, montant, datetime):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("UPDATE caisse SET id_eglise = ?, montant = ?, datetime = ? WHERE id = ?",
                           (id_eglise, montant, datetime, id_caisse))
            connection.connection.commit()
            print("Entrée de caisse mise à jour avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def delete(id_caisse):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("DELETE FROM caisse WHERE id = ?", (id_caisse,))
            connection.connection.commit()
            print("Entrée de caisse supprimée avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererCaisseParId(id_caisse):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM caisse WHERE id = ?"
            result = connection.recupererDonnees(query, (id_caisse,))
            connection.close()
            if result:
                return Caisse(result[0]['id'], result[0]['id_eglise'], result[0]['montant'], result[0]['datetime'])
            else:
                return None  # Aucune entrée de caisse trouvée avec cet ID
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererListeCaisse():
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM caisse"
            result = connection.recupererDonnees(query)
            connection.close()
            caisses = []
            for row in result:
                caisse = Caisse(row['id'], row['id_eglise'], row['montant'], row['datetime'])
                caisses.append(caisse)
            return caisses
        except pyodbc.Error as e:
            raise e
        
    @staticmethod
    def sommeMontantsParEglise(id_eglise, datetime_precise):
        try:
            from Pret import Pret
            annee = Pret.get_year_from_date(datetime_precise)
            dateDebut = str(annee)+'-01-01'
            connection = Connection()
            connection.connect()
            query = "SELECT SUM(montant) AS total FROM caisse WHERE id_eglise = ? AND datetime >= ? AND datetime <= ?"
            result = connection.recupererDonnees(query, (id_eglise, dateDebut, datetime_precise))
            connection.close()
            return result[0]['total'] if result and result[0]['total'] is not None else 0
        except pyodbc.Error as e:
            raise e
        
    def sommeMontantsParEgliseTotale(id_eglise, datetime_precise):
        try:
            from Pret import Pret
            annee = Pret.get_year_from_date(datetime_precise)
            dateDebut = str(annee)+'-01-01'
            print(f"la date de debut est {dateDebut}")
            connection = Connection()
            connection.connect()
            query = "SELECT SUM(montant) AS total FROM caisse WHERE id_eglise = ? AND datetime <= ?"
            result = connection.recupererDonnees(query, (id_eglise, datetime_precise))
            connection.close()
            return result[0]['total'] if result and result[0]['total'] is not None else 0
        except pyodbc.Error as e:
            raise e
