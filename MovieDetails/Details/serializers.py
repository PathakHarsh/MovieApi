from django.db.models import fields
from rest_framework import serializers
from Details.models import Movie
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"