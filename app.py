from flask import Flask, redirect, render_template, request, redirect, url_for, session
from Caisse import Caisse
from Croyant import Croyant
from Eglise import Eglise
from Pret import Pret

app = Flask(__name__, static_url_path='/C:/Users/user/Documents/S4/PROG/EGLISE/')
app.secret_key = 'qwertyuiop0123456789'  

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/accueil')
def accueil():
    return render_template('accueil.html', Eglise=Eglise, Croyant=Croyant, session=session)

@app.route('/connexion', methods=['POST'])
def connexion():
    login = request.form['login']
    mdp = request.form['mdp']
    try:
        a = Croyant.connexion(login, mdp)
        if a:
            session['login'] = a._id_croyant
            session['statut'] = a._statut
            session['eglise'] = a._eglise.id_eglise
            return redirect('/accueil') 
    except Exception as e:
        return render_template('index.html', erreur=str(e))

@app.route('/deconnexion')
def deconnexion():
    # Supprimer toutes les sessions
    session.clear()
    return redirect('/')
      
@app.route('/listecroyant')
def listecroyant():
    
    eglise = Eglise.recupererParId(session['eglise'])
    croyants = eglise.recupererCroyants()
    return render_template('listecroyant.html', Eglise=Eglise, Croyant=Croyant, session=session, croyants=croyants)

@app.route('/listepret')
def listepret():
    if session['statut'] == 'pasteur':
        eglise = Eglise.recupererParId(session['eglise'])
        prets = eglise.getListePretsAvantDatetime('2050-01-01')
    else:
        croyant = Croyant.recupererParId(session['login'])
        prets = croyant.getListePrets()
    return render_template('listepret.html', Eglise=Eglise, Croyant=Croyant, session=session, prets=prets)


@app.route('/listecaisse')
def listecaisse():  
    eglise = Eglise.recupererParId(session['eglise'])
    caisses = eglise.getListeCaisseParId()
    return render_template('listecaisse.html', Eglise=Eglise, Croyant=Croyant, session=session, caisses=caisses)


@app.route('/formcaisse')
def formcaisse():  
    return render_template('formcaisse.html', Eglise=Eglise, Croyant=Croyant, session=session)

@app.route('/traitementcaisse', methods=['POST'])
def traitementcaisse():  
    date = request.form['date']
    montant = request.form['montant']
    try:
        Caisse.inserer(session['eglise'], montant, date)
        return render_template('formcaisse.html', Eglise=Eglise, Croyant=Croyant, session=session, succes='Insertion reussie') 
    except Exception as e:
        return render_template('formcaisse.html', Eglise=Eglise, Croyant=Croyant, session=session, erreur=str(e))


@app.route('/formpret')
def formpret():  
    return render_template('formpret.html', Eglise=Eglise, Croyant=Croyant, session=session)

@app.route('/traitementpret', methods=['POST'])
def traitementpret():  
    date = request.form['date']
    montant = request.form['montant']
    ##try:
    resultat = Pret.getDateObtenueEtReste(session['login'], session['eglise'], float(montant), date)
    dateobtenue = resultat[0]
    reste = resultat[1]
    
    return render_template('formpret.html', Eglise=Eglise, Croyant=Croyant, session=session, obtention=dateobtenue, date=date, montant=montant, reste=reste) 
    # except Exception as e:
    #     return render_template('formpret.html', Eglise=Eglise, Croyant=Croyant, session=session, erreur=str(e))
 
@app.route('/validationpret', methods=['POST'])
def validationpret():  
    datereserve = request.form['date']
    obtention = request.form['obtention']
    montant = request.form['montant']
    reste = request.form['reste']
    try:
        Pret.validationPret(session['login'], montant, datereserve, obtention, reste, session['eglise'])
        return render_template('formpret.html', succes='Validation reussie', Eglise=Eglise, Croyant=Croyant, session=session) 
    except Exception as e:
        return render_template('formpret.html', erreur=str(e), Eglise=Eglise, Croyant=Croyant, session=session)
    
@app.route('/aboutme')
def aboutme():  
    croyant = Croyant.recupererParId(session['login'])
    return render_template('apropos.html', Eglise=Eglise, Croyant=Croyant, croyant=croyant) 


if __name__ == "__main__":
    app.run(debug=True)