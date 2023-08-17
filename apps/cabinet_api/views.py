from rest_framework import generics, status
from rest_framework.response import Response

from apps.cabinet_api.serializers import UserRegisterSerializer


class UserRegister(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        user_serializer = UserRegisterSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response("Registration is successful", status=status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
