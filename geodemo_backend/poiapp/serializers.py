from rest_framework import serializers
from rest_framework.fields import JSONField

from geodemo_backend.poiapp.models import Plugin, Story, Genre, POI


class PluginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plugin
        lookup_field = 'slug'
        # fields = ('url', 'title', 'description')


class NestedPluginSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Plugin
        lookup_field = 'slug'
        fields = ('slug', 'url')


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        lookup_field = 'slug'
        # fields = ('url', 'title', 'description')


class NestedStorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        lookup_field = 'slug'
        fields = ('slug', 'url')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Genre
        lookup_field = 'slug'
        # fields = ('url', 'title', 'description')


class POISerializer(serializers.HyperlinkedModelSerializer):
    plugin = NestedPluginSerializer()
    story = NestedStorySerializer(many=True)
    metadata = JSONField()

    class Meta:
        model = POI
        # fields = ('url', 'title', 'description')
        # lookup_field = 'slug'


# from rest_framework_gis.serializers import GeoFeatureModelSerializer

# from geodemo_backend.poiapp.models import POI


# class POISerializer(GeoFeatureModelSerializer):
#     class Meta:
#         model = POI
#         geo_field = 'mpoly'
#         id_field = 'slug'
#         auto_bbox = True
#         # fields = ('url', 'title', 'description')