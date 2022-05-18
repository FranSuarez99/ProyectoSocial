import platform
import os

oper_sys = platform.system()

if oper_sys == 'Linux':
    os.system('xdg-open http://localhost:5000/')
    os.system('python app.py')
elif oper_sys == 'Windows':
    os.system('start http://localhost:5000/')
    os.system('python app.py')
else:
    pass
