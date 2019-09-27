# Generated by Django 2.0 on 2018-09-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_usersalon'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserComedy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=200)),
                ('singles_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=50, null=True)),
                ('double_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=50, null=True)),
                ('round_table_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=50, null=True)),
                ('vip_table_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, max_length=50, null=True)),
            ],
        ),
    ]