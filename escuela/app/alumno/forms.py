from django import forms
from app.alumno.models import Alumno

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields= [
            'folio',
            'nombre',
            'apellido_paterno',
            'apellido_materno',
            'edad',
            'fecha_nacimiento',
            'tutor',
            'direccion',
            'telefono',
            'maestra',
        ]
        labels = {
            'folio': 'Folio',
            'nombre': 'Nombre',
            'apellido_paterno': 'Apellido Paterno',
            'apellido_materno': 'Apellido Materno',
            'edad': 'Edad',
            'fecha_nacimiento': 'Fecha De Nacimiento',
            'tutor': 'Tutor',
            'direccion': 'Dirección',
            'telefono': 'Teléfono',
            'maestra': 'Maestra',
        }
        widgets = {
            'folio': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_paterno': forms.TextInput(attrs={'class':'form-control'}),
            'apellido_materno': forms.TextInput(attrs={'class':'form-control'}),
            'edad': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': forms.TextInput(attrs={'class':'form-control'}),
            'tutor': forms.TextInput(attrs={'class':'form-control'}),
            'direccion': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'maestra': forms.Select(attrs={'class':'form-control'}),
        }
