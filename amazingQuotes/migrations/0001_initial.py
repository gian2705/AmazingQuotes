# Generated by Django 2.0.7 on 2018-07-12 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AmazingQuotesAbout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(verbose_name='About Amazing Quotes')),
            ],
            options={
                'verbose_name': 'About Amazing Quotes',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('type_of_event', models.CharField(max_length=128)),
                ('time', models.DateTimeField(verbose_name='Date and Time')),
                ('city', models.CharField(max_length=128, verbose_name='City')),
                ('location', models.CharField(max_length=64, verbose_name='Location')),
                ('price', models.IntegerField(verbose_name='Price (0 if free)')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of Product')),
                ('quantity', models.IntegerField(verbose_name='Quantity available')),
                ('price', models.IntegerField(verbose_name='Price')),
                ('type_of_product', models.CharField(choices=[('BOOK', 'Available'), ('CUP', 'Cup'), ('TSHIRT', 'T-shirt'), ('BAND', 'Wrist band')], max_length=64, verbose_name='Product Type')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Name of Team member')),
                ('title', models.CharField(max_length=64, verbose_name='Position')),
                ('about', models.TextField(verbose_name='About You')),
                ('image', models.ImageField(upload_to='', verbose_name='Profile image')),
            ],
            options={
                'verbose_name': 'Team Member',
                'verbose_name_plural': 'Team Members',
            },
        ),
    ]
