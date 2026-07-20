from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from .models import Application
from .serializers import ApplicationSerializer
from applications.permissions import IsApplicant
from applications.permissions import IsApplicant, IsEmployer, IsApplicationOwner
from jobs.models import Job

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action == "create":
              
              permission_classes = [IsAuthenticated, IsApplicant]

        elif self.action in ["update", "partial_update"]:
            permission_classes = [
                IsAuthenticated, 
                IsEmployer,
                IsApplicationOwner,
            ]

        else:
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
         serializer.save(applicant=self.request.user)

    def get_queryset(self):
        user = self.request.user

        if user.role == "APPLICANT":
            return Application.objects.filter(applicant=user)

        elif user.role == "EMPLOYER":
            return Application.objects.filter(
                job__company=user.company
            )

        return Application.objects.none()
    

class EmployerDashboardView(APIView):

        permission_classes = [IsAuthenticated, IsEmployer]

        def get(self, request):

            company = request.user.company

            total_jobs = Job.objects.filter(company=company).count()

            total_applications = Application.objects.filter(
                job__company=company
            ).count()

            under_review = Application.objects.filter(
                job__company=company,
                status="UNDER_REVIEW"
            ).count()

            shortlisted = Application.objects.filter(
                job__company=company,
                status="SHORTLISTED"
            ).count()

            hired = Application.objects.filter(
                job__company=company,
                status="HIRED"
            ).count()

            rejected = Application.objects.filter(
                job__company=company,
                status="REJECTED"
            ).count()

            recent_applications = Application.objects.filter(
                job__company=company
            ).order_by("-applied_at")[:5]

            serializer = ApplicationSerializer(
                recent_applications,
                many=True
            )

            return Response({
                "total_jobs": total_jobs,
                "total_applications": total_applications,
                "under_review": under_review,
                "shortlisted": shortlisted,
                "hired": hired,
                "rejected": rejected,
                "recent_applications": serializer.data
            })
