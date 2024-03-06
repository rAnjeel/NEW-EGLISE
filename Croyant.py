from Connection import Connection
import pyodbc



class Croyant:
    def __init__(self, id_croyant, nom, eglise, login, mdp, statut):
        self._id_croyant = id_croyant
        self._nom = nom
        from Eglise import Eglise

        self._eglise = Eglise.recupererParId(eglise)
        self._login = login
        self._mdp = mdp
        self._statut = statut

    def __json__(self):
        return {
            'id_croyant': self._id_croyant,
            'nom': self._nom,
            'eglise': self._eglise.__json__(),
            'login': self._login,
            'mdp': self._mdp,
            'statut': self._statut
        }
    
    @property
    def id_croyant(self):
        return self._id_croyant

    @id_croyant.setter
    def id_croyant(self, value):
        self._id_croyant = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def eglise(self):
        return self._eglise

    @eglise.setter
    def eglise(self, value):
        self._eglise = value

    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @property
    def mdp(self):
        return self._mdp

    @mdp.setter
    def mdp(self, value):
        self._mdp = value

    @property
    def statut(self):
        return self._statut

    @statut.setter
    def statut(self, value):
        self._statut = value

        
    @staticmethod
    def inserer(nom, eglise, login, mdp, statut):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO croyant (nom, id_eglise, login, mdp, statut) VALUES (?, ?, ?, ?, ?)",
                           (nom, eglise, login, mdp, statut))
            connection.connection.commit()
            print("Croyant inséré avec succès dans la base de données.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def update(id_croyant, nom, eglise, login, mdp, statut):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("UPDATE croyant SET nom = ?, id_eglise = ?, login = ?, mdp = ?, statut = ? WHERE id = ?",
                           (nom, eglise, login, mdp, statut, id_croyant))
            connection.connection.commit()
            print("Croyant mis à jour avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def delete(id_croyant):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("DELETE FROM croyant WHERE id = ?", (id_croyant,))
            connection.connection.commit()
            print("Croyant supprimé avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererTousLesCroyants():
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM croyant"
            results = connection.recupererDonnees(query)
            connection.close()
            croyants = []
            for result in results:
                croyant = Croyant(result['id'], result['nom'], result['id_eglise'], result['login'], result['mdp'], result['statut'])
                croyants.append(croyant)
            return croyants
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererParId(id_croyant):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM croyant WHERE id = ?"
            result = connection.recupererDonnees(query, (id_croyant,))
            connection.close()
            if result:
                croyant = Croyant(result[0]['id'], result[0]['nom'], result[0]['id_eglise'], result[0]['login'], result[0]['mdp'], result[0]['statut'])
                return croyant
            else:
                return None  # Aucun croyant trouvé avec cet ID
        except pyodbc.Error as e:
            raise e
        
    @staticmethod   
    def connexion(login, mdp):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM croyant WHERE login = ?"
            result = connection.recupererDonnees(query, (login))
            connection.close()
            if result:
                croyant = Croyant(result[0]['id'], result[0]['nom'], result[0]['id_eglise'], result[0]['login'], result[0]['mdp'], result[0]['statut'])
                if mdp == croyant._mdp:
                    return croyant
                else:
                    raise Exception("Mot de passe invalide.")
            else:
                raise Exception("Login invalide ou inexistant.")
        except pyodbc.Error as e:
            raise e

    def getListePrets(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM pret WHERE id_croyant = ?"
            result = connection.recupererDonnees(query, (self.id_croyant))
            connection.close()
            prets = []
            for row in result:
                from Pret import Pret
                pret = Pret(row['id'], row['id_croyant'], row['montant'], row['dateDemande'], row['dateObtention'])
                prets.append(pret)
            return prets
        except pyodbc.Error as e:
            raise e
        
        
    def getMatrimoniale(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT matrimoniale FROM situation WHERE id_croyant = ?"
            result = connection.recupererDonnees(query, (self.id_croyant))
            connection.close()
            prets = []
            if result:
                matrimoniale = result[0]['matrimoniale']
                return matrimoniale
            else:
                return None
        except pyodbc.Error as e:
            raise e
        
        
    def getBapteme(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT bapteme FROM situation WHERE id_croyant = ?"
            result = connection.recupererDonnees(query, (self.id_croyant))
            connection.close()
            prets = []
            if result[0]['bapteme'] is not None:
                bapteme = result[0]['bapteme']
                return bapteme
            else:
                return None
        except pyodbc.Error as e:
            raise e
        
        
    def getCommunion(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT communion FROM situation WHERE id_croyant = ?"
            result = connection.recupererDonnees(query, (self.id_croyant))
            connection.close()
            prets = [] 
            if result[0]['communion'] is not None:
                communion = result[0]['communion']
                return communion
            else:
                return None
        except pyodbc.Error as e:
            raise e

    def getPretRecent(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT TOP 1 * FROM pret WHERE id_croyant = ? ORDER BY dateObtention DESC"
            result = connection.recupererDonnees(query, (self.id_croyant,))
            connection.close()
            if result:
                from Pret import Pret
                pret = Pret(result[0]['id'], result[0]['id_croyant'], result[0]['montant'], result[0]['dateDemande'], result[0]['dateObtention'])
                return pret
            else:
                return None
        except pyodbc.Error as e:
            raise e
        
        
    def getListePrets(self):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM pret WHERE id_croyant = ?"
            result = connection.recupererDonnees(query, (self.id_croyant,))
            connection.close()
            prets = []
            for row in result:
                from Pret import Pret
                pret = Pret(row['id'], row['id_croyant'], row['montant'], row['dateDemande'], row['dateObtention'])
                prets.append(pret)
            return prets
        except pyodbc.Error as e: 
            raise e
        
    @staticmethod
    def inserer(nom, eglise, login, mdp, statut):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO croyant (nom, id_eglise, login, mdp, statut) VALUES (?, ?, ?, ?, ?)",
                           (nom, eglise, login, mdp, statut))
            connection.connection.commit()
            print("Croyant inséré avec succès dans la base de données.")
            connection.close()
        except pyodbc.Error as e:
            raise e
