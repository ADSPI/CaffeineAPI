from django.urls import path
from .views import *

urlpatterns  = [

    path('musics', MusicsView.as_view()),
]