from Connection import Connection
import pyodbc
from datetime import datetime, timedelta

class Pret:
    def __init__(self, id_pret, id_croyant, montant, date_demande, date_obtention):
        self._id_pret = id_pret
        from Croyant import Croyant
        self._croyant = Croyant.recupererParId(id_croyant)
        self._montant = montant
        self._date_demande = date_demande
        self._date_obtention = date_obtention

    def __json__(self):
        return {
            'id_pret': self._id_pret,
            'croyant': self._croyant.__json__(),
            'montant': self._montant,
            'date_demande': self._date_demande,
            'date_obtention': self._date_obtention
        }
        
    # Getters and setters
    @property
    def id_pret(self):
        return self._id_pret

    @property
    def croyant(self):
        return self._croyant

    @croyant.setter
    def croyant(self, value):
        self._croyant = value

    @property
    def montant(self):
        return self._montant

    @montant.setter
    def montant(self, value):
        self._montant = value

    @property
    def date_demande(self):
        return self._date_demande

    @date_demande.setter
    def date_demande(self, value):
        self._date_demande = value

    @property
    def date_obtention(self):
        return self._date_obtention

    @date_obtention.setter
    def date_obtention(self, value):
        self._date_obtention = value

    # CRUD methods
    @staticmethod
    def inserer(id_croyant, montant, date_demande, date_obtention):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO pret (id_croyant, montant, dateDemande, dateObtention) VALUES (?, ?, ?, ?)",
                           (id_croyant, montant, date_demande, date_obtention))
            connection.connection.commit()
            print("Prêt inséré avec succès dans la base de données.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def inserer(id_croyant, montant, date_demande, date_obtention, reste, id_eglise):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO pret (id_croyant, montant, dateDemande, dateObtention) VALUES (?, ?, ?, ?)",
                           (id_croyant, montant, date_demande, date_obtention))
            connection.connection.commit()
            print("Prêt inséré avec succès dans la base de données.")
            cursor.execute("INSERT INTO prediction_eglise (id_eglise, reste, dateDemande, dateObtention) VALUES (?, ?, ?, ?)",
                           (id_eglise, reste, date_demande, date_obtention))
            connection.connection.commit()
            print("Prediction insérée avec succès dans la base de données.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def update(id_pret, id_croyant, montant, date_demande, date_obtention):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("UPDATE pret SET id_croyant = ?, montant = ?, dateDemande = ?, dateObtention = ? WHERE id = ?",
                           (id_croyant, montant, date_demande, date_obtention, id_pret))
            connection.connection.commit()
            print("Prêt mis à jour avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def delete(id_pret):
        try:
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("DELETE FROM pret WHERE id = ?", (id_pret,))
            connection.connection.commit()
            print("Prêt supprimé avec succès.")
            connection.close()
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererPretParId(id_pret):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM pret WHERE id = ?"
            result = connection.recupererDonnees(query, (id_pret,))
            connection.close()
            if result:
                pret = Pret(result[0]['id'], result[0]['id_croyant'], result[0]['montant'], result[0]['dateDemande'], result[0]['dateObtention'])
                return pret
            else:
                return None  # Aucun prêt trouvé avec cet ID
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def recupererTousLesPrets():
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT * FROM pret"
            result = connection.recupererDonnees(query)
            connection.close()
            prets = []
            for row in result:
                pret = Pret(row['id'], row['id_croyant'], row['montant'], row['dateDemande'], row['dateObtention'])
                prets.append(pret)
            return prets
        except pyodbc.Error as e:
            raise e
        
    @staticmethod
    def sommeMontantsParEglise(id_eglise, datetime_precise):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT SUM(montant) AS total FROM pret WHERE id_croyant IN (SELECT id FROM croyant WHERE id_eglise = ?)  AND dateDemande <= ?"
            result = connection.recupererDonnees(query, (id_eglise, datetime_precise))
            connection.close()
            return result[0]['total'] if result and result[0]['total'] is not None else 0
        except pyodbc.Error as e:
            raise e

    @staticmethod
    def numero_dimanche_annee(date):
        if not isinstance(date, datetime):
            date = datetime.strptime(date, '%Y-%m-%d')

        while date.weekday() != 6:
            date -= timedelta(days=1)

        num_semaine = date.strftime('%U')

        return int(num_semaine)  
    
    @staticmethod
    def nth_sunday_of_year(N, year):
        first_day = datetime(year, 1, 1)
        first_sunday = first_day + timedelta(days=(6 - first_day.weekday()))
        nth_sunday = first_sunday + timedelta(weeks=N - 1)
        return nth_sunday.strftime('%Y-%m-%d')
    
    @staticmethod
    def get_year_from_date(date_string):
        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        year = date_object.year
        return year
    
    @staticmethod
    def count_sundays_in_year(year):
        # Le premier jour de l'année
        date = datetime(year, 1, 1)  # Utilisez datetime pour créer une date
        # Le dernier jour de l'année
        end_date = datetime(year, 12, 31)
        
        count = 0
        while date <= end_date:
            if date.weekday() == 6:  # Dimanche
                count += 1
            date += timedelta(days=1)  # Incrémentez la date d'un jour
        
        return count
    
    @staticmethod
    def getMontantDimanche(id_eglise, dimanche):
        try:
            connection = Connection()
            connection.connect()
            query = "SELECT SUM(montant) as montants FROM caisse where id_eglise=? AND datetime = ?"
            result = connection.recupererDonnees(query, (id_eglise, dimanche))
            connection.close()
            if result and len(result) > 0 and result[0]['montants'] is not None:
                return result[0]['montants']

            else:
                connection = Connection()
                connection.connect()
                query = "SELECT SUM(montant) as montants FROM estimation where id_eglise=? AND dimanche = ?"
                result = connection.recupererDonnees(query, (id_eglise, dimanche))
                connection.close()
                return result[0]['montants']
        except pyodbc.Error as e:
            raise e
        
    
    @staticmethod
    def getProportion(id_eglise, dateDemande):
        nieme = Pret.numero_dimanche_annee(dateDemande)
        annee = Pret.get_year_from_date(dateDemande)
        date = Pret.nth_sunday_of_year(nieme, annee - 1)
        from Caisse import Caisse
        sommeannee = Caisse.sommeMontantsParEglise(id_eglise, dateDemande)
        sommeannee_1 = Caisse.sommeMontantsParEglise(id_eglise, date)
        proportion = sommeannee / sommeannee_1
        return proportion
    
    ## ilay teo alohany
    @staticmethod
    def dimanche_le_plus_proche(date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        jour_semaine = date.weekday()
        jours_a_soustraire = (jour_semaine + 1) % 7
        dimanche = date - timedelta(days=jours_a_soustraire)
        return dimanche.strftime("%Y-%m-%d")
       
       
    @staticmethod
    def prochain_dimanche(date_str):
        date = datetime.strptime(date_str, "%Y-%m-%d")
        if date.weekday() == 6:
            date += timedelta(days=7)
        else :
            while date.weekday() != 6: 
                date += timedelta(days=1)
        return date.strftime("%Y-%m-%d")
    

    @staticmethod   
    def has_53_sundays(year):
        sunday_count = 0
        current_date = datetime(year, 1, 1)
        while current_date.year == year:
            if current_date.weekday() == 6:  # Dimanche
                sunday_count += 1
            current_date += timedelta(days=1)  # Passer au jour suivant
        return sunday_count == 53
    
    @staticmethod
    def find_closest_year_with_53_sundays(year):
        year -= 1
        while year > 0:  
            if Pret.has_53_sundays(year):
                return year
            year -= 1
        return None  

    @staticmethod
    def getDateDebut(id_eglise, dateDemande):
        from Eglise import Eglise
        eglise = Eglise.getPredictionEglise(id_eglise, dateDemande)
        if eglise is None or (eglise['dateObtention'] <= (datetime.strptime(dateDemande, '%Y-%m-%d')).date()):
            return Pret.dimanche_le_plus_proche(dateDemande)
        else :
            return eglise['dateObtention']
    
    @staticmethod
    def getMontantDebut(id_eglise, dateDemande):
        from Eglise import Eglise
        eglise = Eglise.getPredictionEglise(id_eglise, dateDemande)
        if eglise is None or (eglise['dateObtention'] <= (datetime.strptime(dateDemande, '%Y-%m-%d')).date()):
            from Caisse import Caisse
            from Eglise import Eglise
            e = Eglise.recupererParId(id_eglise)
            return e.getArgentActuel(dateDemande)
        else : 
            return eglise['reste']
        
    @staticmethod    
    def getDateObtenueEtReste(id_croyant, id_eglise, montant, dateDemande):
        from Croyant import Croyant
        croyant = Croyant.recupererParId(id_croyant)
        if croyant.getBapteme() is None:
            raise Exception("Vous ne pouvez pas faire de pret car vous n'avez pas encore fait de bapteme.")
        if croyant.getCommunion() is None:
            raise Exception("Vous ne pouvez pas faire de pret car vous n'avez pas encore fait de communion.")
        if croyant.getMatrimoniale() == 'divorce(e)':
            raise Exception("Vous ne pouvez pas faire de pret a cause de votre situation matrimoniale.")
        lastPret = croyant.getPretRecent()
        if lastPret is not None and lastPret.date_obtention > (datetime.strptime(dateDemande, '%Y-%m-%d')).date() :
            raise Exception("Vous ne pouvez pas faire de pret car vous n'avez pas encore recu votre dernier pret.") 
        nieme = Pret.numero_dimanche_annee(dateDemande)
        annee = Pret.get_year_from_date(dateDemande)
        proportion = Pret.getProportion(id_eglise, Pret.nth_sunday_of_year(nieme, annee))
        dateDebut = Pret.getDateDebut(id_eglise, dateDemande)
        montantDebut = Pret.getMontantDebut(id_eglise, dateDemande)
        dateFinale = dateDebut
        
        nieme = Pret.numero_dimanche_annee(dateFinale.strftime('%Y-%m-%d'))
        annee = Pret.get_year_from_date(dateFinale.strftime('%Y-%m-%d'))
        resteFinale = montantDebut - montant
        if(montantDebut >= montant) : 
            dateFinale = dateDemande
            resteFinale = montantDebut - montant
        print(f"pour le moment, la datefinale est {dateFinale} et le reste est {resteFinale}")
        while montantDebut < montant:
            nieme+= 1
            if (nieme > 52 and not Pret.has_53_sundays(annee)) or (nieme >53 and Pret.has_53_sundays(annee)):
                nieme = 1
                annee += 1
            if nieme == 53 : 
                annee53 = Pret.find_closest_year_with_53_sundays(annee)
                dateDebutAvant  = Pret.nth_sunday_of_year(53, annee53)
                temp = Pret.getMontantDimanche(id_eglise, dateDebutAvant)
                montantDebut += temp * proportion 
            else:
                dateDebutAvant = Pret.nth_sunday_of_year(nieme, annee-1)
                temp = Pret.getMontantDimanche(id_eglise, dateDebutAvant)
                montantDebut += temp * proportion 
            dateDebut = Pret.nth_sunday_of_year(nieme, annee)
            dateFinale = dateDebut
            resteFinale = montantDebut - montant
            print(f"pour le moment, l'estimation est {temp*proportion}. le montant est a {montantDebut}, la datefinale est {dateFinale} et le reste est {resteFinale}")
            
            connection = Connection()
            connection.connect()
            cursor = connection.connection.cursor()
            cursor.execute("INSERT INTO estimation (id_eglise, montant, dimanche) VALUES (?, ?, ?)",
                           (id_eglise, temp * proportion, dateFinale))
            connection.connection.commit()
            connection.close()

        return [dateFinale, resteFinale]
    
#resultat = Pret.getDateObtenueEtReste(1, 1, 2000000, '2024-02-27')
    @staticmethod
    def validationPret(id_croyant, montant, dateDemande, dateFinale, resteFinale, id_eglise):
        Pret.inserer(id_croyant, montant, dateDemande, dateFinale, resteFinale, id_eglise)
        
    

