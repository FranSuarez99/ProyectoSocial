import requests, csv, sys, os
from flask import *
from pyDriveFunct import *

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
        if request.form["btn"] == "!Comencemos!":
            return redirect(url_for('difficult_select'))
    return render_template('index.html')

#VISTA LOGIN PROFESOR
@app.route('/login', methods=['GET', 'POST'])
def login_view():
    if request.method == 'POST':
        if request.form["btn"] == "Iniciar sesión":
            password = request.form['pass']
            if password == master_password:
                return redirect(url_for('new_word_view'))
    return render_template('login.html')

#VISTA NUEVA PALABRA
@app.route('/palabra', methods=['GET', 'POST'])
def new_word_view():
    return render_template('new_word.html')

#VISTA SELECCION DIFICULTAD
@app.route('/start', methods=['GET', 'POST'])
def difficult_select():
    if request.method == 'POST':
        if request.form["btn"] == "¡Empecemos!":
            difficult = str(request.form.get('dif'))
            session['difficult'] = difficult
            return redirect(url_for('game_view'))
    return render_template('difficult.html')

#VISTA JUEGO NINO
@app.route('/game', methods=['GET', 'POST'])
def game_view():
    difficult = session.get('difficult', None)
    photo_source = None
    if request.method == 'POST':
        if request.form["btn"] == "¡Enviar!":
            num_sounds = int(request.form.get("letterNum"))
            file = open("salida.txt", "a")
            file.write(f'{num_sounds}\n')
            child_solution = []
            for i in range(num_sounds):
                name_box = f'select{i}_letter'
                sound = int(request.form.get(name_box))
                child_solution.append(sound)
            file.write(f'{child_solution}\n')
            file.close()
            #revisar solucion del nino
    return render_template('game.html', photo_source=photo_source)

if __name__ == "__main__":
    app.debug = True
    app.run()
