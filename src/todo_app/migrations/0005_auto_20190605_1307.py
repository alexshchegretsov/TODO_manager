# Generated by Django 2.2.2 on 2019-06-05 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0004_auto_20190605_1306'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-date']},
        ),
    ]