# Generated by Django 5.0.3 on 2024-03-23 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, verbose_name='apie save'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='facebook_url'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='instagram_url'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pinterest_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='pinterest_url'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/profile/', verbose_name='profilio nuotrauka'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='twitter_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='twitter_url'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='puslapio nuoroda'),
        ),
    ]
