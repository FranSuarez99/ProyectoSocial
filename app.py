from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import requests, csv, sys, os
from flask import *

from pyDriveFunct import *

master_password = 'incs2022'
fileName1 = 'words.txt'
fileName2 = 'solutions.txt'
fileName3 = 'difficulty.txt'
fileName4 = 'imgSource.txt'

#Configuramos la app de flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Configuracion con Google Drive
authG = GoogleAuth()
authG.LocalWebserverAuth()
drive = GoogleDrive(authG)

wordsID, solutionsID, difficultyID, imgSourceID = None, None, None, None

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:#check every file on Drive and saves the ID of the needed files
  if file1['title'] == fileName1:
      wordsID = file1['id']
  if file1['title'] == fileName2:
      solutionsID = file1['id']
  if file1['title'] == fileName3:
      difficultyID = file1['id']
  if file1['title'] == fileName4:
      imgSourceID = file1['id']

words = dFile(wordsID,fileName1, drive)
difficulty = dict(zip(words, list(map(int, dFile(difficultyID,fileName3, drive)))))
solutions = dict(zip(words, list(map(lambda x : list(map(int, x.split(','))), dFile(solutionsID,fileName2, drive))))) #python tu papa
imgSource = dict(zip(words, dFile(imgSourceID,fileName4, drive)))

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
            difficult = int(str(request.form.get('dif')))
            session['difficult'] = difficult
            wordsList = getWords(difficult, difficulty)
            session['wordsList'] = wordsList
            return redirect(url_for('game_view'))
    return render_template('difficult.html')

#VISTA JUEGO NINO
@app.route('/game', methods=['GET', 'POST'])
def game_view():
    difficult = session.get('difficult', None)
    wordsList = session.get('wordsList', None)
    if len(wordsList) != 0:
        word = wordsList.pop()
    else:
        wordsList = getWords(difficult, difficulty)
        word = wordsList.pop()
    session['wordsList'] = wordsList
    photo_source = None
    if request.method == 'POST':
        if request.form["btn"] == "¡Enviar!":
            num_sounds = int(request.form.get("letterNum"))
            child_solution = []
            for i in range(num_sounds):
                name_box = f'select{i}_letter'
                sound = int(request.form.get(name_box))
                child_solution.append(sound)
            ans = (child_solution == solutions[word])
            #file = open("salida.txt", "a")
            #file.write(str(ans)+"\n")
            #file.close()
    return render_template('game.html', photo_source=photo_source)

if __name__ == "__main__":
    app.debug = True
    app.run()
