from random import shuffle
import os, shutil

def dFile(id,fileN, drive):
	"""
	input:un id que hace referencia al id del archivo en drive y un fileN que es el nombre del
	archivo en drive
	output: el contenido separado por linea del archivo guardado en drive
	"""
	download_file = drive.CreateFile({'id': id})
	download_file.GetContentFile(fileN)
	content = download_file.GetContentString().strip().split()
	return content

def getWords(d, difficulty):
	"""
	Input: Recibe una dificultad d (int) y el diccionario de todas las dificultades (llaves las palabras
	y valor la dificultad)
	Output: Una lista randomizada de las palabras de la dificultad especifica d
	"""
	wordsD = [word for word, diff in difficulty.items() if diff == d]
	shuffle(wordsD)
	return wordsD

def addData2Files(data, file):
	"""
	Input: data es el nombre de la informacion que se va a guardar en el archivo dado (file)
	Output: N.A. (se actualizan los archivos txt locales)
	"""
	file = open(file, "a")
	file.write(str(data)+"\n")
	file.close()
	return

def upload_file_to_drive(file_id, local_path, drive):
    """Overwrites the existing Google drive file."""
    update_file = drive.CreateFile({'id': file_id})
    update_file.SetContentFile(local_path)
    update_file.Upload()

def uploadPhoto(file_id, local_path, img, drive):
	file2 = drive.CreateFile({'parents': [{'id': file_id}]})
	file2.SetContentFile(local_path)
	file2['title'] = img # cambia nombre de png para eliminar el path
	file2.Upload()

def updateImages(imgFolderID, words, scriptPath, drive):
	file_list = drive.ListFile({'q': "'{}' in parents and trashed=false".format(imgFolderID)}).GetList()
	for i, file1 in enumerate(sorted(file_list, key = lambda x: x['title']), start=1):
		file1.GetContentFile(file1['title'])
	for w in words:
		filename = f'{w}.png'
		src = os.path.join(scriptPath, filename)
		dest = os.path.join(scriptPath, 'static', 'images', 'words')
		if os.path.isfile(os.path.join(dest, filename)) != True: #si el archivo no existe lo muevo
			shutil.move(src, dest)
		else: #si ya existe lo borro
			os.remove(src)

def updateLocalVariables(fileName1, fileName2, fileName3, wordsID, difficultyID, solutionsID, drive):
	words = dFile(wordsID,fileName1, drive)
	difficulty = dict(zip(words, list(map(int, dFile(difficultyID,fileName3, drive)))))
	solutions = dict(zip(words, list(map(lambda x : list(map(int, x.split(','))), dFile(solutionsID,fileName2, drive))))) #python tu papa
	return words, difficulty, solutions

def parser(p):
	return p.replace('??', '0')
