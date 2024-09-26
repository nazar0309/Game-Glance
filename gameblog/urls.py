from . import views
from django.urls import path

urlpatterns = [
    path('', views.hello_blog, name='home'),
]