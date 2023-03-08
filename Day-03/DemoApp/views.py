from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def demo(request):
	return HttpResponse('Good Evening to All...')

def sample(q,v):
	return HttpResponse("Hi Good Evening {}".format(v))

def nme(request,y,h):
	return HttpResponse("Hi Good Morning {} your age is: {}".format(h,y))

def naveen(q,b):
	return HttpResponse("<h1>Hi Good Evening {} </h1>".format(b))

def color(request,e,h):
    return HttpResponse("<h2>hi good afternoon <span style='color:red'> {} </span>and your age is:<span style='color:green'> {} </span></h2>".format(e,h))

def jk(request):
	return HttpResponse("<html><head><title>Demo</title></head><body><h3>Sample html structure</h3></body></html>")

def pyk(request):
	return HttpResponse("<script>alert('Welcome')</script>")

def four(request,y):
	return HttpResponse("<script>alert('welcome {}')</script>".format(y))

def bjk(request):
	return render(request,'sa/sample.html')

def hyk(request,b):
	return render(request,'sa/test.html',{'g':b})









