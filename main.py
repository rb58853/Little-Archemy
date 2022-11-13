import little_archemy_backend.manage
import telegram_bot_fronted.main
import os

def runserver():
    path = os.getcwd() + "\little_archemy_backend"
    os.chdir(path)
    os.system("py manage.py runserver")

telegram_bot_fronted.main.start()
runserver()
