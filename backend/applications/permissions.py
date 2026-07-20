from rest_framework.permissions import BasePermission


class IsApplicant(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "APPLICANT"
        )

class IsEmployer(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role == "EMPLOYER"
        )


class IsApplicationOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.job.company.owner == request.user 