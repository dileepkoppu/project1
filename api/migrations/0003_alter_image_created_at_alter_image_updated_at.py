# Generated by Django 4.0.3 on 2022-03-25 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_image_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='image',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]