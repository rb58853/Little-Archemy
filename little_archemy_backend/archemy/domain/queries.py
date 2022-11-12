from archemy.domain.tools import *

class ItemQueries():
    def new_item(item_name:str, parents:str, description_in:str, user_id:int):
        archemy.interfaces.views.ExeptionViews.error_parent = "No se creo el item."
        try:
            if item_in_user(item_name,user_id) == True:
                reply = "   <i>El item</i> <code>"+ item_name + "</code><i> ya exite. No puede tener dos items con el mismo nombre.</i>"
                archemy.interfaces.views.ExeptionViews.error_parent = reply
                return
        except:pass        

        try: user_in = User.objects.get(id = user_id) 
        except: archemy.interfaces.views.ExeptionViews.error_parent = "<i>Usted no esta registrado, por favor user el comando /start para registrarse.</i>"
        
        item = ItemMirror.objects.create(name = item_name,user = user_in, 
                        description = description_in, aprove = "", desaprove= "")
        if add_parents(item,parents, user_in) == False: return 
        result = '<i>   El item</i> <code>'+ item.name +'[id: '+ str(item.id)+']</code>'+ ' <i>ha sido creado satisfactoriamente. Ha sido enviado a revisar.</i>'
        archemy.interfaces.views.ExeptionViews.error_parent = result
        return 

    def aprove_mirror(item_id, credits_in):
        item = ItemMirror.objects.get(id = item_id)
        item.aprove = str(credits_in)
        item.save()
        return True        

    def desaprove_mirror(item_id, reason:str):
        item = ItemMirror.objects.get(id = item_id)
        item.desaprove = reason
        item.save()
        return True        
            
    def aprove_item(item_id):
        item = ItemMirror.objects.get(id = item_id)
        credits_in = int(item.aprove)
        temp = Item.objects.create(name = item.name, credits = credits_in,
                            description = item.description, user = item.user, prime = False)
        temp.parents.set(item.parents.all())
        # for parent in item.parents.all():
        #     temp.parents.add(parent)                    
        ItemMirror.objects.get(id = item_id).delete()

    def desaprove_item(item_id):
        ItemMirror.objects.get(id = item_id).delete()
    
    def get_prime_items():
        return Item.objects.filter(prime = True)
    
    def mirror_from_id(id):    
        return ItemMirror.objects.filter(user_id = id)    
    
    def last_mirror_from_id(id):    
        return ItemMirror.objects.filter(user_id = id).last()    
    
    def items_from_id(id):
        items = Item.objects.filter(user_id = id).all()
        return items_to_jason(items)    

class UserQueries:
    def new_user(id_in, name_in,username_in):
        try:
            user = User.objects.get_or_create(id = id_in, name = name_in, username = username_in, admin = False)
            return "Usted ha sido registrado satisfactoriamente. Se ha registrado por el username: @" +  user.username +". Bienvenido, consulte el comando /help para iformación."
        except:
            reply = "Ha ocurrido un error en su registro, por favor reportelo a los administradores:\n."
            for u in User.objects.filter(admin = True).all():
                reply += "@"+u.username+"\n"
            return reply


    def credits_from_id(id_in):
        result = 0
        items = Item.objects.filter(user_id = id_in).all()
        for item in items:
            result += item.credits
        return result        

class Populate:
    def populate(self):
        self.create_item("numero real", "-")  
        self.create_item("operacion matematica", "-")
        self.create_item("exponente", "-")  
        self.create_item("base", "-")  
        self.create_item("mantisa", "-")  
        self.create_item("aritmética de punto flotante", "-")  
        User.objects.get_or_create(id = 776087157, name = "Raúl", username = "rb58853", admin = True)

    def create_item(self, name_in, description_in):
        Item.objects.get_or_create(prime = True,
                            name = name_in, 
                            description = description_in)
    
