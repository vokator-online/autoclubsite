from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from tinymce.models import HTMLField


SUBJECT_CHOICES = (
    ('', _('Please Choose a Topic That Interests You')),
    (_('Join'), _('For Those Wishing to Become Club Members')),
    (_('Events'), _('Official Club Events and Organizational Matters')),
    (_('Suggestions'), _('Suggestions, Requests for Club Activities')),
    (_('Merchandise'), _('Club Merchandise')),
    (_('Other'), _('Other General Issues Related to Club Activities')),
)

TICKET_STATUSES = (
    ('new', _('new')),
    ('read', _('read')),
    ('processing', _('processing')),
    ('closed', _('closed')),
)

def get_access_key():
    return get_random_string(50)


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
    access_key = models.CharField(_("access key"), max_length=42, default=get_access_key)

    class Meta:
        verbose_name = _("ticket")
        verbose_name_plural = _("tickets")
        ordering = ['-sent_at']

    def __str__(self):
        return _("{} from {} sent {}").format(
            self.subject,
            self.sender_email,
            str(self.sent_at)[:19],
        )

    def clean(self) -> None:
        if self.sender:
            self.sender_email = self.sender.email
            self.sender_name = f"{self.sender.first_name} {self.sender.last_name}"

    def get_absolute_url(self):
        return reverse("ticket_detail", kwargs={"pk": self.pk})


class TicketMessage(models.Model):
    ticket = models.ForeignKey(Ticket, verbose_name=_("ticket"), on_delete=models.CASCADE, related_name="messages")
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
            self.recipient_email = self.recipient.email
            self.recipient_name = f"{self.recipient.first_name} {self.recipient.last_name}"

    def get_absolute_url(self):
        return reverse("ticketmessage_detail", kwargs={"pk": self.pk})


class Event(models.Model):
    image = models.ImageField(upload_to='images/events/', verbose_name=_("event image"), blank=True, null=True)
    title = models.CharField(max_length=100, verbose_name=_("title"))
    date = models.DateField(verbose_name=_("date"), db_index=True)
    content = HTMLField(verbose_name=_("content"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True)
    cancellation_date = models.DateField(blank=True, null=True, verbose_name=_("cancellation date"))

    class Meta:
        verbose_name = _("event")
        verbose_name_plural = _("events")
        ordering = ['-date']

    def __str__(self):
        return self.title


class Merchandise(models.Model):
    image = models.ImageField(_("image"),upload_to='images/merchandise/', null=True, blank=True)
    title = models.CharField(_("title"), max_length=100, db_index=True)
    price = models.DecimalField(_("price"), max_digits=10, decimal_places=2)
    quantity = models.IntegerField(_("quantity"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True, db_index=True)
    is_active = models.BooleanField(_("is active"), default=True)

    class Meta:
        verbose_name = _("merchandise")
        verbose_name_plural = _("merchandises")
        ordering = ['title']

    def __str__(self):
        return self.title
