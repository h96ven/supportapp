from django.contrib.auth.models import User
from django.db import models


class Ticket(models.Model):
    STATUS_UNSOLVED = 'U'
    STATUS_FROZEN = 'F'
    STATUS_SOLVED = 'S'

    STATUS_CHOICES = [
        (STATUS_UNSOLVED, 'Unsolved'),
        (STATUS_FROZEN, 'Frozen'),
        (STATUS_SOLVED, 'Solved'),
    ]
    topic = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default=STATUS_UNSOLVED)
    user = models.ForeignKey(
                User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.topic

    class Meta:
        ordering = ['-updated_at']


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
