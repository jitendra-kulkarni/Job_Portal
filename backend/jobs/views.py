from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Job
from .serializers import JobSerializer
from accounts.permissions import IsEmployer
from accounts.permissions import IsJobOwner


class JobViewSets(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [IsAuthenticatedOrReadOnly()]

        return [IsEmployer()]

    def perform_create(self, serializer):
        serializer.save(company=self.request.user.company)


    def get_permissions(self):

        if self.action in ["list", "retrieve"]:
            return [IsAuthenticatedOrReadOnly()]
        
        elif self.action == "create":
            return [IsEmployer()]
        
        return [IsEmployer(), IsJobOwner()]