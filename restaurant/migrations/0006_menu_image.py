# Generated by Django 4.2.4 on 2023-08-27 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_menu_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='image',
            field=models.ImageField(default=None, upload_to='assets'),
            preserve_default=False,
        ),
    ]