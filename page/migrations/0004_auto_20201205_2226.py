# Generated by Django 3.1.3 on 2020-12-05 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_auto_20201205_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='page'),
        ),
    ]
