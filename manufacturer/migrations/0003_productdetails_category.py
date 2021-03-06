# Generated by Django 3.0.13 on 2021-05-10 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_manufacturer'),
        ('manufacturer', '0002_productdetails_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetails',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='shop.Category'),
            preserve_default=False,
        ),
    ]
