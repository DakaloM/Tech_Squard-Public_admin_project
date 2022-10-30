from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home/', views.homepage, name='homepage'),
    path('projects/', views.projects, name='projects'),
    path('anouncement/', views.anouncement, name='anouncement'),
    path('view_updates/', views.view_updates, name='view_updates'),
]
