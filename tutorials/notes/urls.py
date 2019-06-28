
from django.urls import path
from .views import NotesListView, NotesRudView



urlpatterns = [
    path('list/', NotesListView.as_view(), name="notes-list"),
    path('details/<int:pk>', NotesListView.as_view(), name="notes-details"),
]
