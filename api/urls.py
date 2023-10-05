from django.urls import path
from .views import ContentListView, ContentDetailView, ContentRatingView

urlpatterns = [
    path("content/", ContentListView.as_view(), name="content-list"),
    path("content/<int:pk>/", ContentDetailView.as_view(), name="content-detail"),
    path(
        "content/<int:content_id>/rate/",
        ContentRatingView.as_view(),
        name="content-rate",
    ),
]
