from django.contrib.auth.models import Group
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer, GroupSerializer
from .permissions import HasAccess

# Create your views here.

class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, HasAccess]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [HasAccess]
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    lookup_field = "username"

class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, HasAccess]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer