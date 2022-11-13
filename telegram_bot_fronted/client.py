from asyncio.windows_events import NULL
from telegram_bot_fronted.admin import *
from telegram_bot_fronted.tools.parse_new_item import decoder


@bot.message_handler(commands = ["new_item"])
def new_item (message):
    """Inicia un nuevo item"""
    id = message.chat.id
    mensaje = message.text
    data = decoder(mensaje)
    post_new_item(data['name'],data['parents'],data['description'],id)
    send = get_error_new()
    bot.send_message(id, send, parse_mode="html")

@bot.message_handler(commands = ["start"])
def new_user (message):
    """Inicia un nuevo usuario"""
    id = message.chat.id
    name = message.chat.first_name
    username = message.chat.username
    post_new_user(id,name,username)
    bot.send_message(id, "Bienvenido, usted ha sido registrado en la base de datos correctamente. Para usar el bot vea /help")

@bot.message_handler(commands = ["parents"])
def parents_list (message):
    id = message.chat.id
    items = get_item_for_parents(id)
    send = "<b>AVIABLE ITEMS</b>\n"
    for item in items:
        send+= "⦿ <code>"+item + "</code>\n"
    bot.send_message(id, send,parse_mode="html")

@bot.message_handler(commands = ["pending_items"])
def pending_items (message):
    id = message.chat.id
    items = get_mirror_from_id(id)
    if len(items) == 0:
        bot.send_message(id, "<i>No tiene items pendientes a revisar</i>.",parse_mode="html")
        return
    for item in items:
        SeeItems.item_buttons(id,item)

@bot.message_handler(commands = ["my_items"])
def items_list (message):
    id = message.chat.id
    items = get_items_from_id(id)
    if len(items) == 0:
        bot.send_message(id, "<i>No tiene ningún item aprobado</i>",parse_mode="html")
        return

    pos = pos_in_leader(id)
    credits = int(get_credits_from_user(id))
    text = "<b>ITEMS</b>\n<i>credits:</i><code> " + str(credits)+"</code>   🏅["+str(pos)+"]\n\n"
    text += items_to_string(items)
    bot.send_message(id, text,parse_mode="html")

def pos_in_leader(id):
    pos = 1
    users = get_all_users()
    credits = int(get_credits_from_user(id))
    for user in users:
        if int(int(get_credits_from_user(user['id']))) > credits:
            pos+=1
    return pos

class SeeItems():
    def aprove(item_id):
        url = base_url+"items/aprove/"
        my_data = {'id': item_id}
        r = requests.post(url, json = my_data)
    
    def desaprove(item_id):
        url = base_url+"items/desaprove/"
        my_data = {'id': item_id}
        r = requests.post(url, json = my_data) 

    def item_buttons(message_id, item):
        item_id = item['id']
        markup = InlineKeyboardMarkup()
        if item['aprove'] != "":
            head = "<b>✅ACEPTADO</b>\n\n"
            button = InlineKeyboardButton("ACCEPT" ,callback_data="client ok "+ str(item_id))
            markup.row(button)
            info = "<i>Este item ha sido aprobado, usted obtiene</i> <code>" + item['aprove'] + "</code> <i>créditos.</i>"
            bot.send_message(message_id,head + mirror_to_admin(item) + info, reply_markup=markup,parse_mode= "html")       
            return
        
        if item['desaprove'] != "":
            head = "<b>❌DENEGADO</b>\n\n"
            button = InlineKeyboardButton("ACCEPT" ,callback_data="client no " +" "+ str(item_id))
            markup.row(button)
            info = "<i>Este item ha sido rechazado por el siguiente motivo:</i> <b>" + item['desaprove']+"</b>"
            bot.send_message(message_id,head+ mirror_to_admin(item) + info, reply_markup=markup,parse_mode= "html")       
            return

        button = InlineKeyboardButton("CLOSE" ,callback_data="close")
        markup.row(button)
        info = "\nEste item aún no ha sido evaluado."
        bot.send_message(message_id, mirror_to_admin(item) + info, reply_markup=markup,parse_mode= "html")       
    
    def valid_item(item_id):
        items = get_all_mirror()
        for item in items:
            if item["id"] == int(item_id):
                if item["aprove"] != "" or item["desaprove"] != "": return True
                else: return False      
        return False
    
    def button_from_id(message_id,item_id):
        SeeItems.item_buttons(message_id,SeeItems.get_item(item_id))
    
    def get_item(item_id):
        items = get_all_mirror()
        for item in items:
            if item['id'] == int(item_id):
                return item
        return NULL        
