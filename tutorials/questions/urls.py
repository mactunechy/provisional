from django.urls import path 
from .views import QuestionsRudView,QuestionsListView

urlpatterns = [
    path('list', QuestionsListView.as_view(),name='questions-list'),
    path('details/<int:pk>', QuestionsRudView.as_view(),name='questions-details'),
    
]
