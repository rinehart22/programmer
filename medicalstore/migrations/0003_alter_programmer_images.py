# Generated by Django 4.0.1 on 2022-03-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalstore', '0002_programmer_tools'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programmer',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
