# Generated by Django 2.0 on 2018-10-31 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_auto_20181031_2129'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MovieBid',
            new_name='CelebrityBid',
        ),
    ]