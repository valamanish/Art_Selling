# Generated by Django 5.0.1 on 2024-03-24 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artapp', '0018_alter_buyer_favourites_alter_buyer_totalbids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bidTimeStamp',
        ),
    ]
