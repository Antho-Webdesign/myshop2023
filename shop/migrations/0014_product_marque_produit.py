# Generated by Django 4.1.3 on 2022-12-06 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_alter_contactformmodelmixin_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='marque_produit',
            field=models.CharField(default='', max_length=120),
        ),
    ]
