# Generated by Django 5.0.4 on 2024-04-14 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_alter_aboutsection_assuarance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutsection',
            name='assuarance',
            field=models.CharField(max_length=300),
        ),
    ]