# Generated by Django 5.0 on 2023-12-28 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_ultras', '0032_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.FileField(default='', upload_to='media/'),
        ),
    ]
