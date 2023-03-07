from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse('Good Evening to All...')

def sample(q,v):
	return HttpResponse("Hi Good Evening {}".format(v))