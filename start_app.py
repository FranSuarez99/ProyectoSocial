import platform
import os

oper_sys = platform.system()

if oper_sys == 'Linux':
    os.system('export FLASK_APP=app.py')
    os.system('export FLASK_ENV=development')
    os.system('flask run')
elif oper_sys == 'Windows':
    os.system('start http://localhost:5000/')
    #os.system('set FLASK_APP=app.py')
    #os.system('set FLASK_ENV=development')
    #os.system('flask run')
    os.system('python app.py')
else:
    pass
