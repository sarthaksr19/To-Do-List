from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('delete/<str:pk>', views.delete,name='delete')
    # here pk is collecting the todo id and sent it in views.py delete function
]
