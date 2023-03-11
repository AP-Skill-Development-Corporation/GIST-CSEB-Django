from django.shortcuts import render,redirect
from . forms import Streg

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	k = Streg()
	if request.method == "POST":
		k = Streg(request.POST)
		if k.is_valid():
			k.save()
			return redirect('/')
	return render(request,'html/reg.html',{'h':k})