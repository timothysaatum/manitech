# Generated by Django 5.0.4 on 2024-04-14 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_alter_aboutsection_assuarance'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='whymanitech',
            options={'verbose_name_plural': 'Why Manitech'},
        ),
        migrations.AlterField(
            model_name='testimonies',
            name='testimony',
            field=models.CharField(max_length=250),
        ),
    ]
