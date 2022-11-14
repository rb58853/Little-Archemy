import threading
import telegram_bot_fronted.main
import os

def runserver():
    path = os.getcwd() + "/little_archemy_backend"
    os.chdir(path)
    os.system("python manage.py runserver")

def start ():
    thread = threading.Thread(name = "runserver django",target = runserver)
    thread.start()
    print("Django Server is run")
    telegram_bot_fronted.main.recive_message()

start()
