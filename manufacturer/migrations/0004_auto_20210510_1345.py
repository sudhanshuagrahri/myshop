# Generated by Django 3.0.13 on 2021-05-10 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0003_productdetails_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='approved',
            field=models.BooleanField(blank=True),
        ),
    ]
