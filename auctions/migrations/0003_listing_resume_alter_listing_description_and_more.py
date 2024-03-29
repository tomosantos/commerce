# Generated by Django 5.0.1 on 2024-01-29 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_category_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='resume',
            field=models.CharField(blank=True, max_length=400),
        ),
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
