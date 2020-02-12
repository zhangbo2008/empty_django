from django.conf.urls import url
from extractor import views

urlpatterns = [
    url(r'extractor',views.PolicyExtractorService.as_view()),
]
