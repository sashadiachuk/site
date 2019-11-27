from django.shortcuts import render
from django.urls import path, include
from . import views
urlpatterns = (
    # path('polls/', include('polls.urls')),#добавили варінт перехода по адресі http://127.0.0.1:8000/-локал хост + /polls;
    # polls/- можна міняти
    path('', views.personal, name='personal'),
    path('prof/', views.prof, name='prof'),
    path('dots/', views.dots, name='dots'),
    path('st_v/', views.st_v, name='st_v'),
    path('file/', views.file, name = 'rob-navch-plany2010'),
    path('graf/', views.graf, name = 'graf'),
    path('', views.default_map, name='map')

)




