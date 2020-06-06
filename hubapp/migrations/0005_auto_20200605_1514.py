# Generated by Django 3.0.6 on 2020-06-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hubapp', '0004_add_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add',
            name='aproval',
        ),
        migrations.RemoveField(
            model_name='add',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='add',
            name='category',
        ),
        migrations.RemoveField(
            model_name='add',
            name='condition',
        ),
        migrations.RemoveField(
            model_name='add',
            name='default_image',
        ),
        migrations.RemoveField(
            model_name='add',
            name='description',
        ),
        migrations.RemoveField(
            model_name='add',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='add',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='add',
            name='image_3',
        ),
        migrations.RemoveField(
            model_name='add',
            name='image_4',
        ),
        migrations.RemoveField(
            model_name='add',
            name='negotiable',
        ),
        migrations.RemoveField(
            model_name='add',
            name='user',
        ),
        migrations.AlterField(
            model_name='add',
            name='location',
            field=models.CharField(choices=[('kumasi', 'kumasi'), ('Accra', 'Accra'), ('Tamale', 'Tamale')], max_length=200),
        ),
    ]
