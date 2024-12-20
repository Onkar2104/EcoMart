# Generated by Django 4.2.15 on 2024-12-20 09:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[('Men', 'Men'), ('Kids', 'Kids'), ('Women', 'Women'), ('Unisex', 'Unisex')], max_length=6)),
                ('product_category', models.CharField(max_length=30)),
                ('product_type', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.IntegerField(default='1000')),
                ('color', models.CharField(max_length=30)),
                ('brand', models.CharField(max_length=30)),
                ('discount', models.FloatField(blank=True, null=True)),
                ('discounted_price', models.IntegerField(blank=True, null=True)),
                ('stock', models.IntegerField(default='10')),
                ('available_stock', models.IntegerField()),
                ('sizes', models.CharField(max_length=5)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='products/')),
                ('product_video', models.FileField(blank=True, null=True, upload_to='products/')),
                ('shipping_price', models.IntegerField(blank=True, default='40', null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]