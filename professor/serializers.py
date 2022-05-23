from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import Subjects, Chapters, Questionthemes, Questions


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField(max_length=255)
#     username = serializers.CharField(max_length=255, read_only=True)
#     password = serializers.CharField(max_length=128, write_only=True)
    # token = serializers.CharField(max_length=255, read_only=True)
    #
    # def validate(self, data):
    #     email = data.get('email', None)
    #     password = data.get('password', None)
    #
    #     if email is None:
    #         raise serializers.ValidationError(
    #             'An email address is required to log in.'
    #         )
    #
    #     if password is None:
    #         raise serializers.ValidationError(
    #             'A password is required to log in.'
    #         )
    #
    #     user = authenticate(email=email, password=password)
    #
    #     if user is None:
    #         raise serializers.ValidationError(
    #             'A user with this email and password was not found.'
    #         )
    #     return {
    #         'email': user.email,
    #         'username': user.username,
    #         'token': user.token
    #     }


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
        fields = ('id', 'body', 'active')

#
# class TopicSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Topics
#         fields = ('id', 'lesson_id', 'question', 'answer', 'op1', 'op2', 'op3')