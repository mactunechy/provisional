
from django.contrib import admin
from django.urls import path,include
from rest_framework_jwt.views import obtain_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/notes/',include('notes.urls')),
    path('api/questions/',include('questions.urls')),
    path('api/exams/',include('exams.urls')),
    path('api/auth/login',obtain_jwt_token, name='api-login'),
    path('api/auth/registration/', include('rest_auth.registration.urls')),
]
