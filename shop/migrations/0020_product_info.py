# Generated by Django 4.1.5 on 2023-02-12 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_marqueproduct_tag_remove_product_marque_produit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='info',
            field=models.CharField(blank=True, choices=[('new', 'New'), ('promo', 'Promo'), ('sold', 'Sold'), ('', 'None')], default='', max_length=120, null=True),
        ),
    ]
