# Generated by Django 5.0 on 2023-12-23 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ultras', '0027_alter_product_description_alter_product_material_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
    ]