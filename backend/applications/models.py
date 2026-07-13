from django.db import models
from django.conf import settings
from jobs.models import Job

# Create your models here.
STATUS_CHOISES = [
    ("Applied", "Applied"),
    ("Under Review", "Under Review"),
    ("Shortlisted", "Shortlisted"),
    ("Document Verification", "Document Verification"),
    ("Hired", "Hired"),
    ("Rejected", "Rejected"),
]

class Application(models.Model):
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )

    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE
    )

    resume = models.FileField(
        upload_to="resumes/",
        blank=True,
        null=True
    )

    cover_letter = models.TextField(
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOISES,
        default="Applied"

    )

    applied_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"{self.applicant.username}-{self.job.title}"
