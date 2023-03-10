from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def register(request):
	if request.method == "POST":
		a = request.POST['uname']
		b = request.POST['pd']
		c = request.POST['em']
		return render(request,'html/display.html',{'user':a,'mail':c})
	return render(request,'html/register.html')

def student(request):
	return render(request,'html/std.html')
