# Generated by Django 2.0.4 on 2018-04-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20180423_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadimages',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
        migrations.AlterIndexTogether(
            name='uploadimages',
            index_together={('id', 'slug')},
        ),
    ]
