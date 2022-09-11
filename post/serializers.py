from rest_framework import serializers
from .models import News, Category, Region, AudioNews


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ("id", "name")


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = News
        fields = "__all__"


class AudioNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioNews
        fields = "__all__"
