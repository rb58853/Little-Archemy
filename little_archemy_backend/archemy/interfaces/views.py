from unicodedata import name
from rest_framework.generics import CreateAPIView,RetrieveAPIView
from rest_framework.response import Response
from django.http import JsonResponse
from archemy.data.models import *
from archemy.domain.queries import *
from archemy.interfaces.serializers import *

class ExeptionViews:
    error_parent = "No se creo el item."
    def exception_parents(request):
        data = ExeptionViews.error_parent
        ExeptionViews.error_parent = "   <i>Por favor llene todos los campos para crear el item. El mensaje debe tener el siguiente formato:</i>\n\n/new_item\n <b>Name:</b><i> nombre</i> \n <b>Parents:</b> <i> p1, p2, p3, ...</i> \n <b>Description:</b><i> descripción</i>\n\n <i>   Puede usar la siguiente plantilla:</i>\n\n<code>/new_item\nName: \nParents: \nDescription: -</code>"
        return JsonResponse(data,safe = False)

class UserViews:
    def users(request):
        data  = list(User.objects.values())
        return JsonResponse(data,safe = False)
    
    class CreditsFromUser(RetrieveAPIView):
        def retrieve(self, request, *args, **kwargs):
            id = int(request.query_params.get('user_id',0))
            value = UserQueries.credits_from_id(id)
            data = {'credits': value}
            return JsonResponse(data,safe = False)
    
    class DataFromUser(RetrieveAPIView):
        def retrieve(self, request, *args, **kwargs):
            id_user = int(request.query_params.get('id',0))
            data = list(User.objects.filter(id = id_user).values())
            return JsonResponse(data[0],safe = False)

    class SetAdmin(RetrieveAPIView):
        def retrieve(self, request, *args, **kwargs):
            nick = request.query_params.get('username',0)[1:]
            print(nick)
            reply = "El usuario " + nick +" no esta registrado. Use el comando /start para registrarse"
            try:
                user = User.objects.get(username = nick)
            except:
                return JsonResponse(reply,safe = False)
            user.admin = True
            user.save()
            reply = "El usuario @" + nick +" ahora es administrador."
            return JsonResponse(reply,safe = False)

    class NewUser(CreateAPIView):
        serializer_class  = NewUserSerializer
        def perform_create(self, serializer):
            data = serializer.data
            reply=UserQueries.new_user(data['id'],data['name'],data['username'])
            return JsonResponse(reply,safe = False)


class ItemViews:
    def items(request):
        data = items_to_jason(Item.objects.all())
        return JsonResponse(data,safe = False)
    
    def mirrors(request):    
        data = mirrors_to_jason(ItemMirror.objects.all())
        return JsonResponse(data,safe = False)
    
    def prime_items(request):
        data = []
        for item in Item.objects.filter(prime = True).all():
            data.append(item.name)
        return JsonResponse(data,safe = False)

    class UserFromItem(RetrieveAPIView):
        def retrieve(self, request, *args, **kwargs):
            id_in = int(request.query_params.get('id',0))
            item = ItemMirror.objects.get(id = id_in)
            return JsonResponse(item.user_id,safe = False)
            
    class ItemfromUser(RetrieveAPIView):
        def retrieve(self, request, *args, **kwargs):
            id = int(request.query_params.get('user_id',0))
            data = ItemQueries.items_from_id(id)
            return JsonResponse(data,safe = False)

    class MirrorfromUser(RetrieveAPIView):
        def retrieve(self, request, *args, **kwargs):
            id = int(request.query_params.get('user_id',0))
            data = mirrors_to_jason(ItemQueries.mirror_from_id(id))
            return JsonResponse(data,safe = False)
    
    class NewItem(CreateAPIView):
        ExeptionViews.error_parent = "   <i>Por favor llene todos los campos para crear el item. El mensaje debe tener el siguiente formato:</i>\n\n/new_item\n <b>Name:</b><i> nombre</i> \n <b>Parents:</b> <i> p1, p2, p3, ...</i> \n <b>Description:</b><i> descripción</i>\n\n <i>   Puede usar la siguiente plantilla:</i>\n\n<code>/new_item\nName: \nParents: \nDescription: -</code>"
        serializer_class  = NewItemSerializer

        def perform_create(self, serializer):
            try:    
                data = serializer.data
                ItemQueries.new_item(data['name'],data['parents'],data['description'],data['user_id'])
            except:pass
           
    class AproveMirror(CreateAPIView):
        serializer_class  = AproveMirrorSerializer
        
        def perform_create(self, serializer):
            data = serializer.data
            ItemQueries.aprove_mirror(data['id'],data['credits']) 
    
    class DesaproveMirror(CreateAPIView):
        serializer_class  = DesaproveMirrorSerializer

        def perform_create(self, serializer):
            data = serializer.data
            print("llego " +str(data))
            ItemQueries.desaprove_mirror(data['id'],data['reason'])               
    
    
    class AproveItem(CreateAPIView):
        serializer_class  = AproveItemSerializer

        def perform_create(self, serializer):
            data = serializer.data
            ItemQueries.aprove_item(data['id']) 
            
    class DesaproveItem(CreateAPIView):
        serializer_class  = DesaproveItemSerializer

        def perform_create(self, serializer):
            data = serializer.data
            ItemQueries.desaprove_item(data['id']) 
            