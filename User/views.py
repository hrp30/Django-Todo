from dataclasses import field

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework import status

from User.models import CustomUser


# Create your views here.
class UserRegistration(APIView):
    class InputSerialization(serializers.Serializer):
        password = serializers.CharField(max_length=255)
        email = serializers.EmailField()

        def validate_email(self, email):
            if CustomUser.objects.filter(email=email).exists():
                raise serializers.ValidationError("Email Already Exists")
            return email

    class OutputSerialization(serializers.ModelSerializer):
        class Meta:
            model = CustomUser
            fields = ['email']

    def post(self, request):
        serializer = self.InputSerialization(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user = CustomUser.objects.create_user(email=serializer.validated_data['email'],
                                                  password=serializer.validated_data['password'])
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'message': self.OutputSerialization(user).data}, status=status.HTTP_201_CREATED)
