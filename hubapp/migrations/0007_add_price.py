# Generated by Django 3.0.6 on 2020-06-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubapp', '0006_auto_20200606_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='price',
            field=models.DecimalField(decimal_places=2, default=True, max_digits=6),
        ),
    ]
