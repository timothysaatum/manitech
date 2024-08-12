# Generated by Django 5.0.4 on 2024-04-14 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='manitech/images')),
                ('content', models.CharField(max_length=15)),
                ('value_proposition_1', models.CharField(max_length=13)),
                ('value_proposition_2', models.CharField(max_length=13)),
                ('value_proposition_3', models.CharField(max_length=13)),
                ('assuarance', models.CharField(max_length=30)),
                ('video_link', models.URLField()),
                ('video_background', models.ImageField(upload_to='manitech/images')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('phone_number', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='manitech/images')),
            ],
            options={
                'verbose_name_plural': 'Gallery',
            },
        ),
        migrations.CreateModel(
            name='HomeSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='manitech/images')),
                ('video_link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NewsAndProjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('image', models.ImageField(upload_to='manitech/images')),
                ('title', models.CharField(max_length=10)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'News And Projects',
            },
        ),
        migrations.CreateModel(
            name='ProductsSection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('5kg Bag', '5kg Bag'), ('25kg Bag', '25kg Bag'), ('50kg bag', '50kg bag'), ('100kg', '100kg')], max_length=10)),
                ('image', models.ImageField(upload_to='manitech/images')),
                ('short_notes', models.CharField(max_length=5)),
                ('price', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
                ('role', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='manitech/images')),
                ('facebook_url', models.URLField()),
                ('x_url', models.URLField()),
                ('instagram_url', models.URLField()),
                ('linkedin_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Testimonies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('testimony', models.CharField(max_length=31)),
                ('name_of_customer', models.CharField(max_length=50)),
                ('occupation', models.CharField(max_length=50)),
                ('rating', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Testimonies',
            },
        ),
        migrations.CreateModel(
            name='ValueProposition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=5)),
                ('short_notes', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='WhyManitech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('date_modified', models.DateField(auto_now=True)),
                ('why_us', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Manitech',
            },
        ),
    ]
