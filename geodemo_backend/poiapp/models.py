from django.db import models

from djgeojson.fields import PointField

from jsonfield import JSONField

from django.contrib.postgres.fields import JSONField

from django.core.exceptions import ValidationError

from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel

from jsonschema import validate


class Genre(TitleSlugDescriptionModel, TimeStampedModel, models.Model):

    def __str__(self):              # __unicode__ on Python 2
        return self.slug


class Plugin(TitleSlugDescriptionModel, TimeStampedModel, models.Model):

    json_schema = JSONField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.slug


class Story(TitleSlugDescriptionModel, TimeStampedModel, models.Model):
    genre = models.ForeignKey(Genre, related_name='pois', blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.slug

    class Meta:
        verbose_name = 'story'
        verbose_name_plural = 'stories'


# Create your models here.
class POI(TitleSlugDescriptionModel, TimeStampedModel, models.Model):

    # GeoDjango-specific: a geometry field (MultiPolygonField), and
    # overriding the default manager with a GeoManager instance.
    mpoint = PointField(blank=True, null=True)
    story = models.ManyToManyField('Story', related_name='pois') #, through='StoryPOI')
    plugin = models.ForeignKey('Plugin', related_name='pois')
    metadata = JSONField(blank=True, null=True)

    def __str__(self):              # __unicode__ on Python 2
        return self.slug

    def clean(self):
        schema = self.plugin.json_schema
        if schema:
            print(validate(self.metadata, schema))
            if validate(self.metadata, schema):
                raise ValidationError({'metadata': ('Metadata must match plugin schema.')})

    class Meta:
        verbose_name_plural = 'Points of Interest'

# Create a through table for the above M2M relationship, no longer needed.
# class StoryPOI(models.Model):
#     story = models.ForeignKey(Story, on_delete=models.CASCADE)
#     poi = models.ForeignKey(POI, on_delete=models.CASCADE)
#     position = models.IntegerField()
#     active = models.BooleanField(default=True)
