import requests, csv, sys, os
from flask import *

master_password = 'incs2022'

#Configuramos la app de flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

#VISTA DE INDEX
@app.route('/', methods=['GET', 'POST'])
def index_view():
    if request.method == 'POST':
        if request.form["btn"] == "Soy Profesor":
            return redirect(url_for('login_view'))
    return render_template('index.html')

#VISTA LOGIN PROFESOR
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        password = request.form['pass']
        if request.form["btn"] == "Iniciar sesión":
            pass
    return render_template('login.html')

if __name__ == "__main__":
    app.debug = True
    app.run()
