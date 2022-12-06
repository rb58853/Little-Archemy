from importlib.abc import PathEntryFinder
from telegram_bot_fronted.bot import *


@bot.message_handler(commands = ["create_basic"])
def create_basic (message):
    id = message.chat.id
    data_text = message.text.split()
    
    admin = get_data_from_user(message.chat.id)['admin']
    if admin == False:
        bot.send_message(id, "Este comando solo lo pueden utilizar los administradores")
        return
    
    if len(data_text) >= 2:
        name = ""
        for i in range(1,len(data_text)-1):
            name += data_text[i]+" "
        name += data_text[len(data_text)-1]
        bot.send_message(id,name,parse_mode="html")
        reply = post_create_basic(name)
        
        bot.send_message(id,reply,parse_mode="html")
    else:
        error = "<i>Debe indicar un nombre para el nuevo Item, ejemplo: </i><code>/create_basic item_name</code> "
        bot.send_message(id,error,parse_mode="html")
        return
        

@bot.message_handler(commands = ["list"])
def mirror_list (message):
    id = message.chat.id
    admin = get_data_from_user(message.chat.id)['admin']
    if admin == True:
        items = ItemsAprovation.get_mirror_for_admin()
        if items == "-" :
            bot.send_message(id, "No hay Items disponibles para aprobar.")
            return
        for item in items:
            ItemsAprovation(item['id']).item_buttons(id,item)
    else: bot.send_message(id, "Este comando solo lo pueden utilizar los administradores")

@bot.message_handler(commands = ["set_admin"])
def set_admin (message):
    id = message.chat.id
    data_text = message.text.split()
        
    admin = get_data_from_user(message.chat.id)['admin']
    if admin == True:
        if len(data_text) != 2:
            bot.send_message(id, "El argumento para el comando no es correcto")
            return
        new_admin = data_text[1]
        result = post_set_admin(new_admin)
        bot.send_message(id, result)
    else: bot.send_message(id, "Este comando solo lo pueden utilizar los administradores")
class ItemsAprovation:
    #static vars
    in_queue = {}
    r1 = "bad parents"
    r2 = "bad description"
    reason1 = "Los items padres no son los correctos."
    reason2 = "La descripcion es incompleta."

    def __init__(self,id):
        self.reason = ""
        self.credits = ""
        self.id = id

    def add_to_dic(self):    
        ItemsAprovation.in_queue[str(id)]= self 
    
    def aprove_item(self,credits):
        url = base_url+"items/mirror/aprove/"
        my_data = {
                'id': self.id,
                'credits': int(credits),
            }
        r = requests.post(url, json = my_data)
    
    def desaprove_item(self,reason):
        url = base_url+"items/mirror/desaprove/"
        my_data = {
                'id': int(self.id),
                'reason': reason,
            }
        r = requests.post(url, json = my_data)


    def item_buttons(self,message_id, item):
        item_id = item['id']
        markup = InlineKeyboardMarkup()
        credits1 = InlineKeyboardButton("Accept: 5000 credits" ,callback_data="admin ok 5000 "  + str(item_id))
        credits2 = InlineKeyboardButton("Accept: 10000 credits",callback_data="admin ok 10000 " + str(item_id))
        credits3 = InlineKeyboardButton("Accept: 20000 credits",callback_data="admin ok 20000 " + str(item_id))
        credits4 = InlineKeyboardButton("Accept: 50000 credits",callback_data="admin ok 50000 " + str(item_id))
        credits5 = InlineKeyboardButton("Accept: [enter] credits",callback_data="admin ok enter " + str(item_id))

        decline1 = InlineKeyboardButton("Decline: "+ItemsAprovation.r1,callback_data="admin no " + ItemsAprovation.reason1+" " + str(item_id))
        decline2 = InlineKeyboardButton("Decline: "+ItemsAprovation.r2,callback_data="admin no " + ItemsAprovation.reason2+" " + str(item_id))
        decline3 = InlineKeyboardButton("Decline: [enter]",callback_data="admin no enter " + str(item_id))
        
        close = InlineKeyboardButton("CLOSE",callback_data="close")
        

        markup.row(credits1,credits2).row(credits3,credits4).row(credits5).row(decline1,decline2).row(decline3).row(close)
        bot.send_message(message_id,mirror_to_admin(item),reply_markup=markup, parse_mode="html")
    
    def join_with_spaces(data):
        """Para unir la razon por la cual no se acepta el item, se indexa desde la posicion 2(inclusivo) hasta la n-1(exclusivo)"""
        result = ""
        for i in range(2,len(data)-1):
            result += data[i]+" "
        return result
    def get_mirror_for_admin():
        url = base_url +"items/mirror"
        response = urlopen(url)
        data_json = json.loads(response.read())
        items = []
        for item in data_json:
            if item['aprove'] != "" or item['desaprove'] != "":
                items.append(item)
        for item in items:
            data_json.remove(item)
        if len(data_json) == 0: return "-"        
        return data_json

    def valid_item(item_id):
        items = get_all_mirror()
        for item in items:
            if item["id"] == int(item_id):
                if item["aprove"] != "" or item["desaprove"] != "": return False
                else: return True     
