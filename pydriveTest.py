from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

tugfa = GoogleAuth()
tugfa.LocalWebserverAuth()

drive = GoogleDrive(tugfa)

#file1 = drive.CreateFile({'title': 'HelloP.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
#file1.SetContentString('Hello World! P de Prueba') # Set content of the file from given string.
#file1.Upload()

fileName1 = 'words.txt'
fileName2 = 'solutions.txt'
fileName3 = 'difficulty.txt'
fileName4 = 'imgSource.txt'

wordsID, solutionsID, difficultyID, imgSource = 0, 0, 0, 0

file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file1 in file_list:
  print('title: %s, id: %s' % (file1['title'], file1['id']))
  if file1['title'] == fileName1:
      wordsID = file1['id']
  if file1['title'] == fileName2:
      solutionsID = file1['id']
  if file1['title'] == fileName3:
      difficultyID = file1['id']
  if file1['title'] == fileName4:
      imgSource = file1['id']
words = drive.CreateFile({'id': wordsID})
words.GetContentFile('palabras.txt')
content = words.GetContentString().strip().split()

print(content)

#prueba commit suribe
