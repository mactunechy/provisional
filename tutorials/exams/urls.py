
from django.urls import path
from .views import ExamListView,ExamRudView

urlpatterns = [

    path('api/exams-list/',ExamListView.as_view(), name="exams-list"),
    path('api/exams-details/',ExamRudView.as_view(), name="exams-details"),
]