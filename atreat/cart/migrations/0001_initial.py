<<<<<<< HEAD
# Generated by Django 2.1.3 on 2019-01-05 15:09

from django.conf import settings
import django.contrib.auth.models
=======
# Generated by Django 2.0 on 2018-09-13 20:30

from django.conf import settings
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<< HEAD
=======
        ('catalog', '0020_auto_20180909_2127'),
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
    ]

    operations = [
        migrations.CreateModel(
<<<<<<< HEAD
            name='CelebrityBid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=django.contrib.auth.models.User, max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CinemaQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MealCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MealQuantity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RebidCeleb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default=django.contrib.auth.models.User, max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, default=0.0, max_digits=15, max_length=50)),
                ('celeb', models.CharField(default='none', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserCinemas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cinema_name', models.CharField(max_length=200)),
                ('movie', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
                ('rating', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('time', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComedyDouble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
                ('time', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=200)),
                ('double_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('category', models.CharField(default='Double', max_length=30)),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComedyRound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
                ('time', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=200)),
                ('round_table_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('category', models.CharField(default='Round Table', max_length=30)),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComedySingle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
                ('time', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=200)),
                ('singles_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('category', models.CharField(default='Singles', max_length=30)),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserComedyVip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='')),
                ('time', models.CharField(max_length=10)),
                ('venue', models.CharField(max_length=200)),
                ('vip_table_price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('category', models.CharField(default='Vip Table', max_length=30)),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('real_restaurant', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('Menu', models.CharField(max_length=50)),
                ('Brand', models.CharField(blank=True, max_length=50, null=True)),
                ('Size', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('quantity', models.IntegerField(default=1)),
                ('Total_price', models.CharField(default=0, max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserSalon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('style', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('gender', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
=======
            name='CinemasDetail_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.CinemasDetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Comedy_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Comedy')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Meal_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Meal')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MealCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MealPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('restaurant', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('Menu', models.CharField(max_length=50)),
                ('Brand', models.CharField(blank=True, max_length=50, null=True)),
                ('Size', models.CharField(blank=True, max_length=50, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SalonDetail_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.SalonDetail')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='salondetail_cart',
            name='usercart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.UserCart'),
        ),
        migrations.AddField(
            model_name='meal_cart',
            name='usercart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.UserCart'),
        ),
        migrations.AddField(
            model_name='comedy_cart',
            name='usercart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.UserCart'),
        ),
        migrations.AddField(
            model_name='cinemasdetail_cart',
            name='usercart',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='cart.UserCart'),
>>>>>>> 714da70c489406f200282bb4a66b5e38148dfd8c
        ),
    ]