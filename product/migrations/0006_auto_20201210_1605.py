# Generated by Django 3.1.3 on 2020-12-10 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20201210_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
