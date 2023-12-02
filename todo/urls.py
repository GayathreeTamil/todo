from django.urls import path 
from . import views

urlpatterns = [
    # add task
    path('addTask/', views.addTask, name = 'addTask'),
    # mark as done
    path('markAsDone/<int:pk>/', views.markAsDone, name = 'markAsDone'),
    # mark as undone
    path('markAsUndone/<int:pk>/',views.markAsUndone, name='markAsUndone'),
    # edit feature
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
    # delete task
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask')
]