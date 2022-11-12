from django.db import models

class User(models.Model):
    name = models.CharField(max_length=40)
    username = models.CharField(max_length=40)
    admin = models.BooleanField()


class Item(models.Model):
    name =models.CharField(max_length=60)
    parents = models.ManyToManyField('self',symmetrical=False)
    description = models.CharField(max_length=6000)
    credits = models.IntegerField(null = True)
    user = models.ForeignKey(User, null = True,related_name = "items", on_delete = models.CASCADE)
    prime = models.BooleanField()


class ItemMirror(models.Model):
    name =models.CharField(max_length=60)
    parents = models.ManyToManyField(Item,related_name= "childs")
    description = models.CharField(max_length=6000)
    user = models.ForeignKey(User, null = True,related_name = "items_mirror", on_delete = models.CASCADE)
    aprove = models.CharField(max_length=60)
    desaprove = models.CharField(max_length=6000)