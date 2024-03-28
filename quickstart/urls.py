from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
    path('blog/', BlogView.as_view(), name='blog'),
    path('blog/<int:id>/', BlogDetail.as_view(), name='blog_detail'),
    path('api-auth/', include("rest_framework.urls", namespace='rest_framework'))
]