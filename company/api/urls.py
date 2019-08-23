from django.urls import path

from .views import CompanyListView, CompanyDetailView


urlpatterns = [
    path('api/', CompanyListView.as_view()),    
    path('api/<int:pk>', CompanyListView.as_view()),  
    path('<pk>', CompanyDetailView.as_view())
]