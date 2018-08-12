# Generated by Django 2.0.7 on 2018-08-12 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180810_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.CharField(auto_created=True, blank=True, default='Dont edit this field', max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('LEADERSHIP', 'Leadership'), ('LIFE COACHING', 'Life Coaching'), ('RELATIONSHIP', 'Relationship'), ('ENTREPRENEURSHIP', 'Entrepreneurship')], default='LIFE', max_length=64, verbose_name='Post Category'),
        ),
        migrations.AlterField(
            model_name='post',
            name='feature',
            field=models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=5, verbose_name='Featured?'),
        ),
    ]
