def items_to_string(items):
    text = ""
    for item in items:
        text += item_to_string(item)
    return text     

def mirror_to_string(items):
    text = "ITEMS \n"
    for item in items:
        text += "name: " + str(item['name'])
        text += "  [id: " + str(item['id']) +"]"+"\n"
        text += "description: " + str(item['description'])+"\n"
        text += "parents: " + str(item['parents'])+"\n"
        # for parent in item['parents']:
        #     text+="   -"+parent+"\n"
        text+="\n" 
    return text

def item_to_string(item):
    text = "<b>NAME:</b> <code>" + str(item['name'])+"</code>\n"
    text += "<b>CREDITS:</b> <code>" + str(item['credits'])+"</code>\n"
    text += "<b>PARENTS:</b>\n"
    for parent in item['parents']:
        text+="  ⦿ <code>"+parent+"</code>\n"
    text+="\n" 
    return text

def mirror_to_admin(item):
    text = "<b>NAME:</b> <code>" + str(item['name'])+"</code>\n"
    text += "<b>DESCRIPTION:</b> <i>" + str(item['description'])+"</i>\n"
    text += "<b>PARENTS:</b>\n"
    for parent in item['parents']:
        text+="  ⦿ <code>"+parent+"</code>\n"
    text+="\n" 
    return text