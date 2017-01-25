from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from rest_framework import routers

from geodemo_backend.poiapp.views import PluginViewSet, GenreViewSet, POIViewSet, StoryViewSet
from geodemo_backend.poiapp.views import schema_view


router = routers.DefaultRouter()
router.register(r'plugins', PluginViewSet)
router.register(r'genres', GenreViewSet)
router.register(r'stories', StoryViewSet)
router.register(r'poi', POIViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(router.urls)),
    url(r'^docs/', schema_view),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
]
