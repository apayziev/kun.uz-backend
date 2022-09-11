from post.models import News, Category, Region, AudioNews
from post.serializers import (
    NewsSerializer,
    CategorySerializer,
    RegionSerializer,
    AudioNewsSerializer,
)
from helpers.pagination import CustomPagination
from rest_framework import generics

# Create your views here.

# All news
class AllNewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = CustomPagination


# News by category
class NewsByCategoryList(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get("slug_name", None):
            queryset = queryset.filter(category__slug=self.kwargs["slug_name"])

        return queryset


# News by region
class NewsByRegionList(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    queryset = News.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get("slug_name", None):
            queryset = queryset.filter(region__slug=self.kwargs["slug_name"])

        return queryset


# is_top news
class IsTopNewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    queryset = News.objects.all()
    queryset = queryset.filter(is_top=True)
    queryset = queryset.order_by("-published_datetime")
    queryset = queryset.distinct()
    queryset = queryset[:10]


# is_main news
class IsMainNewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    queryset = News.objects.all()
    queryset = queryset.filter(is_main=True)
    queryset = queryset[:5]


# is_article news
class IsArticleNewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = CustomPagination
    queryset = News.objects.all()
    queryset = queryset.filter(is_article=True)
    queryset = queryset[:5]


# All audio news
class AllAudioList(generics.ListAPIView):
    queryset = AudioNews.objects.all()
    serializer_class = AudioNewsSerializer
    pagination_class = CustomPagination
