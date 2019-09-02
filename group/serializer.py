from rest_framework import serializers
from .models import Group
from  django.contrib.auth.models import User

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'admin', 'capacity', 'weekly_amount', 'searchable', 'members')
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')