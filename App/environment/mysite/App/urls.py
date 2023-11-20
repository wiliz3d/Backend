from django.urls import path
from App.views import *


urlpatterns = [
    path('', BookListView.as_view(), name='home'),
]
