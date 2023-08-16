from rest_framework import generics

from apps.cabinet_api.serializers import UserRegisterSerializer


class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
