# Generated by Django 2.2.3 on 2019-07-13 10:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_department_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
