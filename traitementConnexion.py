from flask import Flask, render_template, request, redirect, url_for, session
from Croyant import Croyant

app = Flask(__name__)
app.secret_key = 'qwertyuiop0123456789'  

@app.route('/connexion', methods=['POST'])
def connexion():
    login = request.form['login']
    mdp = request.form['mdp']
    
    try:
        a = Croyant.connexion(login, mdp)
        if a :
            session['login'] = a
            return redirect(url_for('/accueil'))  
    except Exception as e:
        # Erreur lors de la connexion, renvoie l'erreur à la page de connexion
        return render_template('/', erreur=str(e))

if __name__ == '__main__':
    app.run(debug=True)
