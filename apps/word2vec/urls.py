from django.conf.urls import url
from word2vec import views

urlpatterns = [

url(r'^', views.Word2VecService.as_view()),
]
