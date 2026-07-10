
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Company
from .serializers import CompanySerializer
from accounts.permissions import IsEmployer
from rest_framework.exceptions import ValidationError 

# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsEmployer]

    def perform_create(self, serializer):

        if Company.objects.filter(owner=self.request.user).exists():
            raise ValidationError({
                "You alredy own a Company !!"
            })
        
        serializer.save(owner=self.request.user)