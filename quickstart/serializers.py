from rest_framework import serializers
from .models import *
from django.db.models import fields


class BlogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'date', 'name']
        lookup_fields = 'title'