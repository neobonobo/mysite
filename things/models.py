from django.db import models

class ThingCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Thing(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ThingCategory, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    unit = models.CharField(max_length=50, help_text="e.g., kg, unit, bottle")
    value_per_unit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"
