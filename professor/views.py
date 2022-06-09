from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# from professor.auth import create_access_token, create_refresh_token
from professor.models import *
from professor.serializers import *

#
# class RegisterAPIView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)


#
# class LoginAPIView(APIView):
#     def post(self, request):
#         user = Users.objects.filter(username=request.data['username']).first()
#
#         if not user:
#             raise APIException('Invalid credentials!')
#
#         if not user.check_password(request.data['password']):
#             raise APIException('Invalid credentials!')
#
#         access_token = create_access_token(user.id)
#         refresh_token = create_refresh_token(user.id)
#
#         response = Response()
#
#         response.set_cookie(key='refreshToken', value=refresh_token, httponly=True)
#         response.data = {
#             'token': access_token
#         }
#
#         return response


class SubjectsViewSet(viewsets.ModelViewSet):

    # http://127.0.0.1:8000/subjects/ только GET

    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer


    def list(self, request):
        queryset = Subjects.objects.all()
        serializer = SubjectSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)



class ChaptersViewSet(viewsets.ModelViewSet):

    # http://127.0.0.1:8000/chapters/ Get список разделов Post создание новой ТОЛЬКО название раздела текстовое поле

    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer

    def get_queryset(self):
        return self.queryset.filter(subjectid=3)

    def perform_create(self, serializer):
        serializer.save()


# class QuestionThemeViewSet(viewsets.ModelViewSet):
#     # permission_classes = (IsAuthenticated,)
#     queryset = Questionthemes.objects.all()
#     serializer_class = QuestionThemeSerializer
#
#
#
#
#
# class QuestionViewSet(viewsets.ModelViewSet):
#
#     queryset = Questions.objects.all()
#     serializer_class = QuestionSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(created_by=self.request.user)
#
#     def perform_create(self, serializer):
#         serializer.save(created_by=self.request.user)
#
#     def perform_update(self):
#         self.save()
#
