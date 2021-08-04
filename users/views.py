from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.response import Response

from .serializers import ReadOnlyUserSerializer, WriteOnlyUserSerializer

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return ReadOnlyUserSerializer
        else:
            return WriteOnlyUserSerializer

    def destroy(self, request, pk=None):
        self.user = get_object_or_404(User, id=pk)
        self.user.is_active = 'False'
        self.user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
