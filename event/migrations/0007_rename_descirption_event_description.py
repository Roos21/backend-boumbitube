# Generated by Django 5.0.6 on 2024-06-10 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_event_descirption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='descirption',
            new_name='description',
        ),
    ]
