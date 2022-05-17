import platform
import os

oper_sys = platform.system()

if oper_sys == 'Linux':
    os.system('export FLASK_APP=app.py')
    os.system('export FLASK_ENV=development')
    os.system('flask run')
elif oper_sys == 'Windows':
    os.system('set FLASK_APP=app.py')
    os.system('set FLASK_ENV=development')
    os.system('flask run')
else:
    pass
