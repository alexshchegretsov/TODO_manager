# Generated by Django 2.2.2 on 2019-06-07 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0012_auto_20190607_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.TextField(default='low'),
        ),
    ]