# Generated by Django 3.1.6 on 2021-04-01 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210401_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('teacher', 'Teacher')], default=['Student', 'Teacher'], max_length=30),
        ),
    ]