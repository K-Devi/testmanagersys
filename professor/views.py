from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .models import *
from .serializers import *

from rest_framework.response import Response
from rest_framework import viewsets, status, permissions
from rest_framework.views import APIView
# from .renderers import UserJSONRenderer
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.generics import ListAPIView, CreateAPIView
# from rest_framework.status import (
#     HTTP_201_CREATED,
#     HTTP_400_BAD_REQUEST
# )


# class LoginAPIView(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    # serializer_class = LoginSerializer

    # def post(self, request):
    #     user = request.data.get('user', {})
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
    # token
    #     return Response(serializer.data, status=status.HTTP_200_OK)


class SubjectsViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer

    def list(self, request):
        queryset = self.Subjects.objects.all()
        serializer = SubjectSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ChaptersViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer


#
# def get_themes(request):
#     chapter_id = request.GET.get('chapter_id', '')
#     themes = Questionthemes.objects.all()
#
#     if chapter_id:
#         themes = themes.filter(themes__in=[int(chapter_id)])
#
#     serializer = ChapterSerializer(themes, many=True)
#     return Response(serializer.data)
#
#
# def get_questions(request):
#     theme_id = request.GET.get('theme_id', '')
#     questions = Questions.objects.all()
#
#     if theme_id:
#         questions = questions.filter(chapters__in=[int(theme_id)])
#
#     serializer = QuestionSerializer(questions, many=True)
#     return Response(serializer.data)
#
#
# class QuestionView(viewsets.ModelViewSet):
#     serializer_class = QuestionSerializer
#     queryset = Questions.objects.all()
#
#     def add_question(self, request):
#         serializer = QuestionSerializer(data=request.data)
#         if serializer.is_valid():
#             assignment = serializer.create(request)
#             if assignment:
#                 return Response(status=HTTP_201_CREATED)
#         return Response(status=HTTP_400_BAD_REQUEST)
