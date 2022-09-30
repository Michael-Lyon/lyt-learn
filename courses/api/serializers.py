from asyncore import file_dispatcher
from dataclasses import field

from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.response import Response

from ..models import Content, Course, Module, Subject


class ItemRelatedField(serializers.RelatedField):
    def to_representation(self, value):
        return value.render()


class ContentSerializer(serializers.ModelSerializer):
    item = ItemRelatedField(read_only=True)

    class Meta:
        model = Content
        fields = [
            'order', 'item'
        ]
class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id', 'title', 'slug']


class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = [
            'order', 'title', 'description'
        ]


class CourseSerializer(serializers.ModelSerializer):
    modules = ModuleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug',
            'overview', 'created', 'owner', 'modules'
        ]




class ModuleWithContentsSerializer(serializers.ModelSerializer):
    contents = ContentSerializer(many=True)
    class Meta:
        model = Module
        fields = [
            'order', 'title', 'description', 'contents'
        ]

    


class CourseWithContentsSerializer(serializers.ModelSerializer):
    modules = ModuleWithContentsSerializer(many=True)

    class Meta:
        model = Course
        fields = [
            'id', 'subject', 'title', 'slug',
            'overview', 'created', 'owner', 'modules'
        ]