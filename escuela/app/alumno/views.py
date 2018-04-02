from django.shortcuts import render, redirect
from django.http import HttpResponse
from app.alumno.forms import AlumnoForm
from app.alumno.models import Alumno
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

def alumno_list(request):
    alumno = Alumno.objects.all().order_by('folio')
    contexto = {'alumno':alumno}
    return render(request, 'alumno/alumno_list.html', contexto)

def alumno_edit(request, folio):
    alumno = Alumno.objects.get(folio=folio)
    if request.method == 'GET':
        form = AlumnoForm(instance=alumno)
    else:
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
        return redirect('alumno_listar')
    return render(request, 'alumno/alumno_form.html',{'form':form})

def alumno_delete(request, folio):
    alumno = Alumno.objects.get(folio=folio)
    if request.method == 'POST':
        alumno.delete()
        return redirect('alumno_listar')
    return render(request, 'alumno/alumno_delete.html', {'alumno':alumno})
