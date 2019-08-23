from django.urls import path
from . import views

urlpatterns = [
    path('api/upload/', views.UploadView.as_view(), name= 'uploads_list'),
]