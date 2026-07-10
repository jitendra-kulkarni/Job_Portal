from django.db import models
from django.conf import settings

# Create your models here.
class Company(models.Model):
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='company'
    )

    company_name = models.CharField(max_length=200)

    company_email = models.EmailField(
        blank=True,
        null=True
    )

    website = models.URLField(
        blank=True,
        null=True
    )

    logo = models.ImageField(
        upload_to="company_logos/",
        blank=True,
        null=True
    )

    description = models.TextField()

    industry = models.CharField(max_length=100)

    location = models.CharField(max_length=200)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name 