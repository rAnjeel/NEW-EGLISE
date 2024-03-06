from flask import Flask, render_template
from Connection import Connection

# Définition de l'objet app de Flask
app = Flask(__name__)

class Main:
    def __init__(self, app):
        self.app = app
        self.connection = Connection(
            server="DESKTOP-A7362A9\\SQLEXPRESS",
            database="eglise",
            username="sa",
            password="sqlserver"
        )
        self.connection.connect()

    def setup_routes(self):
        @self.app.route('/')
        def index():
            data = self.connection.fetch_data()
            return render_template('index.html', data=data)

if __name__ == '__main__':
    main = Main(app)
    main.setup_routes()
    app.run(debug=True, port=8000)
