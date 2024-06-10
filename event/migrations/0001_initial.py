# Generated by Django 5.0.6 on 2024-06-06 22:56

import django.db.models.deletion
import django.utils.timezone
import hashid_field.field
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TicketInfo',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('reference_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False, unique=True)),
                ('available_tickets', models.IntegerField()),
                ('price', models.IntegerField(blank=True, default=0, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('reference_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('takePlaceAt', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='events/images/')),
                ('guestList', models.ManyToManyField(related_name='invited_to_event', to='accounts.subscriber')),
                ('owner', models.ManyToManyField(blank=True, related_name='organizer_event', to='accounts.user')),
                ('ticketInfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.ticketinfo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventTicket',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('reference_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False, unique=True)),
                ('purchase_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_reserved', models.BooleanField(default=False)),
                ('reservation_expiry', models.DateTimeField(blank=True, null=True)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.user')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='event.event')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]