# Generated by Django 5.0.1 on 2024-02-29 06:33

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artapp', '0006_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[300, 300], upload_to=''),
        ),
    ]
