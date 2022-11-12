from archemy.data.models import Item, ItemMirror, User
import archemy.interfaces.views

def item_in_user(item_name, user_id_in):
    mirrors = ItemMirror.objects.filter(user_id = user_id_in).all()
    items = Item.objects.filter(user_id = user_id_in).all()
    for item in mirrors:
        if item.name == item_name:  return True
    for item in items:
        if item.name == item_name:  return True
    return False    

def item_to_json(item):
    parents = []
    for parent in item.parents.all():
        parents.append(parent.name )#+"["+str(parent.id)+"]")
    return {'id': item.id,'name': item.name,'description': item.description,'parents': parents, 'credits': item.credits }

def items_to_jason(items):
    data = []
    for item in items:
        data.append(item_to_json(item))
    return data    

def mirror_to_json(item):
    parents = []
    for parent in item.parents.all():
        parents.append(parent.name )#+"["+str(parent.id)+"]")
    return {'id': item.id,'name': item.name,'description': item.description,
            'parents': parents, 'aprove':item.aprove,'desaprove':item.desaprove }

def mirrors_to_jason(items):
    data = []
    for item in items:
        data.append(mirror_to_json(item))
    return data     

def split_spaces(chain:str):
    array = []
    temp = ''
    for i in range(len(chain)):
        if chain[i] != ' ':
            temp += chain[i]
        else:
            if temp != '':
                array.append(temp)
            temp = ''
    if temp != '':
        array.append(temp)
    return array

septor = [',','|']
def split_spaces_comas(chain:str):
    array = []
    temp = ''
    comas = True
    for i in range(len(chain)):
        
        if chain[i] == ',' or chain[i] == '|':
            comas = True #encontro un separador
            if temp != '':
                array.append(temp)
            temp = ''
            continue
        
        if comas == True:   #esta comenzando otro termino xq hay un separador activo
            if chain[i] != ' ':
                comas = False #Encuentra una letra
        
        if comas == False:  #Hay que empezar a encadenar los char
            temp += chain[i]
    if temp != '':
        array.append(temp)
            
    return array


def add_parents(item,chain:str, user_in):
    array = split_spaces_comas(chain)
    parents = []
    
    for parent_name in array:
        querie1 = Item.objects.filter(name = parent_name, user = user_in, prime = False)
        querie2 = Item.objects.filter(name = parent_name, prime = True)
        
        if len(querie1) == 1:
            parents.append(querie1[0])
        else:
            if len(querie2) == 1:
                parents.append(querie2[0])
            else:
                exc = "error: El item `"+ parent_name + "` no existe o no esta desbloqueado, no puede usarlo como padre. Compruebe los espacios en blanco y asegurese de que la ortografia sea exacta (por ejemplo las tildes)."
                archemy.interfaces.views.ExeptionViews.error_parent = exc                
                item.delete()
                return False
            
    for parent in parents:
        item.parents.add(parent)
