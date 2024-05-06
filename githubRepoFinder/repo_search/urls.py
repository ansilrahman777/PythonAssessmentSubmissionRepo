from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('repository/<int:repository_id>/', views.repository_details, name='repository_details'),

]