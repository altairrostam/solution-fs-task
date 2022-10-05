from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .api import *
app_name = 'unity'

urlpatterns = [
    path('emails/',EmailList.as_view()),
    path('emails/<str:idEmail>',EmailDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)