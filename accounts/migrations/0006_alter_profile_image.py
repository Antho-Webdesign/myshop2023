# Generated by Django 4.1.5 on 2023-01-17 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='prod/profile_img/default.png', null=True, upload_to='prod/profile_img/'),
        ),
    ]