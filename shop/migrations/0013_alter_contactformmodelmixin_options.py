# Generated by Django 4.1.3 on 2022-12-03 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_contactformmodelmixin_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactformmodelmixin',
            options={'ordering': ('full_name', 'date_sent', 'email', 'subject', 'message', 'cc_myself'), 'verbose_name': 'Contact form', 'verbose_name_plural': 'Contact forms'},
        ),
    ]
