from Connection import Connection
import pyodbc


class Eglise:
    def __init__(self, id_eglise, nom, argent):
        self._id_eglise = id_eglise
        self._nom = nom
        self._argent = argent

    def __json__(self):
        return {
            'id_eglise': self._id_eglise,
            'nom': self._nom,
            'argent': self._argent
        }
        
    @property  
    def id_eglise(self):
        return self._id_eglise

    @id_eglise.setter
    def id_eglise(self, value):
        self._id_eglise = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def argent(self):
        return self._argent

    @argent.setter
    def argent(self, value):
        self._argent = value
        
        
    @staticmethod
    def inserer(nom, argent):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO eglise (nom, argent) VALUES (?, ?)", (nom, argent))
            connection.connection.commit()
            print("Église insérée avec succès dans la base de données.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def update(id_eglise, nom, argent):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("UPDATE eglise SET nom = ?, argent = ? WHERE id = ?",
                           (nom, argent, id_eglise))
            connection.connection.commit()
            print("Église mise à jour avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def delete(id_eglise):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("DELETE FROM eglise WHERE id = ?", (id_eglise,))
            connection.connection.commit()
            print("Église supprimée avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererToutesLesEglises():
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM eglise"
            result = connection.recupererDonnees(query)
            connection.close()
            eglises = []
            for row in result:
                eglise = Eglise(row['id'], row['nom'], row['argent'])
                eglises.append(eglise)
            return eglises
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererParId(id_eglise):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM eglise WHERE id = ?"
            result = connection.recupererDonnees(query, (id_eglise,))
            connection.close()
            if result:
                eglise = Eglise(result[0]['id'], result[0]['nom'], result[0]['argent'])
                return eglise
            else:
                return None  
        except pyodbc.Error as e:
            raise e

    def recupererCroyants(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM croyant WHERE id_eglise = ?"
            result = connection.recupererDonnees(query, (self.id_eglise,))
            connection.close()
            croyants = []
            for row in result:
                from Croyant import Croyant

                croyant = Croyant(row['id'], row['nom'], row['id_eglise'], row['login'], row['mdp'], row['statut'])
                croyants.append(croyant)
            return croyants
        except pyodbc.Error as e:
            raise e
        
    def getPasteur(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM croyant WHERE id_eglise = ? AND statut = 'pasteur'"
            result = connection.recupererDonnees(query, (self.id_eglise,))
            connection.close()
            pasteurs = []
            for row in result:
                from Croyant import Croyant

                pasteur = Croyant(row['id'], row['nom'], row['id_eglise'], row['login'], row['mdp'], row['statut'])
                pasteurs.append(pasteur)
            return pasteurs
        except pyodbc.Error as e:
            raise e
        
        
    def getListeCaisseParId(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM caisse WHERE id_eglise = ?"
            result = connection.recupererDonnees(query, (self.id_eglise,))
            connection.close()
            caisses = []
            for row in result:
                from Caisse import Caisse
                caisse = Caisse(row['id'], row['id_eglise'], row['montant'], row['datetime'])
                caisses.append(caisse)
            return caisses
        except pyodbc.Error as e:
            raise e

    def getListeCaisseParDate(self, datetime):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM caisse WHERE id_eglise = ? AND datetime <= ?"
            result = connection.recupererDonnees(query, (self.id_eglise, datetime))
            connection.close()
            caisses = []
            for row in result:
                from Caisse import Caisse
                caisse = Caisse(row['id'], row['id_eglise'], row['montant'], row['datetime'])
                caisses.append(caisse)
            return caisses
        except pyodbc.Error as e:
            raise e
        
    def getListePretsAvantDatetime(self, datetime_precise):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM pret WHERE id_croyant IN (SELECT id FROM croyant WHERE id_eglise = ?) AND dateDemande <= ?"
            result = connection.recupererDonnees(query, (self.id_eglise, datetime_precise))
            connection.close()
            prets = []
            for row in result:
                from Pret import Pret
                pret = Pret(row['id'], row['id_croyant'], row['montant'], row['dateDemande'], row['dateObtention'])
                prets.append(pret)
            return prets
        except pyodbc.Error as e:
            raise e
        
    def getArgentActuel(self, datetime_precise):
        from Caisse import Caisse
        sumCaisse = Caisse.sommeMontantsParEgliseTotale(self.id_eglise, datetime_precise)
        from Pret import Pret
        sumPret = Pret.sommeMontantsParEglise(self.id_eglise, datetime_precise)
        return sumCaisse - sumPret
    
    @staticmethod
    def getPredictionEglise(id, dateDemande) :
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT TOP 1 * FROM prediction_eglise WHERE id_eglise = ? AND dateDemande <= ? ORDER BY dateDemande DESC"
            result = connection.recupererDonnees(query, (id, dateDemande))
            connection.close()  
            if len(result) > 0:
                return result[0]
        except pyodbc.Error as e:
            raise e
        return None
    