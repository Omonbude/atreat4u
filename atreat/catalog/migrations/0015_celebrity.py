# Generated by Django 2.0 on 2018-08-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_auto_20180829_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('movie', models.FileField(upload_to='')),
                ('slug', models.SlugField()),
                ('charity_name', models.CharField(max_length=100)),
                ('charity_image', models.ImageField(upload_to='')),
            ],
        ),
    ]
