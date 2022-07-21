from django.urls import path
from post.views import *


urlpatterns = [
    path("news/", AllNewsList.as_view(), name="news"),
    path(
        "news/<slug:slug_name>/", NewsByCategoryList.as_view(), name="news_by_category"
    ),
    path("news/<slug:slug_name>/", NewsByRegionList.as_view(), name="news_by_region"),
    path("news/is_top/", IsTopNewsList.as_view(), name="is_top_news"),
    path("news/is_main/", IsMainNewsList.as_view(), name="is_main_news"),
    path("news/is_article/", IsArticleNewsList.as_view(), name="is_article_news"),
    path("audio/", AllAudioList.as_view(), name="audio"),
]
