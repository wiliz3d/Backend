from django.urls import path
from api.views import *


urlpatterns = [
    path('', BookAPIView.as_view()),
]
