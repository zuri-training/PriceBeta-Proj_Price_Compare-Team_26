# Generated by Django 4.0.6 on 2022-08-09 06:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import products.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('image_url', models.URLField()),
                ('slug', models.SlugField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_sub_category', models.BooleanField(default=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_categories', to='products.category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('brand', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(limit_choices_to={'is_sub_category': True}, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.category')),
                ('loved', models.ManyToManyField(null=True, related_name='favourites', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
                ('favicon', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SalesDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=1.0, max_digits=20, validators=[products.validators.min_price_validator])),
                ('search_url', models.URLField(default='https://www.testing.com/')),
                ('product_url', models.URLField(default='https://www.testing.com/')),
                ('available', models.BooleanField(default=True)),
                ('description', models.TextField()),
                ('modified', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_details', to='products.product')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.store')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField(blank=True, max_length=250, null=True)),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=3, validators=[products.validators.max_rating_validator])),
                ('is_scrapper', models.BooleanField(default=False)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.product')),
                ('store', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='products.store')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-date_time',),
            },
        ),
        migrations.AddConstraint(
            model_name='salesdetail',
            constraint=models.UniqueConstraint(fields=('store', 'product'), name='unique_product_and_store'),
        ),
        migrations.AddConstraint(
            model_name='product',
            constraint=models.UniqueConstraint(condition=models.Q(models.Q(('name', ''), _negated=True), models.Q(('brand', ''), _negated=True)), fields=('name', 'brand'), name='unique_product_and_brand'),
        ),
    ]
