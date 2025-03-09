from django.db import models
from datetime import date

class Task(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Due Today', 'Due Today'),
        ('Overdue', 'Overdue'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming', editable=False)

    def save(self, *args, **kwargs):
        """Automatically updates the status before saving based on due_date."""
        today = date.today()
        if self.due_date < today:
            self.status = 'Overdue'
        elif self.due_date == today:
            self.status = 'Due Today'
        else:
            self.status = 'Upcoming'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} - {self.status}"
