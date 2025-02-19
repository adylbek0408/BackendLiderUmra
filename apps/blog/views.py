from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Blog, Lesson, DetailDescription, FAQ
from .serializers import BlogSerializer, LessonSerializer, DetailDescriptionSerializer, FAQSerializer


class BlogViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Blog.objects.prefetch_related('desc_blogs').all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'created_at']
    search_fields = ['name']


class LessonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'created_at']
    search_fields = ['name']


class DetailDescriptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DetailDescription.objects.select_related('blog').all()
    serializer_class = DetailDescriptionSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog', 'lesson']
    search_fields = ['text']
    

class FAQViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


