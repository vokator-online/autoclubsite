# Generated by Django 5.0.3 on 2024-03-23 18:15

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_ticket_content_alter_ticket_sender_email_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ticket',
            options={'ordering': ['-sent_at'], 'verbose_name': 'užklausa', 'verbose_name_plural': 'užklausos'},
        ),
        migrations.AlterModelOptions(
            name='ticketmessage',
            options={'ordering': ['-sent_at'], 'verbose_name': 'užklausos pranešimas', 'verbose_name_plural': 'užklausos pranešimai'},
        ),
        migrations.AlterField(
            model_name='ticket',
            name='content',
            field=models.TextField(blank=True, default='', max_length=10000, verbose_name='turinys'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='mail_sent',
            field=models.BooleanField(default=False, verbose_name='išsiųstas elektroninis laiškas'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='support_tickets', to=settings.AUTH_USER_MODEL, verbose_name='siuntėjas'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sender_email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='elektroninis pašto adresas'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sender_name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='vardas ir pavardė'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='išsiųsta'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('new', 'nauja'), ('read', 'perskaityta'), ('processing', 'apdorojama'), ('closed', 'uždaryta')], db_index=True, default='new', max_length=15, verbose_name='būsena'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='subject',
            field=models.CharField(choices=[('', '-- Prašom pasirinkti --'), ('Join', 'Norintiems tapti klubo nariais'), ('Events', 'Oficialūs klubo renginiai ir organizaciniai klausimai'), ('Suggestions', 'Pasiūlymai, pageidavimai klubo veiklai'), ('merchandise', 'Klubo atributika'), ('Other', 'Kiti bendri su klubo veikla susiję klausimai')], default='', max_length=50, verbose_name='tema'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='content',
            field=models.TextField(blank=True, default='', max_length=10000, verbose_name='turinys'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='perskaityta'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='mail_sent',
            field=models.BooleanField(default=False, verbose_name='išsiųstas elektroninis laiškas'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_ticket_messages', to=settings.AUTH_USER_MODEL, verbose_name='gavėjas'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='recipient_email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='elektroninis pašto adresas'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='recipient_name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='vardas ir pavardė'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sent_ticket_messages', to=settings.AUTH_USER_MODEL, verbose_name='siuntėjas'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='sender_email',
            field=models.EmailField(blank=True, db_index=True, max_length=254, null=True, verbose_name='elektroninis pašto adresas'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='sender_name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='vardas ir pavardė'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='sent_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='išsiųsta'),
        ),
        migrations.AlterField(
            model_name='ticketmessage',
            name='ticket',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.ticket', verbose_name='užklausa'),
        ),
    ]
