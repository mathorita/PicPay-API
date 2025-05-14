from django.shortcuts import render
from rest_framework import viewsets
from .models import User,Transaction
from .serializers import UserSerializer, TransactionSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSender, IsUser


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsUser]
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    

class TransactionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,IsSender]

    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def get_queryset(self):
        return Transaction.objects.filter(sender=self.request.user)
