# Generated by Django 5.1.7 on 2025-03-18 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vynzora_app', '0010_remove_service_unique_service_heading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='add_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='website',
            name='meta_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='website',
            name='meta_title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='website',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
