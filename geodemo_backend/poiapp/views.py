from rest_framework.decorators import api_view, renderer_classes
from rest_framework import response, schemas
from rest_framework import viewsets

import rest_framework_filters as filters
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer


from geodemo_backend.poiapp.serializers import PluginSerializer, GenreSerializer, POISerializer, StorySerializer
from geodemo_backend.poiapp.models import Plugin, Story, Genre, POI


class PluginFilter(filters.FilterSet):
    class Meta:
        model = Plugin
        fields = {'slug': ['contains'], 'title': ['contains'], 'description': ['contains']}


class StoryFilter(filters.FilterSet):
    class Meta:
        model = Story
        fields = {'slug': ['contains'], 'title': ['contains'], 'description': ['contains']}


class GenreFilter(filters.FilterSet):
    class Meta:
        model = Genre
        fields = {'slug': ['contains'], 'title': ['contains'], 'description': ['contains']}


class POIFilter(filters.FilterSet):
    genre = filters.RelatedFilter(GenreFilter, name='genre')
    story = filters.RelatedFilter(StoryFilter, name='story')
    class Meta:
        model = POI
        fields = {'slug': ['contains'], 'title': ['contains'], 'description': ['contains']}


@api_view()
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Geodemo API')
    return response.Response(generator.get_schema(request=request))


# Create your views here.
class PluginViewSet(viewsets.ModelViewSet):
    queryset = Plugin.objects.all()
    filter_class = PluginFilter
    serializer_class = PluginSerializer
    # lookup_field = 'slug'


# Create your views here.
class StoryViewSet(viewsets.ModelViewSet):
    queryset = Story.objects.all()
    filter_class = StoryFilter
    serializer_class = StorySerializer
    # lookup_field = 'slug'


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    filter_class = GenreFilter
    serializer_class = GenreSerializer
    # lookup_field = 'slug'


class POIViewSet(viewsets.ModelViewSet):
    queryset = POI.objects.all()
    filter_class = POIFilter
    serializer_class = POISerializer
    # lookup_field = 'slug'
