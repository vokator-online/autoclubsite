# Generated by Django 5.0.3 on 2024-04-08 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_merchandise'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='merchandise',
            options={'ordering': ['title'], 'verbose_name': 'merchandise', 'verbose_name_plural': 'merchandises'},
        ),
    ]