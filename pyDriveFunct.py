
def dFile(id,fileN, drive):
	"""
	input:un id que hace referencia al id del archivo en drive y un fileN que es el nombre deo archivo en drive
	output: el contenido separado por linea del archivo guardado en drive
	"""
	download_file = drive.CreateFile({'id': id})
	download_file.GetContentFile(fileN)
	content = download_file.GetContentString().strip().split()
	return content

def sPalabra(w,s,d,i,words):
	"""
	Input: Recibe una string w de la palobra en cuestion
	una lista l de n posiciones donde n es el numero de sonidos en la palabra,
	cada poscion en L hace referencia a un tipo de sonido (consonante, vocal, vocal tonica, rr o ñ),
	una dificultad d de la palabra y el nombre de la imagen i de la palabra.
	output: guarda el archivo actualizado
	"""
	if w not in words:
		ans = None
