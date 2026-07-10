from rest_framework.routers import DefaultRouter
from .views import JobViewSets

router = DefaultRouter()
router.register(r'jobs', JobViewSets, basename='job')

urlpatterns = router.urls