# Generated by Django 4.2.15 on 2024-12-22 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_addproduct_product_image2_addproduct_product_image3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addproduct',
            name='brand',
            field=models.CharField(choices=[('Zara', 'Zara'), ('Titan', 'Titan'), ('River', 'River'), ('Asos', 'Asos')], max_length=30),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='gender',
            field=models.CharField(choices=[('Kids', 'Kids'), ('Men', 'Men'), ('Unisex', 'Unisex'), ('Women', 'Women')], max_length=6),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='product_category',
            field=models.CharField(choices=[('Accessories', 'Accessories'), ('Watch', 'Watch'), ('Clothing', 'Clothing'), ('Shoes', 'Shoes')], max_length=30),
        ),
        migrations.AlterField(
            model_name='addproduct',
            name='product_type',
            field=models.CharField(choices=[('Wedding', 'Wedding'), ('Kurtas', 'Kurtas'), ('Formal', 'Formal'), ('Casual', 'Casual'), ('Sports', 'Sports'), ('Business_casual', 'Business_casual')], max_length=20),
        ),
    ]