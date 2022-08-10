from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    class TicketStatus(models.TextChoices):
        STATUS_UNSOLVED = 'U', _('Unsolved')
        STATUS_FROZEN = 'F', _('Frozen')
        STATUS_SOLVED = 'S', _('Solved')

    topic = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=TicketStatus.choices,
        default=TicketStatus.STATUS_UNSOLVED)
    user = models.ForeignKey(
                User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ('-updated_at',)


class Reply(models.Model):
    ticket = models.ForeignKey(
                Ticket, on_delete=models.CASCADE,
                null=True, related_name='replies')
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
                User, on_delete=models.SET_NULL,
                null=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'Replies'
