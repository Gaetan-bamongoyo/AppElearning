# Generated by Django 4.0.1 on 2023-09-04 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearningApp', '0005_contenus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contenus',
            name='niveau',
            field=models.CharField(max_length=50, null=True),
        ),
    ]