# Generated by Django 4.0.1 on 2022-03-01 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicalstore', '0003_alter_programmer_images'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programmer',
            old_name='images',
            new_name='image',
        ),
    ]
