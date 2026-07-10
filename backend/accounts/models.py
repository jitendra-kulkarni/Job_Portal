from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOISES = (
        ('APPLICANT', 'Applicant'),
        ('EMPLOYER', 'Employer'),
    )

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOISES,
        default='APPLICANT'
    )

    def __str__(self):
        return self.username