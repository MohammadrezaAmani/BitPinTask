from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContentViewSet, RatingViewSet

router = DefaultRouter()
router.register(r"contents", ContentViewSet)
router.register(r"ratings", RatingViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
