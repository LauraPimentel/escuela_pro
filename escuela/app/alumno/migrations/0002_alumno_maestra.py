# Generated by Django 2.0.3 on 2018-03-22 02:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
        ('alumno', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='maestra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='docente.Maestra'),
        ),
    ]
