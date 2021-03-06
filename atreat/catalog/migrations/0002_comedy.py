# Generated by Django 2.0 on 2018-08-27 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comedy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField()),
                ('time', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=200)),
                ('singles_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('double_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('round_table_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('vip_table_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
            ],
        ),
    ]
