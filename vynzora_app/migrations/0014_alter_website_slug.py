# Generated by Django 5.1.7 on 2025-03-24 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vynzora_app', '0013_career_model_candidate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='website',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True),
        ),
    ]
