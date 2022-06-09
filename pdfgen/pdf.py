import pdfkit

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response

from professor.serializers import TopicSerializer
from professor.models import *




@api_view(['GET'])
def generate_pdf(request):
    test = Topics.objects.get(id=3)
    theory = Questions.objects.filter(questiontypeid_id=2)
    problem = Questions.objects.filter(questiontypeid_id=3)

    context = {
        "name": test.name,
        "subject": test.chapterid.subjectid.name,
        "chapter": test.chapterid.name
    }


    template = get_template('index.html')
    html = template.render(context=context)
    pdf = pdfkit.from_string(html, False, options={})

    response = HttpResponse(pdf, content_type='topic/pdf')
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'

    return response