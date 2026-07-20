from rest_framework.routers import DefaultRouter
from .views import ApplicationViewSet, EmployerDashboardView
from django.urls import path

router = DefaultRouter()
router.register(r"applications", ApplicationViewSet, basename = "applications")

urlpatterns = [
    path(
        "employer/dashboard/",
        EmployerDashboardView.as_view(),
        name="employer-dashboard",
    ),
]

urlpatterns += router.urls