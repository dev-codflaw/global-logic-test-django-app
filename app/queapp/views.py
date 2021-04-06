from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Question, Answer
from .serializers import QuestionSerializer


class QuestionView(APIView):

    def get(self, request, pk):
        queryset = Question.objects.get(pk=pk)
        serialized_content = QuestionSerializer(queryset)

        content = {'data': 'post content'}
        return Response(serialized_content.data)

# class ArticleList(APIView):
#     # permission_classes = (AllowAny)

#     def get(self, request):
#         queryset = Post.objects.all().filter(status=True)
#         serialized_content = PostSerializer(queryset, many=True)
#         # print(serializer.data)
#         # content = {'data': 'post content'}
#         return Response(serialized_content.data)