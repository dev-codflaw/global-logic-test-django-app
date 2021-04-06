from django.urls import path
from . import views

urlpatterns = [
    path('question/<pk>/',views.QuestionView().as_view(), name='question'),
]   