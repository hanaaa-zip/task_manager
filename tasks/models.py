from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Overdue', 'Overdue'),
        ('Completed', 'Completed'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def save(self, *args, **kwargs):
        """Remove automatic status update so users can edit manually."""
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
