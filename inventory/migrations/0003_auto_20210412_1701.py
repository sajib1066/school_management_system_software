# Generated by Django 3.1 on 2021-04-12 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
        ('inventory', '0002_auto_20201125_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentitems',
            name='students_given',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='student.enrolledstudent'),
        ),
    ]
