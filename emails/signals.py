from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from support.models import Ticket


# Sending of emails on status change
@receiver(post_save, sender=Ticket)
def update_status(sender, instance, created, **kwargs):
    if not created:
        if instance.status == 'S' or instance.status == 'F':
            send_mail(
                'New status!',
                'The status of the topic you created has been changed.',
                'noreply@email.com',
                [instance.user.email]
            )
