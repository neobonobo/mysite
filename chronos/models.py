from django.db import models
from django.utils.timezone import now
from django.conf import settings

class ImportantDate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="important_dates")
    name = models.CharField(max_length=255, help_text="Name of the event, e.g., 'Stopped Smoking'")
    description = models.TextField(blank=True, null=True, help_text="Additional details about the event")
    date = models.DateField(help_text="The date of the event")

    def __str__(self):
        return f"{self.name} - {self.date}"

    def time_since(self):
        """
        Calculate the time (days, months, years) since the date.
        """
        from datetime import date
        today = date.today()
        delta = today - self.date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        days = (delta.days % 365) % 30

        time_since_str = []
        if years > 0:
            time_since_str.append(f"{years} year{'s' if years > 1 else ''}")
        if months > 0:
            time_since_str.append(f"{months} month{'s' if months > 1 else ''}")
        if days > 0:
            time_since_str.append(f"{days} day{'s' if days > 1 else ''}")

        return ", ".join(time_since_str) if time_since_str else "Today"

class Todo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todos")
    title = models.CharField(max_length=255, help_text="Short description of the task")
    description = models.TextField(blank=True, null=True, help_text="Detailed information about the task")
    is_completed = models.BooleanField(default=False, help_text="Mark as completed when the task is done")
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(blank=True, null=True, help_text="Optional deadline for the task")

    def __str__(self):
        return f"{self.title} ({'Completed' if self.is_completed else 'Pending'})"
