from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='adoption-home'),
    path('about/', views.about, name='adoption-about'),
    path('dogs/', views.dogs, name='adoption-dogs'),
    path('dogs/<int:id>/', views.show, name='adoption-show'),
    path('dogs/new', views.create, name='adoption-create')
]
