from django.conf.urls import url
from tokenizer import views

urlpatterns = [
    url(r'^tokenizer', views.DocTokenizerService.as_view()),
]