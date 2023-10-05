from rest_framework import generics
from .models import Content, Rating
from .serializers import ContentSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Prefetch

from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


class ContentListView(generics.ListAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    pagination_class = PageNumberPagination
    renderer_classes = (JSONRenderer,)
    serializer_class = ContentSerializer

    def get_queryset(self, user_id):
        return Content.objects.select_related("rating").prefetch_related(
            Prefetch(
                "rating__user_ratings",
                queryset=Rating.objects.filter(user__id=user_id),
                to_attr="limited_user",
            )
        )

    def get(self, request, format=None):
        try:
            content_list = self.get_queryset(request.user.id)
            if content_list:
                serializer = ContentSerializer(content_list, many=True)
                return Response(serializer.data)
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


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
