from django.urls import path
from .views import *

app_name = 'app'
urlpatterns = [
    path('', IndexPage, name='index'),
    path('createpersonne', CreatePersonne, name='createpersonne')
]
 