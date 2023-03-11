from django.shortcuts import render,redirect
from .models import Student

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
	y = Student.objects.all()
	if request.method == "POST":
		a = request.POST['rn']
		b = request.POST['nm']
		c = request.POST['em']
		d = request.POST['ag']
		w = Student(rno=a,nme=b,em=c,age=d)
		w.save()
		return redirect('/stdnt')
	return render(request,'html/std.html',{'g':y})

def studup(request,h):
	a = Student.objects.get(id=h)
	if request.method == "POST":
		a.rno = request.POST['rn']
		a.nme = request.POST['nm']
		a.em = request.POST['em']
		a.age = request.POST['ag']
		a.save()
		return redirect('/stdnt')
	return render(request,'html/stdup.html',{'t':a})

def studlte(request,u):
	k = Student.objects.get(id=u)
	if request.method == "POST":
		k.delete()
		return redirect('/stdnt')
	return render(request,'html/stdt.html',{'p':k})
