from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):

    job_title = serializers.CharField(
            source ="job.title",
            read_only = True 

    )

    applicant_username = serializers.CharField(
            source ="applicant.username",
            read_only = True 

    )

    applicant_email = serializers.CharField(
            source ="applicant.email",
            read_only = True 

    )
    
    class Meta:
        model = Application
        fields = "__all__"
        read_only_fields = ["applicant", "applied_at"]

        

    def validate(self, attrs):

        if self.instance:
            return attrs
        
        applicant = self.context["request"].user 
        job = attrs["job"]

        if Application.objects.filter(applicant=applicant, job=job).exists():
            raise serializers.ValidationError(
                "You have already applied for this Job"
            )
        
        return attrs
    
    def update(self, instance, validated_data):

        request = self.context["request"]

        if request.user.role == "EMPLOYER":
            instance.status = validated_data.get("status", instance.status)
            instance.save(update_fields = ["status"])

        return instance