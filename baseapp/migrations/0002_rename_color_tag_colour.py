# Generated by Django 5.1.1 on 2024-09-04 09:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('baseapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tag',
            old_name='color',
            new_name='colour',
        ),
    ]
