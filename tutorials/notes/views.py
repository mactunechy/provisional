from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
# from django.db.models import Q

from .models import Notes
from .serializers import NotesSerializer


#Lists all questions and create a question and search questions
class NotesListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = NotesSerializer
    # permission_classes = []

    def get_queryset(self):
        qs =  Notes.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query).distinct()
        return qs
    
    def post(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs)
    
#retrieving, updating , destroying the object
class NotesRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = NotesSerializer
    # permission_classes = []

    def get_queryset(self):
        qs =  Notes.objects.all()
        return qs
        

    

