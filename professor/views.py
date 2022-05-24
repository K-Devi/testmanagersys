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
    # permission_classes = (IsAuthenticated,)
    queryset = Subjects.objects.all()
    serializer_class = SubjectSerializer


    def list(self, request):
        queryset = Subjects.objects.all()
        serializer = SubjectSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)


class ChaptersViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Chapters.objects.all()
    serializer_class = ChapterSerializer

class QuestionThemeViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Questionthemes.objects.all()
    serializer_class = QuestionThemeSerializer




class QuestionViewSet(viewsets.ModelViewSet):
# def get_questions(request):
#     theme_id = request.GET.get('theme_id', '')
    queryset = Questions.objects.all()
    #
    # if theme_id:
    #     questions = questions.filter(chapters__in=[int(theme_id)])

    serializer_class = QuestionSerializer
    # return Response(serializer.data)


# def add_question(request):
