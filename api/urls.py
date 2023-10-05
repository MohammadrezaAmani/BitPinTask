from django.urls import path
from .views import ContentListView, ContentRatingView

urlpatterns = [
    path("content/", ContentListView.as_view(), name="content-list"),
    path("content/<int:pk>/rate/", ContentRatingView.as_view(), name="content-rate"),
]
