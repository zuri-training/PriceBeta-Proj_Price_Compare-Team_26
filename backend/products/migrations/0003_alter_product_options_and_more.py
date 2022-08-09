# Generated by Django 4.0.6 on 2022-08-09 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_remove_product_loved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('-brand',), 'verbose_name_plural': 'products'},
        ),
        migrations.RemoveConstraint(
            model_name='product',
            name='unique_product_and_brand',
        ),
    ]
