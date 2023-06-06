from django.urls import path, include
from .views import index

urlpatterns = [
    path(route='', view=index, name='index')
]
