from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer

User = get_user_model()


@api_view(['GET', 'POST'])
def get_users(request):
    if request.method == 'POST':
        serializer = WriteOnlyUserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=request.data['username'],
                first_name=request.data['first_name'],
                last_name=request.data['last_name'],
                password=request.data['password'],
                is_active=request.data['is_active']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    qs = User.objects.all()
    serializer = ReadOnlyUserSerializer(qs, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def get_users_details(request, pid):
    if request.method == 'GET':
        user = get_object_or_404(User, id=pid)
        serializer = ReadOnlyUserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

    if request.method == 'PUT':
        user = get_object_or_404(User, id=pid)
        serializer = WriteOnlyUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            user.set_password(request.data['password'])
            user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        user = get_object_or_404(User, id=pid)
        serializer = WriteOnlyUserSerializer(
                        user,
                        data=request.data,
                        partial=True
                        )
        if serializer.is_valid():
            serializer.save()
            if 'password' in request.data:
                user.set_password(request.data['password'])
                user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user = get_object_or_404(User, id=pid)
        user.is_active = 'False'
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
