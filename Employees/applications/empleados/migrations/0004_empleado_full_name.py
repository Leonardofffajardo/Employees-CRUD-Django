# Generated by Django 4.2.6 on 2023-11-02 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_empleado_hoja_vida_alter_empleado_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='full_name',
            field=models.CharField(blank=True, max_length=120, verbose_name='Nombre completo'),
        ),
    ]
