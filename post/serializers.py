from rest_framework import serializers
from .models import News, Tag, Category, Region, AudioNews


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name")


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    tag = TagSerializer(many=True)
    category = CategorySerializer()

    class Meta:
        model = News
        fields = "__all__"


class AudioNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioNews
        fields = "__all__"
