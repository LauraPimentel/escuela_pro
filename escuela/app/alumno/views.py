from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.alumno.forms import AlumnoForm
# Create your views here.

def index(request):
    return render(request,'alumno/index.html')

def alumno_view(request):
    if request.method == 'POST':
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save()
        # return render(request, 'alumno/index.html')
        return redirect('index')
    else:
        form = AlumnoForm()
    return render(request, 'alumno/alumno_form.html', {'form':form})
