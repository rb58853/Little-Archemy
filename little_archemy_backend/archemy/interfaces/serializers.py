from rest_framework import serializers 

class NewItemSerializer(serializers.Serializer):
    parents = serializers.CharField()
    name = serializers.CharField()
    description = serializers.CharField()
    user_id = serializers.IntegerField()

class NewUserSerializer(serializers.Serializer):
    name = serializers.CharField()
    username = serializers.CharField()
    id = serializers.IntegerField()
    
class AproveItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class AproveMirrorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    credits = serializers.IntegerField()

class DesaproveItemSerializer(serializers.Serializer):
    id = serializers.IntegerField()

class DesaproveMirrorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    reason = serializers.CharField()
      
    