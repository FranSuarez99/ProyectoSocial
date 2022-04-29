from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import requests, csv, sys, os
from flask import *

from pyDriveFunct import *

master_password = 'incs2022'

#Configuramos la app de flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

authG = GoogleAuth()
authG.LocalWebserverAuth()

drive = GoogleDrive(authG)

fileName1 = 'words.txt'
fileName2 = 'solutions.txt'
fileName3 = 'difficulty.txt'
fileName4 = 'imgSource.txt'

wordsID, solutionsID, difficultyID, imgSourceID = None, None, None, None

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:#check every file on Drive and saves the ID of the needed files
  #print('title: %s, id: %s' % (file1['title'], file1['id']))
  if file1['title'] == fileName1:
      wordsID = file1['id']
  if file1['title'] == fileName2:
      solutionsID = file1['id']
  if file1['title'] == fileName3:
      difficultyID = file1['id']
  if file1['title'] == fileName4:
      imgSourceID = file1['id']




words = dFile(wordsID,fileName1)
solutions = dFile(solutionsID,fileName2)
difficulty = dFile(difficultyID,fileName3)
imgSource = dFile(imgSourceID,fileName4)

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
    word = None#palabra
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
            
            trueSolution = getSolution(word, words, solutions)
    return render_template('game.html', photo_source=photo_source)

if __name__ == "__main__":
    app.debug = True
    app.run()
