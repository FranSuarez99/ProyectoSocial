from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

tugfa = GoogleAuth()
tugfa.LocalWebserverAuth()

drive = GoogleDrive(tugfa)

#file1 = drive.CreateFile({'title': 'HelloP.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#file1.SetContentString('Hello World! P de Prueba') # Set content of the file from given string.
#file1.Upload()

palabrasID = 0

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  if file1['title'] == 'palabras':
      palabrasID = file1['id']
palabras = drive.CreateFile({'id': palabrasID})
palabras.GetContentFile('palabras.txt')

#prueba commit suribe
