from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Job
from .serializers import JobSerializer
from accounts.permissions import IsEmployer
from accounts.permissions import IsJobOwner


class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


    def get_permissions(self):

        if self.action in ["list", "retrieve"]:
            return [IsAuthenticatedOrReadOnly()]
        
        elif self.action == "create":
            return [IsEmployer()]
        
        return [IsEmployer(), IsJobOwner()]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ["location", "employment_type", "experience_level"]

    search_fields = ["title", "description", "company__company_name"]

    ordering_fields = ["salary", "created_at"]