from django.shortcuts import render
from rest_framework import generics
from rest_framework import mixins
# from django.db.models import Q

from .models import Question
from .serializers import QuestionSerializer
from tutorials.permissions import IsStaffOrReadOnly


#Lists all questions and create a question and search questions
class QuestionsListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = QuestionSerializer
    permission_classes = [IsStaffOrReadOnly]
    # permission_classes = []

    def get_queryset(self):
        qs =  Question.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(title__icontains=query).distinct()
        return qs
    
    def post(self,request, *args, **kwargs):
        return self.create(request,*args,**kwargs)

    def get_serializer_context(self,*args,**kwargs):
        return { "request" :self.request }
        
    
#retrieving, updating , destroying the object
class QuestionsRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = QuestionSerializer
    permission_classes = [IsStaffOrReadOnly]

    # permission_classes = []

    def get_queryset(self):
        qs =  Question.objects.all()
        return qs
    
    def get_serializer_context(self,*args,**kwargs):
        return { "request" :self.request }
        

    

