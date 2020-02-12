from django.shortcuts import render, HttpResponse
from django.views import View
# Create your views here.

class Word2VecService(View):

    def get(self, request):

        return HttpResponse("GET Service From Word2VecService")

    def post(self, request):

        return HttpResponse("POST service from Word2VecService")