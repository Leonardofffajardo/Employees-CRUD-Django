# Generated by Django 4.2.6 on 2023-10-25 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Habilidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidad', models.CharField(max_length=50, verbose_name='Habilidad')),
            ],
        ),
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['-first_name'], 'verbose_name': 'Empleado', 'verbose_name_plural': 'Empleados'},
        ),
        migrations.AlterUniqueTogether(
            name='empleado',
            unique_together={('first_name', 'last_name')},
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='empleados.habilidades'),
        ),
    ]
