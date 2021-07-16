from rest_framework import serializers

from .models import Language


class LanguageSerializer(serializers.ModelSerializer):  # HyperlinkedModelSerializer
    class Meta:
        model = Language
        fields = ('id', 'name', 'paradigm')  # 'url'
