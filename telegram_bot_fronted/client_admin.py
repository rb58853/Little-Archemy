from telegram_bot_fronted.client import *
from telegram_bot_fronted.tools.leaderboard_tools import *

@bot.callback_query_handler(func = lambda x: True)
def items_aprovation_call(call):
    """Llamada a las acciones de los botones de todo el bot, tanto los de admin como los 
    del cliente."""
    cid = call.from_user.id
    mid = call.message.id
    if call.data == "close":
        bot.delete_message(cid,mid)
        return
    data = call.data.split()
    
    if data[0] == "client":
        """ Trabajo con los metodos del fichero client.py"""
        data = call.data.split()
        item_id = int(data[2])
        if SeeItems.valid_item(item_id) == True:
            if data[1] == "ok":
                SeeItems.aprove(item_id)
                bot.answer_callback_query(call.id,"Operación exitosa.")
            if data[1] == "no":
                SeeItems.desaprove(item_id)
                bot.answer_callback_query(call.id,"Operación exitosa.")
            bot.delete_message(cid,mid)
        else:
            bot.answer_callback_query(call.id,"Este item ya esta registrado.")
            bot.delete_message(cid,mid)

    if data[2] == "enter":
        bot.answer_callback_query(call.id,"Esta opcion aún no está implementada.")
        return
        
    if data[0] == "admin":
        """ Trabajo con los metodos del fichero admin.py"""
        item_id = data[len(data)-1]
        if ItemsAprovation.valid_item(item_id) == True:
            user_id = get_user_from_item(item_id) #message_id coincide
            if data[1] == "ok":
                if data[2] != "enter":
                    ItemsAprovation(int(item_id)).aprove_item(data[2])
                    bot.answer_callback_query(call.id,"Operación exitosa.")
            if data[1] == "no":
                reply= ItemsAprovation.join_with_spaces(data) 
                if data[2] != "enter":
                    ItemsAprovation(int(item_id)).desaprove_item(reply)
                    bot.answer_callback_query(call.id,"Operación exitosa.")
            if data[2] != "enter":
                bot.delete_message(cid,mid)
            SeeItems.button_from_id(user_id,item_id)        
        else:
            bot.answer_callback_query(call.id,"Este item ya esta registrado.")
            bot.delete_message(cid,mid)

@bot.message_handler(commands = ["leaderboard"])
def view_leaderboard (message):
    id = message.chat.id
    users = get_all_users()
    
    leaderboard = []
    for user in users:
        user_id = user['id']
        user_credits = get_credits_from_user(user_id)
        leaderboard.append(str(user_credits)+" "+user['username']+" "+str(user['id']))
    
    text =create_text_leaderboard(leaderboard,id)
    bot.send_message(id, text, parse_mode="html")


