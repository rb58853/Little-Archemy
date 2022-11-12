from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Item)
admin.site.register(ItemMirror)
admin.site.register(User)