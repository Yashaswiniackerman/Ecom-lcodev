from rest_framework import serializers

from .models import Category
#HyperlinkModelSerializer akbeku .Serializer atra

class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = ('name', 'description')

