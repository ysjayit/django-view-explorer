from django.db import models

class Reminder(models.Model):
    title = models.CharField(max_length=255)
    reminder_time = models.DateTimeField()
    is_notified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
