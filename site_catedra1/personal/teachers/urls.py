from django.shortcuts import render
from django.urls import path, include
from . import views
urlpatterns = [
    #path('polls/', include('polls.urls')),#добавили варінт перехода по адресі http://127.0.0.1:8000/-локал хост + /polls;
    # polls/- можна міняти
    # path('', views.personal, name = 'personal'),
    # path('news/', views.news, name = 'news')

]



