# Generated by Django 5.0.4 on 2024-04-14 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_testimonies_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='alt',
            field=models.CharField(default='gallery image', max_length=100),
        ),
    ]
