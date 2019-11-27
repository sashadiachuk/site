import os
from django.shortcuts import render, render_to_response
from .forms import *
from .teachers.models import *
from django.views.static import serve

def personal(request):
     form = abituraForm(request.POST)
     if request.method == 'POST':
            print(request.POST)
            new_form = form.save()
            form=form.clean()
     form = abituraForm()

     return render(request, "abiturA.html", locals())
def prof(request):
    ctx1 = Teacher_prof.objects.all()
    return render(request, 'teachers/prof.html', locals())
def dots(request):
    ctx2 = Teacher_dotsent.objects.all()
    return render(request, 'teachers/dots.html', locals())
def st_v(request):
    ctx3 = Teacher_st_vikl.objects.all()
    return render(request, 'teachers/st_v.html', locals())
def file(request):
    filepath = 'personal/static/img/zipka.zip'
    return serve(request, os.path.basename(filepath), os.path.dirname(filepath))
def graf(request):
     return render(request, 'teachers/graf.html', locals())
def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'map.html',{ 'mapbox_access_token': mapbox_access_token })