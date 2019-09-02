from rest_framework import serializers
from .models import *
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'description', 'admin', 'capacity', 'weekly_amount', 'searchable', 'members')
        
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user
    class Meta:
        model = UserModel
        fields = ('id', 'username', 'email', 'password')
        
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('id', 'user',  'amount', 'group')