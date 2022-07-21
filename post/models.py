from django.db import models
from helpers.models import BaseModel


# Create your models here.


class Category(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Region(BaseModel):
    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class News(BaseModel):
    title = models.CharField(max_length=128, verbose_name="Nomi")
    slug = models.CharField(max_length=128, unique=True)
    content = models.TextField()
    sub_content = models.CharField(max_length=256)
    images = models.FileField(upload_to="post/", blank=True)
    image_caption = models.CharField(max_length=128, null=True, blank=True)

    # published date and views count
    published_datetime = models.DateTimeField(auto_now_add=True)
    views_count = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True, blank=True, related_name="posts"
    )
    region = models.ForeignKey(
        Region, on_delete=models.CASCADE, null=True, blank=True, related_name="posts"
    )
    tag = models.ManyToManyField(Tag, null=True, blank=True, related_name="posts")

    # share content
    facebook_link = models.CharField(max_length=128)
    twitter_link = models.CharField(max_length=128)
    telegram_link = models.CharField(max_length=128)
    youtube_url = models.CharField(max_length=128, blank=True)

    # status
    is_main = models.BooleanField(default=False)
    is_top = models.BooleanField(default=False)
    is_article = models.BooleanField(default=False)
    is_editor_choice = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_video_news = models.BooleanField(default=False)
    is_interview = models.BooleanField(default=False)
    is_investigation = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=False)
    is_advertisement = models.BooleanField(default=False)


class AudioNews(BaseModel):
    title = models.CharField(max_length=128, verbose_name="Nomi")
    slug = models.CharField(max_length=128, unique=True)
    audio_file = models.FileField(upload_to="post/", blank=True)
    audio_duration = models.CharField(max_length=128, null=True, blank=True)
