# Generated by Django 5.0.6 on 2024-06-10 15:55

import django.db.models.deletion
import hashid_field.field
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('musics', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('reference_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False, unique=True)),
                ('alias', models.CharField(max_length=255)),
                ('civilStatus', models.CharField(max_length=255)),
                ('dateOfBirth', models.DateField()),
                ('phoneNumber', models.CharField(max_length=20)),
                ('firstHitSingle', models.CharField(blank=True, max_length=255, null=True)),
                ('isPremiem', models.BooleanField(default=True)),
                ('facebook', models.URLField(blank=True, max_length=255, null=True)),
                ('instagram', models.URLField(blank=True, max_length=255, null=True)),
                ('tiktok', models.URLField(blank=True, max_length=255, null=True)),
                ('youtube', models.URLField(blank=True, max_length=255, null=True)),
                ('profileImage', models.ImageField(upload_to='images/artist/profile')),
                ('coverImage', models.ImageField(upload_to='images/artist/cover')),
                ('totalViews', models.IntegerField(blank=True, null=True)),
                ('totalSubscribers', models.IntegerField(blank=True, null=True)),
                ('bio', models.CharField(blank=True, default='Je suis un artiste passionner par la melodie', max_length=255)),
                ('aboutMe', models.TextField(blank=True, default="Je suis un introverti qui prends de connaitr quelqu'un avat de commencer le debat", max_length=4096, null=True)),
                ('followers', models.ManyToManyField(blank=True, related_name='followers', to='accounts.subscriber')),
                ('styleMusic', models.ManyToManyField(blank=True, to='musics.stylemusical')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductionHouse',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('reference_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('instagram', models.CharField(blank=True, max_length=255, null=True)),
                ('tiktok', models.CharField(blank=True, max_length=255, null=True)),
                ('youtube', models.CharField(blank=True, max_length=255, null=True)),
                ('profileImage', models.ImageField(blank=True, null=True, upload_to='images/artist/cover')),
                ('coverImage', models.ImageField(blank=True, null=True, upload_to='images/artist/profile')),
                ('foundingYear', models.IntegerField(blank=True, null=True)),
                ('founder', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('website', models.URLField(blank=True, max_length=255, null=True)),
                ('contracts', models.ManyToManyField(blank=True, related_name='signed_contracts', to='accounts.artist')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Copyright',
            fields=[
                ('created_at', models.DateField(auto_now_add=True, null=True)),
                ('updated_at', models.DateField(auto_now_add=True, null=True)),
                ('reference_id', hashid_field.field.HashidAutoField(alphabet='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', min_length=7, prefix='', primary_key=True, serialize=False, unique=True)),
                ('registration_date', models.DateField()),
                ('expiration_date', models.DateField()),
                ('details', models.TextField()),
                ('holder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.productionhouse')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
