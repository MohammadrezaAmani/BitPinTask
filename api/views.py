from rest_framework import generics
from .models import Content, Rating
from .serializers import ContentSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = PageNumberPagination

class ContentRatingView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    def get_object(self):
        user = self.request.user
        content_id = self.kwargs.get("pk")
        return Rating.objects.get(user=user, content_id=content_id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)
