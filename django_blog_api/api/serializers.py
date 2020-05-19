from rest_framework import serializers
from django.contrib.auth import get_user_model
from taggit_serializer.serializers import (TagListSerializerField, TagList,
                                           TaggitSerializer)

from posts.models import Post


class TagSlugListSerializerField(TagListSerializerField):

    def to_representation(self, value):
        if not isinstance(value, TagList):
            if not isinstance(value, list):
                if self.order_by:
                    tags = value.all().order_by(*self.order_by)
                else:
                    tags = value.all()
                value = [{'slug': tag.slug, 'name': tag.name} for tag in tags]
            value = TagList(value, pretty_print=self.pretty_print)

        return value


class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagSlugListSerializerField()

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created', 'tags')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'email')
