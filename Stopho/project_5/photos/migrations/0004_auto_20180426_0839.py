# Generated by Django 2.0.4 on 2018-04-26 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20180424_0016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uploadimages',
            options={'verbose_name': 'image', 'verbose_name_plural': 'photos'},
        ),
        migrations.AlterField(
            model_name='uploadimages',
            name='img_description',
            field=models.CharField(max_length=100),
        ),
    ]