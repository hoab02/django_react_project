from django.urls import path
from .views import index

urlpatterns = [
    path('', index),
    path('joinn', index),
    path('create', index)
]