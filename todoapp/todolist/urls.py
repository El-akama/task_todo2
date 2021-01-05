from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("update/<int:pk>/", update_task, name="update_task"),
    path("delete/<int:pk>/", delete_task, name="delete_task"),
    
]