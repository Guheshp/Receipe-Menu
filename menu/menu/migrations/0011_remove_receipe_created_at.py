# Generated by Django 5.0.1 on 2024-01-25 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0010_receipe_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='receipe',
            name='created_at',
        ),
    ]