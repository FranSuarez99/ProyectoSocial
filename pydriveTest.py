from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

tugfa = GoogleAuth()
tugfa.LocalWebserverAuth()

drive = GoogleDrive(tugfa)

a = 1

file1 = drive.CreateFile({'title': 'HelloP.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
file1.SetContentString('Hello World! P de Prueba') # Set content of the file from given string.
file1.Upload()