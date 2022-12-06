from telegram_bot_fronted.queries.get import *
from telegram_bot_fronted.queries.post import *
from telegram_bot_fronted.tools.text_item import *
import telebot #Telegram API

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

token = telegram_bot_fronted.queries.environment.telegram_token
bot = telebot.TeleBot(token)

#client
new_item = "⦿ /new_item  Crea un nuevo item con el formato:\n<b>   Name</b>: <i>item_name</i> \n<b>   Parents:</b> <i>parent1, parent2, parent3, ....</i> \n<b>   Description:</b> <i>item_description</i> \n"
parents = "⦿ /parents Muestra la lista de items con los cuales dispones para crear nuevos elementos.\n"
my_items = "⦿ /my_items Muestra una lista con todos los items que has desbloqueado.\n"
pending_items_text = "⦿ /pending_items Muestra la lista de items que has propuesto.\n"
about_text = "⦿ /about informacion sobre el bot\n"
leader_text = "⦿ /leaderboard Muestra la tabla de posiciones segun los creditos.\n"

#admin
create_basic_text = "⦿ /create_basic crea un nuevo item basico.\n"
list_item = "⦿ /list Muestra la lista de items propuestos por los estudiantes para asi aceptarlos o rechazarlos.\n"
set_admin_text = "⦿ /set_admin Convierte un usuario en administrador. Se le pasa como argumento el @username del usuario.\n"

@bot.message_handler(commands = ["help"])
def help (message):
    id = message.chat.id
    help_text = "<b>LITTLE ARCHEMY\n\nLista de comandos[users]:</b>\n" 
    help_text += about_text
    help_text += parents
    help_text += my_items
    help_text += pending_items_text
    help_text += leader_text
    help_text += new_item
    help_text += "\n<b>Lista de comandos[admins]:</b>\n" 
    help_text += create_basic_text
    help_text += list_item
    help_text += set_admin_text
    bot.send_message(id, help_text, parse_mode="html")

@bot.message_handler(commands = ["about"])
def about(message):
    id = message.chat.id
    info = "<b>Cómo usar el bot?</b>\n\n El objetivo principal es crear nuevos elementos, para ello se cuenta con una lista de elementos básicos con los cuales se comienza la alquimia(/parents). Una vez un elemento de los que creó ha sido aceptado usted podrá utilizar el mismo para crear otros nuevos elementos. Cada item otorga cierta cantidad de créditos para la asignatura de matemática numérica, y acá usted podrá competir con sus compañeros en la tabla de posiciones donde se escala por cantidad de créditos. Si usa el comando /help le quedará claro cada uso de los comandos y le será fácil y maleable el uso de nuestra bot. Les deseamos muchos éxitos en la asignatura, esperamos que este bot los ayude y les sea útil. Cualquier tipo de sugerencia, queja o error por favor comunícase con @rb58853."
    bot.send_message(id, info,parse_mode="html")
