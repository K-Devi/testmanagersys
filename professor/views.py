from rest_framework import viewsets
from rest_framework.decorators import api_view
import base64

from rest_framework.response import Response



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


class QuestionThemeFirstViewSet(viewsets.ModelViewSet):

    queryset = Questionthemes.objects.all()
    serializer_class = QuestionThemeSerializer

    def get_queryset(self):
        return self.queryset.filter(chaptertheme__chaptersid=5)

    def perform_create(self, serializer):
        serializer.save()


# class QuestionThemeSecondViewSet(viewsets.ModelViewSet):
#
#     queryset = Questionthemes.objects.all()
#     serializer_class = QuestionThemeSerializer
#
#     def get_queryset(self):
#         return self.queryset.filter(chaptertheme__chaptersid=4)
#
#     def perform_create(self, serializer):
#         serializer.save()


@api_view(['GET'])
def get_questions1(request):
    questions = Questions.objects.filter(questionthemeid=2)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_questions2(request):
    if request.method == 'GET':
        questions = Questions.objects.filter(questionthemeid=3)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_questions3(request):
    questions = Questions.objects.filter(questionthemeid=4)
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Questions.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        return self.queryset.all()

    def perform_create(self, serializer):
        serializer.save()



    #
    #
    # if request.method == 'POST':
    #     serializer = QuestionSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #
    # questions = Questions.objects.filter(questionthemeid=4)
    # serializer = QuestionSerializer(questions, many=True)
    # return Response(serializer.data)


class ImageViewSet(viewsets.ModelViewSet):

    #http://127.0.0.1:8000/images/ через vue bytestring в норм изображение

    queryset = Images.objects.all()
    serializer_class = ImageSerializer

