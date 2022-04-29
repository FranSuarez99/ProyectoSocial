#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive

#authG = GoogleAuth()
#authG.LocalWebserverAuth()

#drive = GoogleDrive(authG)

#file1 = drive.CreateFile({'title': 'HelloP.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#file1.SetContentString('Hello World! P de Prueba') # Set content of the file from given string.
#file1.Upload()

def dFile(id,fileN):
	"""
	input:un id que hace referencia al id del archivo en drive y un fileN que es el nombre deo archivo en drive
	output: el contenido separado por linea del archivo guardado en drive
	"""
	download_file = drive.CreateFile({'id': id})
	download_file.GetContentFile(fileN)
	content = download_file.GetContentString().strip().split() 
	return content

def getSolution(c):
	"""
	input: una palabra
	output: la solucion
	"""
	
	return 

def posWord(words,p):return  words.index(p)


def sPalabra(w,s,d,i,words):
	global wordsID,solutionsID,difficultyID,imgSource

	"""
	Input: Recibe una string w de la palobra en cuestion
	una lista l de n posiciones donde n es el numero de sonidos en la palabra,
	cada poscion en L hace referencia a un tipo de sonido (consonante, vocal, vocal tonica, rr o ñ),
	una dificultad d de la palabra y el nombre de la imagen i de la palabra.
	output: guarda el archivo actualizado
	"""
	if w not in words:
    ans = None





def evaluate(w,s,words):
	"""
	n = posword(words,w)
	sol = getSolution(words[n])
	"""
  ans = None





"""
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


word[0]
solutions[0]
d[0]
"""