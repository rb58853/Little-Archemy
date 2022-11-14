import threading
import little_archemy_backend.manage
import telegram_bot_fronted.main
import os


def runserver():
    path = os.getcwd() + "\little_archemy_backend"
    os.chdir(path)
    os.system("py manage.py runserver")

def start ():
    thread = threading.Thread(name = "runserver django",target = runserver)
    thread.start()
    print("Django Server is run")
    telegram_bot_fronted.main.start()

start()