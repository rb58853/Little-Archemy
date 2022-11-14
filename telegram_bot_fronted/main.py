import threading
from telegram_bot_fronted.client_admin import bot
def recive_message():
    bot.infinity_polling()

def start():
    print ("Bot Server is run")
    thread = threading.Thread(name = "hilo",target = recive_message)
    thread.start()
    # print ("El bot se esta ejecutando en otro Hilo")

#start()
