from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Application
from .serializers import ApplicationSerializer
from applications.permissions import IsApplicant

# Create your views here.
class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

    def get_permissions(self):
        if self.action == "create":
              
              permission_classes = [IsAuthenticated, IsApplicant]

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