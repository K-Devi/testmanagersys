from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Subjects, Chapters, Questionthemes, Questions, Users, Topics


# class UserSerializer(ModelSerializer):
#     class Meta:
#         model = Users
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {
#             'password': {'write_only': True}
#         }


# class userProfileSerializer(serializers.ModelSerializer):
#
#     user = serializers.StringRelatedField(read_only=True)
#
#     class Meta:
#         model = Users
#         fields = '__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subjects
        fields = ['id', 'name', 'description']


class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapters
        fields = ('id', 'name')


class QuestionThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questionthemes
        fields = ('id', 'name')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ('id', 'body', 'active', 'questiontypeid', 'questionthemeid')


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topics
        fields = ('id', 'chapterid', 'name', 'timelimit')