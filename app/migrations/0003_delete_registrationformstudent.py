# Generated by Django 4.2.6 on 2024-04-15 05:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_rename_registrationform_registrationformstudent'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RegistrationFormStudent',
        ),
    ]
