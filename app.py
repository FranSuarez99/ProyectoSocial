from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import requests, sys, os, shutil
from flask import *

from pyDriveFunct import *

scriptPath = sys.path[0]

master_password = 'incs2022'
fileName1 = 'words.txt'
fileName2 = 'solutions.txt'
fileName3 = 'difficulty.txt'
fileName4 = 'imgSource.txt'
fileName5 = 'imgFolder'
#Configuramos la app de flask
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

#Configuracion con Google Drive
authG = GoogleAuth()
authG.LocalWebserverAuth()
drive = GoogleDrive(authG)

wordsID, solutionsID, difficultyID, imgSourceID, imgFolderID = None, None, None, None, None

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
    if file1['title'] == fileName5:
        imgFolderID = file1['id']

words = dFile(wordsID,fileName1, drive)
difficulty = dict(zip(words, list(map(int, dFile(difficultyID,fileName3, drive)))))
solutions = dict(zip(words, list(map(lambda x : list(map(int, x.split(','))), dFile(solutionsID,fileName2, drive))))) #python tu papa
imgSource = dict(zip(words, dFile(imgSourceID,fileName4, drive)))
updateImages(imgFolderID, imgSource, scriptPath, drive)

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
    LOCAL_IMAGES_PATH = os.path.join(scriptPath, 'static','images','words')
    #Actualizar BD palabras
    words = dFile(wordsID,fileName1, drive)
    difficulty = dict(zip(words, list(map(int, dFile(difficultyID,fileName3, drive)))))
    solutions = dict(zip(words, list(map(lambda x : list(map(int, x.split(','))), dFile(solutionsID,fileName2, drive))))) #python tu papa
    imgSource = dict(zip(words, dFile(imgSourceID,fileName4, drive)))
    updateImages(imgFolderID, imgSource, scriptPath, drive)
    if request.method == 'POST':
        if request.form["btn"] == "¡Agregar!":
            #Agregar palabra
            word = str(request.form['palabra']).upper()
            addData2Files(word, fileName1)
            upload_file_to_drive(wordsID, fileName1, drive)
            #Agregar solucion
            num_sounds = int(request.form.get("letterNum"))
            solution = ''
            for i in range(num_sounds):
                name_box = f'select{i}_letter'
                sound = int(request.form.get(name_box))
                solution += f'{sound},'
            solution = solution[:-1]
            addData2Files(solution, fileName2)
            upload_file_to_drive(solutionsID, fileName2, drive)
            #Agregar dificultad
            difficult = int(request.form.get('dif'))
            addData2Files(difficult, fileName3)
            upload_file_to_drive(difficultyID, fileName3, drive)
            #Agregar nombre imagen
            #img = f'{word}.png'
            img = str(word)+".png"
            addData2Files(img, fileName4)
            upload_file_to_drive(imgSourceID, fileName4, drive)
            #Guardar foto asociada a la nueva palabra
            file = request.files['file']
            file_name = os.path.join(LOCAL_IMAGES_PATH, img)
            file.save(file_name) #guardar local
            uploadPhoto(imgFolderID, file_name, img, drive) #guardar la foto en drive
    return render_template('new_word.html')

#VISTA SELECCION DIFICULTAD
@app.route('/start', methods=['GET', 'POST'])
def difficult_select():
    if request.method == 'POST':
        if request.form["btn"] == "¡Empecemos!":
            difficult = int(request.form.get('dif'))
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
    photo_source = f'{word}.png'
    if request.method == 'POST':
        if request.form["btn"] == "¡Enviar!":
            num_sounds = int(request.form.get("letterNum"))
            child_solution = []
            for i in range(num_sounds):
                name_box = f'select{i}_letter'
                sound = int(request.form.get(name_box))
                child_solution.append(sound)
            ans = (child_solution == solutions[word])
    return render_template('game.html', photo_source=photo_source)

if __name__ == "__main__":
    app.debug = True
    app.run()
