import threading
from client_admin import *

def recive_message():
    bot.infinity_polling()

print ("Inicio Correcto del bot")
hilo = threading.Thread(name = "hilo",target = recive_message)
hilo.start()
print ("El bot se esta ejecutando en otro Hilo")

