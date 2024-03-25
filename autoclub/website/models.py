from typing import Iterable
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User


SUBJECT_CHOICES = (
    ('', _('-- Please choose --')),
    ('Join', _('For those who want to join the club')),
    ('Events', _('Official club events and organisational matters')),
    ('Suggestions', _('Suggestions, complaints for club activities')),
    ('merchandise', _('Club merchandise')),
    ('Other', _('Other general issues related to the club\'s activities')),
)

TICKET_STATUSES = (
    ('new', _('new')),
    ('read', _('read')),
    ('processing', _('processing')),
    ('closed', _('closed')),
)


class Ticket(models.Model):
    subject = models.CharField(_("subject"), max_length=50, choices=SUBJECT_CHOICES, default='')
    content = models.TextField(_("content"), max_length=10000, default='', blank=True)
    sender = models.ForeignKey(
        User, 
        verbose_name=_("sender"), 
        on_delete=models.CASCADE, 
        related_name='support_tickets', 
        null=True, blank=True,
    )
    sender_name = models.CharField(_("full name"), max_length=100, null=True, blank=True, db_index=True)
    sender_email = models.EmailField(_("email"), max_length=254, null=True, blank=True, db_index=True)
    sent_at = models.DateTimeField(_("sent at"), auto_now_add=True, db_index=True)
    mail_sent = models.BooleanField(_("email sent"), default=False)
    status = models.CharField(_("status"), max_length=15, choices=TICKET_STATUSES, default='new', db_index=True)

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        ordering = ['-sent_at']

    def __str__(self):
        return _("{} from {} sent {}").format(
            self.subject,
            self.sender_email,
            self.sent_at,
        )

    def clean(self) -> None:
        if self.sender:
            self.sender_email = self.sender.email
            self.sender_name = f"{self.sender.first_name} {self.sender.last_name}"

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})


class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name=_("ticket"), on_delete=models.CASCADE)
    content = models.TextField(_("content"), max_length=10000, default='', blank=True)
    sender = models.ForeignKey(
        User, 
        verbose_name=_("sender"), 
        on_delete=models.CASCADE, 
        related_name='sent_ticket_messages', 
        null=True, blank=True,
    )
    recipient = models.ForeignKey(
        User,
        verbose_name=_("recipient"), 
        on_delete=models.CASCADE,
        related_name='received_ticket_messages',
        null=True, blank=True,
    )
    sender_name = models.CharField(_("full name"), max_length=100, null=True, blank=True, db_index=True)
    sender_email = models.EmailField(_("email"), max_length=254, null=True, blank=True, db_index=True)
    recipient_name = models.CharField(_("full name"), max_length=100, null=True, blank=True, db_index=True)
    recipient_email = models.EmailField(_("email"), max_length=254, null=True, blank=True, db_index=True)
    sent_at = models.DateTimeField(_("sent at"), auto_now_add=True, db_index=True)
    mail_sent = models.BooleanField(_("email sent"), default=False)
    is_read = models.BooleanField(_("is read"), default=False)

    class Meta:
        verbose_name = _("ticket message")
        verbose_name_plural = _("ticket messages")
        ordering = ['-sent_at']

    def __str__(self):
        return _("ticket: {} message from {} to {} at {}").format(
            self.ticket.id,
            self.sender_email,
            self.recipient_email,
            self.sent_at,
        )

    def clean(self) -> None:
        if self.sender:
            self.sender_email = self.sender.email
            self.sender_name = f"{self.sender.first_name} {self.sender.last_name}"
        if self.recipient:
            self.recipient_name = self.recipient.email
            self.recipient_name = f"{self.recipient.first_name} {self.recipient.last_name}"

    def get_absolute_url(self):
        return reverse("ticketmessage_detail", kwargs={"pk": self.pk})
