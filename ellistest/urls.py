from django.contrib import admin
from django.conf.urls import include, url
from ellistest.views import JSONWebTokenAPIView,ProtectedView
from rest_framework.routers import DefaultRouter

default = DefaultRouter()
default.register(r'ellis',ProtectedView,basename='ellis')

urlpatterns = [
    url(r'^login$', JSONWebTokenAPIView.as_view(), name='login'),
    url(r'^', include(default.urls)),
]