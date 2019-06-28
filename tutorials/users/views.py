from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
# from django.db.models import Q
from tutorials.permissions import IsStaffOrReadOnly
from .models import CustomUser
from .serializers import CustomUserSerializer


#Lists all questions and create a question and search questions
class CustomUserListView(generics.CreateAPIView):
    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    # permission_classes = []

    
    def post(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    
#retrieving, updating , destroying the object
class CustomUserRudView(generics.RetrieveUpdateDestroyAPIView):

    lookup_field = 'pk'
    serializer_class = CustomUserSerializer
    # permission_classes = [IsStaffOrReadOnly]

    def get_queryset(self):
        qs =  CustomUser.objects.all()
        return qs
        

    

