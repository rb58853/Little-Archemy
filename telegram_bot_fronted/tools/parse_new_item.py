from telegram_bot_fronted.tools.split_full_spaces import split_spaces_and_jump

def decoder(chain:str):
    array = split_spaces_and_jump(chain)
    name = ""
    parents = ""
    description = ""
    name_bool = False
    parents_bool = False
    description_bool = False
    words_name = ["name","name:","Name:","Name"]
    words_parents = ["parents","parents:","Parents","Parents:"]
    words_description = ["description", "description:","Description:","Description"]

    for word in array:
        if  in_words(word, words_name):
            name_bool = True
            parents_bool = False
            description_bool = False
            continue
        if  in_words(word, words_parents):
            parents_bool = True
            name_bool = False
            description_bool = False
            continue
        if  in_words(word, words_description):
            description_bool = True
            parents_bool = False
            name_bool = False
            continue

        if name_bool == True:   name+= word+" "
        if parents_bool == True:   parents+= word+" "
        if description_bool == True:   description+= word+" "
    
    return {'name':name,'parents': parents, 'description':description}    

def in_words(word_in, words):
    for word in words:
        if word_in == word: return True
    return False             