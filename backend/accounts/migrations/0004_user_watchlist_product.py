# Generated by Django 4.0.6 on 2022-08-08 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('watchlist', '0001_initial'),
        ('accounts', '0003_alter_user_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist_product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='watchlist_items_for_user', to='watchlist.watchlistitem'),
        ),
    ]
