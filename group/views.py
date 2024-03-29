from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Group, Payment
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from .serializer import GroupSerializer, UserSerializer, PaymentSerializer
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response
from rest_framework import permissions

UserModel = get_user_model()
@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


class GroupView(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class GroupSearchView(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset = Group.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    permission_classes = [permissions.DjangoModelPermissions]


@permission_classes((AllowAny,))
class UserView(viewsets.ModelViewSet):
    http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentView(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
