from django.conf.urls import url
from matcher import views

urlpatterns = [
    url(r'^policyMatchList', views.PolicyMatchService.as_view()),
    url(r'^policySearchList', views.PolicySearchService.as_view()),
    url(r'^companyMatchList', views.CompanyMatchService.as_view()),
]
