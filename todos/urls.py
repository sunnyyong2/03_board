from django.urls import path
from . import views

urlpatterns = [
    #Create
    path('new/',views.new),
    path('create/',views.create),
    #Read
    path('',views.index),
    path('<int:todo_id>/',views.detail),
    #update
    path('<int:todo_id>/edit/',views.edit),
    path('<int:todo_id>/update/',views.update),    
    #delete
    path('<int:todo_id>/delete/',views.delete),
]