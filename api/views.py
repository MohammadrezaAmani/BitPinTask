from rest_framework import generics, permissions
from .models import Content, Rating
from .serializers import ContentSerializer, RatingSerializer

class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentDetailView(generics.RetrieveAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRatingView(generics.CreateAPIView, generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        user = self.request.user
        content_id = self.kwargs['content_id']
        return Rating.objects.get(user=user, content_id=content_id)