from django.db import models
from companies.models import Company

# Create your models here.
class Job(models.Model):
    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        related_name="jobs"
    )

    title = models.CharField(max_length=255)
    description = models.TextField()
    requirements = models.TextField()

    location = models.CharField(max_length=200)

    salary = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    vacancies = models.PositiveIntegerField(default=1)

    EMPLOYMENT_TYPE_CHOISES = [
        ('FULL_TIME','full Time'),
        ("PART_TIME", "Part Time"),
        ("INTERNSHIP", "Internship"),
        ("CONTRACT", "Contract"),
        ("REMOTE", "Remote"),
    ]

    employment_type = models.CharField(
        max_length=20,
        choices=EMPLOYMENT_TYPE_CHOISES
    )

    EXPERIENCE_LEVEL_CHOISES = [
        ("FRESHER", "Fresher"),
        ("JUNIOR", "Junior (1-2 years)"),
        ("MID", "Mid-Level (3-5 years)"),
        ("SENIOR", "Senior (5+ years)"),
    ]
    experience_level = models.CharField(
        max_length=20,
        choices=EXPERIENCE_LEVEL_CHOISES,
        default="FRESHER"
    )

    is_active = models.BooleanField(default=True)
    application_deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title}-{self.company}"  
