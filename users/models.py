# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models  # new
from django.db.models.signals import post_save  # new
from django.dispatch import receiver  # new

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.email if self.email else self.username

class UserProfile(models.Model):  # new
    user = models.OneToOneField(
        "users.CustomUser",
        on_delete=models.CASCADE,
    )
    # add additional fields for UserProfile
    birthday = models.DateField(blank=True, null=True, help_text="User's birthday")
    last_smoking = models.DateField(blank=True, null=True, help_text="Date of last smoking")
    title = models.CharField(max_length=255, blank=True, null=True, help_text="User's title")

    def __str__(self):
        return f"Profile for {self.user.email}"

    class Meta:
        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

@receiver(post_save, sender=CustomUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)
    else:
        instance.userprofile.save()
