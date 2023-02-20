from django.urls import path, include
from . import views
urlpatterns = [

    path('', views.home,name='home'),
    path('addNotes/', views.addNotes,name='addNotes'),
    path('notes/', views.notes,name='notes'),
]